#!/usr/bin/env python3
"""
Deploy Optimized Memory Filter
Automated deployment script with safety checks and rollback capability
"""

import os
import sys
import shutil
import time
import json
from datetime import datetime
from pathlib import Path
import argparse

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

class MemoryFilterDeployment:
    """Handles deployment of optimized memory filter"""
    
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.deployment_log = []
        self.start_time = datetime.now()
        self.memory_dir = Path(__file__).parent.parent / "memory"
        self.current_filter = self.memory_dir / "crawl4ai-memory-filter.py"
        self.optimized_filter = self.memory_dir / "crawl4ai-memory-filter-optimized.py"
        self.backup_path = None
        
    def log(self, message, level="INFO"):
        """Log deployment actions"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        self.deployment_log.append(log_entry)
    
    def pre_deployment_checks(self):
        """Run pre-deployment validation"""
        self.log("Running pre-deployment checks...")
        
        checks_passed = True
        
        # Check 1: Verify optimized filter exists
        if not self.optimized_filter.exists():
            self.log(f"❌ Optimized filter not found at {self.optimized_filter}", "ERROR")
            checks_passed = False
        else:
            self.log("✅ Optimized filter found")
        
        # Check 2: Verify current filter exists
        if not self.current_filter.exists():
            self.log(f"❌ Current filter not found at {self.current_filter}", "ERROR")
            checks_passed = False
        else:
            self.log("✅ Current filter found")
        
        # Check 3: Verify optimized filter has correct threshold
        if self.optimized_filter.exists():
            with open(self.optimized_filter, 'r') as f:
                content = f.read()
            
            if "'neo4j': 0.8" in content or "'neo4j': 0.8," in content:
                self.log("✅ Neo4j threshold verified (0.8)")
            else:
                self.log("❌ Neo4j threshold not 0.8 in optimized filter", "ERROR")
                checks_passed = False
        
        # Check 4: Check if already deployed
        if self.current_filter.exists():
            with open(self.current_filter, 'r') as f:
                content = f.read()
            
            if "OptimizedCrawl4AIMemoryFilter" in content:
                self.log("⚠️  Optimized filter may already be deployed", "WARNING")
        
        # Check 5: Disk space
        import shutil
        stat = shutil.disk_usage(self.memory_dir)
        free_mb = stat.free / (1024 * 1024)
        if free_mb < 100:
            self.log(f"⚠️  Low disk space: {free_mb:.1f}MB free", "WARNING")
        else:
            self.log(f"✅ Sufficient disk space ({free_mb:.0f}MB free)")
        
        return checks_passed
    
    def create_backup(self):
        """Create backup of current filter"""
        self.log("Creating backup of current filter...")
        
        if self.dry_run:
            self.log("  [DRY RUN] Would create backup")
            return True
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            self.backup_path = self.memory_dir / f"crawl4ai-memory-filter.backup-{timestamp}.py"
            
            shutil.copy2(self.current_filter, self.backup_path)
            self.log(f"✅ Backup created: {self.backup_path.name}")
            
            # Verify backup
            if self.backup_path.exists() and self.backup_path.stat().st_size == self.current_filter.stat().st_size:
                self.log("✅ Backup verified")
                return True
            else:
                self.log("❌ Backup verification failed", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"❌ Backup failed: {e}", "ERROR")
            return False
    
    def deploy_filter(self):
        """Deploy the optimized filter"""
        self.log("Deploying optimized memory filter...")
        
        if self.dry_run:
            self.log("  [DRY RUN] Would copy optimized filter to production")
            return True
        
        try:
            # Copy optimized filter to production location
            shutil.copy2(self.optimized_filter, self.current_filter)
            self.log("✅ Optimized filter copied to production")
            
            # Verify deployment
            with open(self.current_filter, 'r') as f:
                content = f.read()
            
            if "OptimizedCrawl4AIMemoryFilter" in content and "'neo4j': 0.8" in content:
                self.log("✅ Deployment verified - optimized filter active with 0.8 threshold")
                return True
            else:
                self.log("❌ Deployment verification failed", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"❌ Deployment failed: {e}", "ERROR")
            return False
    
    def test_deployment(self):
        """Run basic tests on deployed filter"""
        self.log("Testing deployed filter...")
        
        if self.dry_run:
            self.log("  [DRY RUN] Would run deployment tests")
            return True
        
        try:
            # Import and instantiate the filter
            sys.path.insert(0, str(self.memory_dir))
            from importlib import import_module, reload
            
            # Force reload to get new version
            if 'crawl4ai-memory-filter' in sys.modules:
                del sys.modules['crawl4ai-memory-filter']
            
            # Import using alternative method due to hyphen
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "crawl4ai_memory_filter",
                str(self.current_filter)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Test instantiation
            if hasattr(module, 'OptimizedCrawl4AIMemoryFilter'):
                filter_instance = module.OptimizedCrawl4AIMemoryFilter()
                self.log("✅ Filter instantiation successful")
                
                # Test basic functionality
                test_content = {
                    'url': 'https://test.example.com/api/endpoint',
                    'title': 'Test Content',
                    'text': 'This is a test of the memory filter deployment'
                }
                
                result = filter_instance.process_crawled_content(test_content)
                if result and 'status' in result:
                    self.log("✅ Basic functionality test passed")
                    return True
                else:
                    self.log("❌ Basic functionality test failed", "ERROR")
                    return False
            else:
                self.log("❌ OptimizedCrawl4AIMemoryFilter class not found", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"❌ Testing failed: {e}", "ERROR")
            return False
    
    def rollback(self):
        """Rollback to previous version"""
        self.log("Rolling back deployment...", "WARNING")
        
        if self.dry_run:
            self.log("  [DRY RUN] Would rollback to backup")
            return True
        
        if not self.backup_path or not self.backup_path.exists():
            self.log("❌ No backup available for rollback", "ERROR")
            return False
        
        try:
            shutil.copy2(self.backup_path, self.current_filter)
            self.log("✅ Rollback completed")
            
            # Verify rollback
            with open(self.current_filter, 'r') as f:
                content = f.read()
            
            if "OptimizedCrawl4AIMemoryFilter" not in content:
                self.log("✅ Rollback verified - original filter restored")
                return True
            else:
                self.log("❌ Rollback verification failed", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"❌ Rollback failed: {e}", "ERROR")
            return False
    
    def save_deployment_log(self):
        """Save deployment log to file"""
        log_data = {
            "deployment_id": self.start_time.strftime("%Y%m%d-%H%M%S"),
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "dry_run": self.dry_run,
            "success": all("[ERROR]" not in log for log in self.deployment_log),
            "backup_path": str(self.backup_path) if self.backup_path else None,
            "log": self.deployment_log
        }
        
        log_file = f"deployment-log-{log_data['deployment_id']}.json"
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        self.log(f"Deployment log saved to: {log_file}")
    
    def deploy(self):
        """Main deployment process"""
        print("=" * 60)
        print("MEMORY FILTER DEPLOYMENT".center(60))
        print("=" * 60)
        
        if self.dry_run:
            print("DRY RUN MODE - No changes will be made".center(60))
            print("=" * 60)
        
        # Step 1: Pre-deployment checks
        if not self.pre_deployment_checks():
            self.log("Pre-deployment checks failed. Aborting.", "ERROR")
            self.save_deployment_log()
            return False
        
        # Step 2: Create backup
        if not self.create_backup():
            self.log("Backup creation failed. Aborting.", "ERROR")
            self.save_deployment_log()
            return False
        
        # Step 3: Deploy filter
        if not self.deploy_filter():
            self.log("Deployment failed. Attempting rollback...", "ERROR")
            self.rollback()
            self.save_deployment_log()
            return False
        
        # Step 4: Test deployment
        if not self.test_deployment():
            self.log("Deployment tests failed. Attempting rollback...", "ERROR")
            self.rollback()
            self.save_deployment_log()
            return False
        
        # Success!
        self.log("=" * 60)
        self.log("🎉 DEPLOYMENT SUCCESSFUL! 🎉")
        self.log("=" * 60)
        self.log("Optimized memory filter is now active with:")
        self.log("  - Neo4j threshold: 0.8 (reduced from 0.6)")
        self.log("  - Expected Neo4j reduction: 80%")
        self.log("  - Performance improvement: 3-4x")
        self.log("")
        self.log("Next steps:")
        self.log("  1. Monitor queue depth and processing times")
        self.log("  2. Check circuit breaker status")
        self.log("  3. Verify cost reduction in 24 hours")
        
        self.save_deployment_log()
        return True

def main():
    parser = argparse.ArgumentParser(description="Deploy optimized memory filter")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run deployment simulation without making changes")
    parser.add_argument("--force", action="store_true",
                        help="Skip confirmation prompt")
    
    args = parser.parse_args()
    
    if not args.force and not args.dry_run:
        print("\n⚠️  WARNING: This will deploy the optimized memory filter to production!")
        print("The following changes will be made:")
        print("  - Neo4j threshold will increase from 0.6 to 0.8")
        print("  - Memory filter will use batch processing")
        print("  - Circuit breaker will be activated")
        print("\nA backup will be created before deployment.")
        
        response = input("\nDo you want to continue? (yes/no): ")
        if response.lower() != "yes":
            print("Deployment cancelled.")
            return
    
    # Run deployment
    deployment = MemoryFilterDeployment(dry_run=args.dry_run)
    success = deployment.deploy()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()