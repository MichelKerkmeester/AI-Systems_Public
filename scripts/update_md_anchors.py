#!/usr/bin/env python3
import re
import sys
from pathlib import Path


HEADING_NUM_RE = re.compile(r"^(?P<hashes>#{1,6})(?P<space>\s+)(?P<num>\d+(?:\.\d+)*)(?P<punc>[\.)])?\s*(?P<rest>.*)$")

def is_code_fence(line: str) -> bool:
    return bool(re.match(r"^\s*```", line))

def parse_toc(lines):
    toc_start = None
    for i, line in enumerate(lines):
        if re.match(r"(?i)^##\s*(?:[\U0001F300-\U0001FAFF]\s*)?table of contents", line):
            toc_start = i
            break
    if toc_start is None:
        return {}, None, [], None

    # Collect up to next heading or horizontal rule
    mapping = {}
    order_ids = []
    num_pattern = re.compile(r"^\s*(?P<num>\d+)[\.)]\s*\[.*?\]\(#(?P<id>[^)]+)\)")
    bullet_pattern = re.compile(r"^\s*[-*+]\s*\[\s*(?:(?P<num2>\d+)[\.)]\s*)?.*?\]\(#(?P<id2>[^)]+)\)")

    toc_end = None
    for idx, line in enumerate(lines[toc_start+1:], start=toc_start+1):
        if re.match(r"^\s*---+\s*$", line) or re.match(r"^#{1,6}\s", line):
            toc_end = idx
            break
        m = num_pattern.match(line)
        if m:
            try:
                n = int(m.group('num'))
                anchor = m.group('id').strip()
                mapping[n] = anchor
                order_ids.append(anchor)
            except Exception:
                pass
            continue
        m2 = bullet_pattern.match(line)
        if m2:
            num2 = m2.group('num2')
            id2 = m2.group('id2')
            if id2:
                anchor = id2.strip()
                order_ids.append(anchor)
                if num2:
                    try:
                        n = int(num2)
                        mapping[n] = anchor
                    except Exception:
                        pass
    if toc_end is None:
        toc_end = len(lines)
    return mapping, toc_start, order_ids, toc_end


_TOC_NUM_RE = re.compile(r"^(\s*)(\d+)([\.)])\s*\[(?P<text>[^\]]+)\]\(#(?P<id>[^)]+)\)(.*)$")
_TOC_BULLET_RE = re.compile(r"^(\s*)[-*+]\s*\[(?P<text>[^\]]+)\]\(#(?P<id>[^)]+)\)(.*)$")

def uppercase_toc_line(line: str) -> str:
    m = _TOC_NUM_RE.match(line)
    if m:
        text = m.group('text')
        return f"{m.group(1)}{m.group(2)}{m.group(3)} [{text.upper()}](#{m.group('id')}){m.group(6)}"
    m = _TOC_BULLET_RE.match(line)
    if m:
        text = m.group('text')
        pre = line[:m.start('text')]
        post = line[m.end('text'):]
        return f"{pre}{text.upper()}{post}"
    return line

def has_anchor_above(lines, idx):
    # Look up to 2 lines above for an anchor tag
    start = max(0, idx-2)
    for j in range(idx-1, start-1, -1):
        s = lines[j].strip()
        if not s:
            continue
        if s.lower().startswith('<a ') and 'id=' in s.lower():
            mid = re.search(r"id=\"([^\"]+)\"", s)
            return True, (mid.group(1) if mid else None), j
        # If we hit non-empty, non-anchor content, stop
        break
    return False, None, None

def upper_after_number(text: str) -> str:
    # Preserve emojis and other symbols, uppercase letters
    return text.upper()

def process_file(path: Path) -> bool:
    original = path.read_text(encoding='utf-8')
    lines = original.splitlines()

    toc_map, toc_start, toc_order, toc_end = parse_toc(lines)

    in_code = False
    changed = False
    new_lines = []
    seen_anchor_ids = set()

    toc_seq_index = 0
    for i, line in enumerate(lines):
        # Uppercase ToC entries if within ToC block
        if toc_start is not None and toc_end is not None and (i > toc_start and i < toc_end):
            new_line = uppercase_toc_line(line)
            if new_line != line:
                changed = True
            new_lines.append(new_line)
            continue

        if is_code_fence(line):
            in_code = not in_code
            new_lines.append(line)
            continue

        if not in_code:
            # Remove duplicated existing anchors
            m_anchor = re.match(r'^\s*<a id=\"([^\"]+)\"></a>\s*$', line)
            if m_anchor:
                aid = m_anchor.group(1)
                if aid in seen_anchor_ids:
                    changed = True
                    continue
                else:
                    seen_anchor_ids.add(aid)
                    new_lines.append(line)
                    continue

            m = HEADING_NUM_RE.match(line)
            if m:
                # Determine base number (first segment)
                num_str = m.group('num')
                try:
                    base_num = int(num_str.split('.')[0])
                except Exception:
                    base_num = None

                # Uppercase the rest of the title
                rest = m.group('rest')
                upper_rest = upper_after_number(rest)
                if rest != upper_rest:
                    changed = True
                    line = f"{m.group('hashes')}{m.group('space')}{num_str}{m.group('punc') or ''} {upper_rest}".rstrip()

                # Insert anchor if ToC provides id for this base number
                if base_num is not None and base_num in toc_map:
                    want_id = toc_map[base_num]
                    has_a, existing_id, anchor_idx = has_anchor_above(new_lines, len(new_lines))
                    if not has_a:
                        if new_lines and new_lines[-1].strip():
                            new_lines.append("")
                        if want_id not in seen_anchor_ids:
                            new_lines.append(f"<a id=\"{want_id}\"></a>")
                            seen_anchor_ids.add(want_id)
                        new_lines.append("")
                        changed = True
                    else:
                        if existing_id and existing_id != want_id and anchor_idx is not None:
                            new_lines[anchor_idx] = re.sub(r"id=\"[^\"]+\"", f'id="{want_id}"', new_lines[anchor_idx])
                            changed = True

                    if m.group('hashes') == '##' and toc_start is not None and i > toc_start and toc_order:
                        toc_seq_index += 1

                new_lines.append(line)
                continue

            # H2 headings without numbering: map by ToC order when available
            if re.match(r"^##\s+", line) and toc_start is not None and i > toc_start and toc_order:
                has_a, existing_id, anchor_idx = has_anchor_above(new_lines, len(new_lines))
                if not has_a and toc_seq_index < len(toc_order):
                    want_id = toc_order[toc_seq_index]
                    if new_lines and new_lines[-1].strip():
                        new_lines.append("")
                    if want_id not in seen_anchor_ids:
                        new_lines.append(f"<a id=\"{want_id}\"></a>")
                        seen_anchor_ids.add(want_id)
                    new_lines.append("")
                    changed = True
                    toc_seq_index += 1
                elif not has_a:
                    toc_seq_index += 1
                new_lines.append(line)
                continue

        new_lines.append(line)

    if changed:
        path.write_text("\n".join(new_lines) + ("\n" if original.endswith("\n") else ""), encoding='utf-8')
    return changed


def main(argv):
    if len(argv) < 2:
        print("Usage: update_md_anchors.py <file1.md> [file2.md ...]", file=sys.stderr)
        return 2
    changed_any = False
    for arg in argv[1:]:
        p = Path(arg)
        if not p.exists() or not p.is_file():
            continue
        changed = process_file(p)
        if changed:
            print(f"Updated: {p}")
            changed_any = True
    return 0 if changed_any else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
