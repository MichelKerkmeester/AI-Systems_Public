#!/usr/bin/env python3
"""
Documentation Audit Script
Performs regular audits of documentation health
"""

import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any

class DocAuditor:
    """Documentation health auditor"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.docs_path = self.base_path / "docs"
        self.audit_results = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {},
            "issues": {},
            "recommendations": []
        }
    
    def count_documentation_files(self) -> Dict[str, int]:
        """Count documentation files by type"""
        counts = {
            "total_files": 0,
            "readme_files": 0,
            "guide_files": 0,
            "reference_files": 0,
            "example_files": 0
        }
        
        for md_file in self.docs_path.rglob("*.md"):
            counts["total_files"] += 1
            
            name_lower = md_file.name.lower()
            if "readme" in name_lower:
                counts["readme_files"] += 1
            elif any(x in name_lower for x in ["guide", "tutorial"]):
                counts["guide_files"] += 1
            elif any(x in name_lower for x in ["reference", "api", "command"]):
                counts["reference_files"] += 1
            elif "example" in name_lower:
                counts["example_files"] += 1
        
        return counts
    
    def check_documentation_freshness(self) -> List[Dict[str, Any]]:
        """Find stale documentation"""
        stale_docs = []
        cutoff_date = datetime.now() - timedelta(days=90)  # 3 months
        
        for md_file in self.docs_path.rglob("*.md"):
            stat = md_file.stat()
            mod_time = datetime.fromtimestamp(stat.st_mtime)
            
            if mod_time < cutoff_date:
                stale_docs.append({
                    "file": str(md_file.relative_to(self.base_path)),
                    "last_modified": mod_time.strftime("%Y-%m-%d"),
                    "age_days": (datetime.now() - mod_time).days
                })
        
        return sorted(stale_docs, key=lambda x: x["age_days"], reverse=True)
    
    def check_missing_documentation(self) -> List[str]:
        """Identify areas missing documentation"""
        missing = []
        
        # Check for expected documentation
        expected_docs = {
            "docs/CONTRIBUTING.md": "Contribution guidelines",
            "docs/CHANGELOG.md": "Change history",
            "docs/API.md": "API reference",
            "docs/SECURITY.md": "Security guidelines"
        }
        
        for path, description in expected_docs.items():
            if not (self.base_path / path).exists():
                missing.append(f"{path} - {description}")
        
        # Check each MCP has documentation
        mcp_dir = self.docs_path / "technical" / "mcp"
        if mcp_dir.exists():
            for mcp_subdir in mcp_dir.iterdir():
                if mcp_subdir.is_dir():
                    readme = mcp_subdir / "README.md"
                    if not readme.exists():
                        missing.append(f"{readme.relative_to(self.base_path)} - MCP documentation")
        
        return missing
    
    def analyze_documentation_coverage(self) -> Dict[str, float]:
        """Analyze documentation coverage by directory"""
        coverage = {}
        
        # Check code directories for corresponding docs
        code_dirs = {
            "logic": self.base_path / "logic",
            "hooks": self.base_path / "hooks",
            "scripts": self.base_path / "scripts"
        }
        
        for name, code_dir in code_dirs.items():
            if not code_dir.exists():
                continue
                
            # Count Python files
            py_files = list(code_dir.rglob("*.py"))
            
            # Count documented files (rough estimate)
            doc_dir = self.docs_path / name
            documented = 0
            
            if doc_dir.exists():
                # Estimate based on doc file count
                doc_files = list(doc_dir.rglob("*.md"))
                documented = min(len(doc_files), len(py_files))
            
            if py_files:
                coverage[name] = (documented / len(py_files)) * 100
            else:
                coverage[name] = 100.0  # No code files
        
        return coverage
    
    def check_toc_consistency(self) -> List[Dict[str, Any]]:
        """Check if all docs have consistent TOCs"""
        issues = []
        
        for md_file in self.docs_path.rglob("*.md"):
            if md_file.name in ["INDEX.md", "UPDATE_REPORT.md"]:
                continue
                
            content = md_file.read_text()
            
            # Check for TOC
            has_toc = "## Table of Contents" in content or "## TOC" in content
            
            # Count headers
            header_count = content.count("\n## ") + content.count("\n### ")
            
            # Should have TOC if more than 3 sections
            if header_count > 3 and not has_toc:
                issues.append({
                    "file": str(md_file.relative_to(self.base_path)),
                    "issue": "Missing table of contents",
                    "headers": header_count
                })
        
        return issues
    
    def generate_recommendations(self):
        """Generate improvement recommendations"""
        recommendations = []
        
        # Based on file counts
        if self.audit_results["metrics"]["counts"]["example_files"] < 5:
            recommendations.append("Consider adding more example documentation")
        
        # Based on freshness
        stale_count = len(self.audit_results["metrics"]["stale_docs"])
        if stale_count > 5:
            recommendations.append(f"Update {stale_count} stale documentation files")
        
        # Based on coverage
        for area, coverage in self.audit_results["metrics"]["coverage"].items():
            if coverage < 50:
                recommendations.append(f"Improve {area} documentation coverage (currently {coverage:.0f}%)")
        
        # Based on missing docs
        if self.audit_results["issues"]["missing_docs"]:
            recommendations.append("Create missing documentation files")
        
        self.audit_results["recommendations"] = recommendations
    
    def run_audit(self):
        """Run complete documentation audit"""
        print("Running documentation audit...")
        
        # Collect metrics
        self.audit_results["metrics"]["counts"] = self.count_documentation_files()
        self.audit_results["metrics"]["stale_docs"] = self.check_documentation_freshness()
        self.audit_results["metrics"]["coverage"] = self.analyze_documentation_coverage()
        
        # Identify issues
        self.audit_results["issues"]["missing_docs"] = self.check_missing_documentation()
        self.audit_results["issues"]["toc_issues"] = self.check_toc_consistency()
        
        # Generate recommendations
        self.generate_recommendations()
        
        # Calculate health score
        total_files = self.audit_results["metrics"]["counts"]["total_files"]
        stale_files = len(self.audit_results["metrics"]["stale_docs"])
        missing_files = len(self.audit_results["issues"]["missing_docs"])
        toc_issues = len(self.audit_results["issues"]["toc_issues"])
        
        # Simple health score calculation
        health_score = 100
        health_score -= (stale_files / max(total_files, 1)) * 30  # 30% for freshness
        health_score -= min(missing_files * 5, 20)  # 20% for completeness
        health_score -= min(toc_issues * 2, 10)  # 10% for consistency
        
        avg_coverage = sum(self.audit_results["metrics"]["coverage"].values()) / max(len(self.audit_results["metrics"]["coverage"]), 1)
        health_score -= (100 - avg_coverage) * 0.4  # 40% for coverage
        
        self.audit_results["health_score"] = max(0, min(100, health_score))
    
    def save_report(self):
        """Save audit report"""
        report_path = self.docs_path / "AUDIT_REPORT.md"
        
        lines = ["# Documentation Audit Report", ""]
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"Health Score: **{self.audit_results['health_score']:.0f}%**")
        lines.append("")
        
        # File counts
        lines.append("## Documentation Metrics")
        counts = self.audit_results["metrics"]["counts"]
        lines.append(f"- Total files: {counts['total_files']}")
        lines.append(f"- README files: {counts['readme_files']}")
        lines.append(f"- Guide files: {counts['guide_files']}")
        lines.append(f"- Reference files: {counts['reference_files']}")
        lines.append(f"- Example files: {counts['example_files']}")
        lines.append("")
        
        # Coverage
        lines.append("## Documentation Coverage")
        for area, coverage in self.audit_results["metrics"]["coverage"].items():
            status = "✅" if coverage >= 80 else "⚠️" if coverage >= 50 else "❌"
            lines.append(f"- {area}: {coverage:.0f}% {status}")
        lines.append("")
        
        # Stale docs
        stale_docs = self.audit_results["metrics"]["stale_docs"]
        if stale_docs:
            lines.append(f"## Stale Documentation ({len(stale_docs)} files)")
            for doc in stale_docs[:10]:  # Show top 10
                lines.append(f"- {doc['file']} (last modified: {doc['last_modified']})")
            if len(stale_docs) > 10:
                lines.append(f"- ... and {len(stale_docs) - 10} more")
            lines.append("")
        
        # Missing docs
        missing = self.audit_results["issues"]["missing_docs"]
        if missing:
            lines.append("## Missing Documentation")
            for item in missing:
                lines.append(f"- {item}")
            lines.append("")
        
        # TOC issues
        toc_issues = self.audit_results["issues"]["toc_issues"]
        if toc_issues:
            lines.append("## Table of Contents Issues")
            for issue in toc_issues[:5]:
                lines.append(f"- {issue['file']}: {issue['issue']}")
            if len(toc_issues) > 5:
                lines.append(f"- ... and {len(toc_issues) - 5} more")
            lines.append("")
        
        # Recommendations
        if self.audit_results["recommendations"]:
            lines.append("## Recommendations")
            for rec in self.audit_results["recommendations"]:
                lines.append(f"- {rec}")
        
        report_path.write_text('\n'.join(lines))
        
        # Save JSON report
        json_path = self.docs_path / "audit-results.json"
        with open(json_path, 'w') as f:
            json.dump(self.audit_results, f, indent=2)
        
        return report_path

def main():
    """Run documentation audit"""
    auditor = DocAuditor()
    auditor.run_audit()
    report_path = auditor.save_report()
    
    print(f"\nAudit complete!")
    print(f"Health Score: {auditor.audit_results['health_score']:.0f}%")
    print(f"Report saved to: {report_path.relative_to(auditor.base_path)}")
    
    # Show summary
    if auditor.audit_results["recommendations"]:
        print("\nTop recommendations:")
        for rec in auditor.audit_results["recommendations"][:3]:
            print(f"- {rec}")

if __name__ == "__main__":
    main()