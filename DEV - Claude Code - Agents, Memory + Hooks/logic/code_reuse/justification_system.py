#!/usr/bin/env python3
"""
Justification System - New File Justification
Requires exhaustive analysis before allowing new files and maintains audit trail
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum


class JustificationStatus(Enum):
    """Status of file creation justification"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    NEEDS_INFO = "needs_more_info"


@dataclass
class ReuseAttempt:
    """Record of an attempt to reuse existing code"""
    file_path: Path
    match_score: float
    reason_not_suitable: str
    modification_effort: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class FileJustification:
    """Complete justification for creating a new file"""
    file_path: Path
    purpose: str
    functionality: str
    why_new_file_needed: str
    reuse_attempts: List[ReuseAttempt] = field(default_factory=list)
    alternatives_considered: List[str] = field(default_factory=list)
    compliance_check_passed: bool = False
    status: JustificationStatus = JustificationStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    approved_at: Optional[str] = None
    approved_by: Optional[str] = None
    rejection_reason: Optional[str] = None
    task_id: Optional[str] = None
    author: str = "ai_agent"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        data = asdict(self)
        data['file_path'] = str(self.file_path)
        data['status'] = self.status.value
        data['reuse_attempts'] = [
            {
                'file_path': str(attempt.file_path),
                'match_score': attempt.match_score,
                'reason_not_suitable': attempt.reason_not_suitable,
                'modification_effort': attempt.modification_effort,
                'timestamp': attempt.timestamp
            }
            for attempt in self.reuse_attempts
        ]
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FileJustification':
        """Create from dictionary"""
        data['file_path'] = Path(data['file_path'])
        data['status'] = JustificationStatus(data['status'])
        data['reuse_attempts'] = [
            ReuseAttempt(
                file_path=Path(attempt['file_path']),
                match_score=attempt['match_score'],
                reason_not_suitable=attempt['reason_not_suitable'],
                modification_effort=attempt['modification_effort'],
                timestamp=attempt['timestamp']
            )
            for attempt in data.get('reuse_attempts', [])
        ]
        return cls(**data)


class JustificationSystem:
    """System for managing and validating file creation justifications"""
    
    def __init__(self, claude_path: Path = None):
        """Initialize justification system"""
        if claude_path is None:
            # Find .claude directory
            current = Path.cwd()
            while not (current / ".claude").exists() and current != current.parent:
                current = current.parent
            self.claude_path = current / ".claude"
        else:
            self.claude_path = claude_path
            
        self.project_root = self.claude_path.parent
        
        # Justification storage
        self.justifications_dir = self.claude_path / "logic" / "code_reuse" / "justifications"
        self.justifications_dir.mkdir(parents=True, exist_ok=True)
        
        # Audit log
        self.audit_log_path = self.justifications_dir / "audit_log.json"
        self._ensure_audit_log()
        
    def _ensure_audit_log(self):
        """Ensure audit log exists"""
        if not self.audit_log_path.exists():
            with open(self.audit_log_path, 'w') as f:
                json.dump({"entries": []}, f, indent=2)
    
    def create_justification(
        self,
        file_path: Path,
        purpose: str,
        functionality: str,
        why_needed: str,
        reuse_analysis: Optional[Dict[str, Any]] = None,
        task_id: Optional[str] = None
    ) -> FileJustification:
        """
        Create a new file justification
        
        Args:
            file_path: Path where new file will be created
            purpose: High-level purpose of the file
            functionality: Specific functionality it provides
            why_needed: Detailed explanation of why new file is needed
            reuse_analysis: Results from reuse analyzer
            task_id: Associated task ID
            
        Returns:
            FileJustification object
        """
        justification = FileJustification(
            file_path=file_path,
            purpose=purpose,
            functionality=functionality,
            why_new_file_needed=why_needed,
            task_id=task_id
        )
        
        # Add reuse attempts from analysis
        if reuse_analysis and 'matches' in reuse_analysis:
            for match in reuse_analysis['matches'][:5]:  # Top 5 matches
                attempt = ReuseAttempt(
                    file_path=Path(match['file_path']),
                    match_score=match['score'],
                    reason_not_suitable=self._generate_unsuitability_reason(match),
                    modification_effort=match.get('modification_effort', 0)
                )
                justification.reuse_attempts.append(attempt)
                
        # Save justification
        self._save_justification(justification)
        
        # Add to audit log
        self._add_audit_entry("created", justification)
        
        return justification
    
    def validate_justification(
        self,
        justification: FileJustification,
        compliance_result: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, str]:
        """
        Validate if justification is sufficient
        
        Args:
            justification: The justification to validate
            compliance_result: Results from compliance validator
            
        Returns:
            Tuple of (is_valid, reason)
        """
        reasons = []
        
        # Check basic requirements
        if not justification.purpose or len(justification.purpose) < 20:
            reasons.append("Purpose description too brief")
            
        if not justification.functionality or len(justification.functionality) < 30:
            reasons.append("Functionality description insufficient")
            
        if not justification.why_new_file_needed or len(justification.why_new_file_needed) < 50:
            reasons.append("Explanation for new file too brief")
            
        # Check reuse analysis
        if not justification.reuse_attempts:
            reasons.append("No reuse analysis performed")
        else:
            # Check if any high-scoring matches were rejected
            high_scores = [a for a in justification.reuse_attempts if a.match_score > 70]
            if high_scores:
                reasons.append(f"High-scoring match ({high_scores[0].match_score}%) not adequately justified")
                
        # Check alternatives
        if not justification.alternatives_considered:
            reasons.append("No alternatives documented")
            
        # Check compliance
        if compliance_result and not compliance_result.get('is_compliant', False):
            reasons.append("Failed compliance validation")
            justification.compliance_check_passed = False
        else:
            justification.compliance_check_passed = True
            
        is_valid = len(reasons) == 0
        reason = " | ".join(reasons) if reasons else "All checks passed"
        
        return is_valid, reason
    
    def approve_justification(
        self,
        justification: FileJustification,
        approved_by: str = "system"
    ) -> FileJustification:
        """Approve a justification"""
        justification.status = JustificationStatus.APPROVED
        justification.approved_at = datetime.now().isoformat()
        justification.approved_by = approved_by
        
        self._save_justification(justification)
        self._add_audit_entry("approved", justification)
        
        return justification
    
    def reject_justification(
        self,
        justification: FileJustification,
        reason: str
    ) -> FileJustification:
        """Reject a justification"""
        justification.status = JustificationStatus.REJECTED
        justification.rejection_reason = reason
        
        self._save_justification(justification)
        self._add_audit_entry("rejected", justification, {"reason": reason})
        
        return justification
    
    def require_more_info(
        self,
        justification: FileJustification,
        what_needed: str
    ) -> FileJustification:
        """Mark justification as needing more information"""
        justification.status = JustificationStatus.NEEDS_INFO
        justification.rejection_reason = f"More info needed: {what_needed}"
        
        self._save_justification(justification)
        self._add_audit_entry("needs_info", justification, {"info_needed": what_needed})
        
        return justification
    
    def get_justification(self, file_path: Path) -> Optional[FileJustification]:
        """Get justification for a file path"""
        justification_file = self._get_justification_path(file_path)
        
        if justification_file.exists():
            with open(justification_file, 'r') as f:
                data = json.load(f)
                return FileJustification.from_dict(data)
                
        return None
    
    def get_pending_justifications(self) -> List[FileJustification]:
        """Get all pending justifications"""
        pending = []
        
        for file_path in self.justifications_dir.glob("*.json"):
            if file_path.name == "audit_log.json":
                continue
                
            with open(file_path, 'r') as f:
                data = json.load(f)
                justification = FileJustification.from_dict(data)
                
                if justification.status == JustificationStatus.PENDING:
                    pending.append(justification)
                    
        return pending
    
    def get_audit_trail(self, file_path: Optional[Path] = None) -> List[Dict[str, Any]]:
        """
        Get audit trail for file creations
        
        Args:
            file_path: Optional specific file to filter by
            
        Returns:
            List of audit entries
        """
        with open(self.audit_log_path, 'r') as f:
            data = json.load(f)
            
        entries = data.get('entries', [])
        
        if file_path:
            file_str = str(file_path)
            entries = [e for e in entries if e.get('file_path') == file_str]
            
        return entries
    
    def generate_justification_report(self) -> Dict[str, Any]:
        """Generate report on file creation justifications"""
        report = {
            'total_justifications': 0,
            'approved': 0,
            'rejected': 0,
            'pending': 0,
            'needs_info': 0,
            'by_month': {},
            'common_rejection_reasons': {},
            'reuse_success_rate': 0,
            'timestamp': datetime.now().isoformat()
        }
        
        all_justifications = []
        
        # Load all justifications
        for file_path in self.justifications_dir.glob("*.json"):
            if file_path.name == "audit_log.json":
                continue
                
            with open(file_path, 'r') as f:
                data = json.load(f)
                justification = FileJustification.from_dict(data)
                all_justifications.append(justification)
                
        # Calculate statistics
        report['total_justifications'] = len(all_justifications)
        
        for just in all_justifications:
            # Status counts
            if just.status == JustificationStatus.APPROVED:
                report['approved'] += 1
            elif just.status == JustificationStatus.REJECTED:
                report['rejected'] += 1
                # Track rejection reasons
                reason = just.rejection_reason or "Unknown"
                report['common_rejection_reasons'][reason] = \
                    report['common_rejection_reasons'].get(reason, 0) + 1
            elif just.status == JustificationStatus.PENDING:
                report['pending'] += 1
            elif just.status == JustificationStatus.NEEDS_INFO:
                report['needs_info'] += 1
                
            # By month
            month = just.created_at[:7]  # YYYY-MM
            if month not in report['by_month']:
                report['by_month'][month] = {
                    'total': 0,
                    'approved': 0,
                    'rejected': 0
                }
            report['by_month'][month]['total'] += 1
            if just.status == JustificationStatus.APPROVED:
                report['by_month'][month]['approved'] += 1
            elif just.status == JustificationStatus.REJECTED:
                report['by_month'][month]['rejected'] += 1
                
        # Calculate reuse success rate
        if report['total_justifications'] > 0:
            report['reuse_success_rate'] = \
                (report['rejected'] / report['total_justifications']) * 100
                
        return report
    
    def _generate_unsuitability_reason(self, match: Dict[str, Any]) -> str:
        """Generate reason why a match is not suitable"""
        score = match.get('score', 0)
        effort = match.get('modification_effort', 0)
        
        if score < 40:
            return "Too different from requirements"
        elif score < 60:
            return "Would require substantial modifications"
        elif effort > 70:
            return "Modification effort too high"
        else:
            return "Interface incompatibility or architectural mismatch"
    
    def _get_justification_path(self, file_path: Path) -> Path:
        """Get path for justification file"""
        # Create unique filename based on file path
        safe_name = str(file_path).replace('/', '_').replace('\\', '_')
        return self.justifications_dir / f"{safe_name}.json"
    
    def _save_justification(self, justification: FileJustification):
        """Save justification to disk"""
        file_path = self._get_justification_path(justification.file_path)
        
        with open(file_path, 'w') as f:
            json.dump(justification.to_dict(), f, indent=2)
    
    def _add_audit_entry(
        self,
        action: str,
        justification: FileJustification,
        extra_data: Optional[Dict[str, Any]] = None
    ):
        """Add entry to audit log"""
        with open(self.audit_log_path, 'r') as f:
            data = json.load(f)
            
        entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'file_path': str(justification.file_path),
            'status': justification.status.value,
            'author': justification.author,
            'task_id': justification.task_id
        }
        
        if extra_data:
            entry.update(extra_data)
            
        data['entries'].append(entry)
        
        with open(self.audit_log_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def enforce_justification(
        self,
        file_path: Path,
        code_content: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Enforce justification requirement before file creation
        
        Args:
            file_path: Path where file will be created
            code_content: Optional code content to validate
            
        Returns:
            Tuple of (allowed, message)
        """
        # Check if justification exists
        justification = self.get_justification(file_path)
        
        if not justification:
            return False, "No justification found. Run reuse analysis and create justification first."
            
        if justification.status == JustificationStatus.REJECTED:
            return False, f"Justification rejected: {justification.rejection_reason}"
            
        if justification.status == JustificationStatus.NEEDS_INFO:
            return False, f"Justification incomplete: {justification.rejection_reason}"
            
        if justification.status == JustificationStatus.PENDING:
            # Auto-validate
            is_valid, reason = self.validate_justification(justification)
            
            if is_valid:
                self.approve_justification(justification, "auto-validation")
                return True, "Justification approved automatically"
            else:
                self.reject_justification(justification, reason)
                return False, f"Justification invalid: {reason}"
                
        if justification.status == JustificationStatus.APPROVED:
            return True, f"File creation approved on {justification.approved_at}"
            
        return False, "Unknown justification status"