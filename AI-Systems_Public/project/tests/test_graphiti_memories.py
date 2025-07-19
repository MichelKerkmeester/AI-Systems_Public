#!/usr/bin/env python3
"""
Test script for Graphiti memory system verification
"""

import asyncio
import json
import sys
import os
from datetime import datetime
from typing import List, Dict, Any

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mcp'))

from graphiti_mcp import (
    initialize_graphiti, 
    add_episode, 
    search, 
    retrieve_episodes,
    EpisodeData,
    SearchQuery
)

class GraphitiMemoryTester:
    def __init__(self):
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'tests': [],
            'summary': {}
        }
    
    async def test_retrieve_all_memories(self):
        """Retrieve and display all recent memories"""
        print("\n🔍 Retrieving all recent memories...")
        
        try:
            result = await retrieve_episodes(last_n=20)
            
            if result.status == 'success':
                episodes = result.data['episodes']
                print(f"✅ Found {len(episodes)} memories\n")
                
                # Group by source/category
                by_group = {}
                for ep in episodes:
                    group = ep.get('group_id', 'ungrouped')
                    if group not in by_group:
                        by_group[group] = []
                    by_group[group].append(ep)
                
                # Display formatted
                for group, eps in by_group.items():
                    print(f"\n📁 Group: {group or 'default'}")
                    print("-" * 50)
                    for ep in eps:
                        print(f"  • {ep['name']}")
                        print(f"    Created: {ep['created_at']}")
                        print(f"    Source: {ep.get('source', 'unknown')}")
                
                self.results['tests'].append({
                    'name': 'retrieve_all',
                    'status': 'passed',
                    'count': len(episodes),
                    'groups': list(by_group.keys())
                })
            else:
                print(f"❌ Error: {result.error}")
                self.results['tests'].append({
                    'name': 'retrieve_all',
                    'status': 'failed',
                    'error': result.error
                })
                
        except Exception as e:
            print(f"❌ Exception: {str(e)}")
            self.results['tests'].append({
                'name': 'retrieve_all',
                'status': 'error',
                'error': str(e)
            })
    
    async def test_search_queries(self):
        """Test various search queries"""
        print("\n🔍 Testing search functionality...")
        
        test_queries = [
            ("security", "Security-related memories"),
            ("pattern", "Code patterns"),
            ("bug fix", "Bug fixes"),
            ("optimization performance", "Performance improvements"),
            ("Webflow", "Webflow-specific items"),
            ("API", "API-related content")
        ]
        
        search_results = []
        
        for query, description in test_queries:
            print(f"\n  Searching for: '{query}' ({description})")
            try:
                result = await search(SearchQuery(query=query, limit=5))
                
                if result.status == 'success':
                    count = result.data['count']
                    print(f"    ✅ Found {count} results")
                    search_results.append({
                        'query': query,
                        'description': description,
                        'count': count,
                        'status': 'success'
                    })
                else:
                    print(f"    ❌ Error: {result.error}")
                    search_results.append({
                        'query': query,
                        'description': description,
                        'status': 'failed',
                        'error': result.error
                    })
                    
            except Exception as e:
                print(f"    ❌ Exception: {str(e)}")
                search_results.append({
                    'query': query,
                    'description': description,
                    'status': 'error',
                    'error': str(e)
                })
        
        self.results['tests'].append({
            'name': 'search_queries',
            'status': 'completed',
            'queries_tested': len(test_queries),
            'results': search_results
        })
    
    async def test_memory_categories(self):
        """Verify all memory categories are stored"""
        print("\n📊 Verifying memory categories...")
        
        expected_categories = {
            'architecture_decision': 'DECISION:',
            'security_update': 'SECURITY:',
            'code_pattern': 'PATTERN:',
            'bug_fix': 'RESOLVED:',
            'performance': 'OPTIMIZATION:',
            'manual_preference': 'Manual:'
        }
        
        # Retrieve recent episodes
        result = await retrieve_episodes(last_n=30)
        
        if result.status == 'success':
            episodes = result.data['episodes']
            found_categories = {}
            
            # Check which categories we found
            for ep in episodes:
                name = ep['name']
                for cat, prefix in expected_categories.items():
                    if name.startswith(prefix):
                        found_categories[cat] = ep
            
            print(f"\n  Expected categories: {len(expected_categories)}")
            print(f"  Found categories: {len(found_categories)}")
            
            for cat, prefix in expected_categories.items():
                if cat in found_categories:
                    print(f"    ✅ {cat}: {found_categories[cat]['name'][:50]}...")
                else:
                    print(f"    ❌ {cat}: Not found")
            
            self.results['tests'].append({
                'name': 'category_verification',
                'status': 'passed' if len(found_categories) == len(expected_categories) else 'partial',
                'expected': len(expected_categories),
                'found': len(found_categories),
                'missing': [c for c in expected_categories if c not in found_categories]
            })
        else:
            print(f"❌ Error retrieving episodes: {result.error}")
            self.results['tests'].append({
                'name': 'category_verification',
                'status': 'failed',
                'error': result.error
            })
    
    async def test_group_filtering(self):
        """Test filtering by group IDs"""
        print("\n🏷️  Testing group filtering...")
        
        test_groups = [
            'anobel-architecture',
            'security-measures',
            'webflow-patterns',
            'bug-fixes',
            'performance-improvements',
            'client-requirements'
        ]
        
        for group_id in test_groups:
            print(f"\n  Filtering by group: {group_id}")
            try:
                result = await retrieve_episodes(last_n=10, group_ids=[group_id])
                
                if result.status == 'success':
                    count = result.data['count']
                    print(f"    ✅ Found {count} memories in group")
                else:
                    print(f"    ❌ Error: {result.error}")
                    
            except Exception as e:
                print(f"    ❌ Exception: {str(e)}")
        
        self.results['tests'].append({
            'name': 'group_filtering',
            'status': 'completed',
            'groups_tested': len(test_groups)
        })
    
    def save_results(self):
        """Save test results to file"""
        output_path = os.path.join(
            os.path.dirname(__file__), 
            'graphiti-test-results.md'
        )
        
        # Calculate summary
        total_tests = len(self.results['tests'])
        passed = sum(1 for t in self.results['tests'] if t.get('status') in ['passed', 'success', 'completed'])
        failed = sum(1 for t in self.results['tests'] if t.get('status') in ['failed', 'error'])
        
        self.results['summary'] = {
            'total_tests': total_tests,
            'passed': passed,
            'failed': failed,
            'success_rate': f"{(passed/total_tests)*100:.1f}%" if total_tests > 0 else "0%"
        }
        
        # Generate markdown report
        report = f"""# Graphiti Memory Test Results
*Generated: {self.results['timestamp']}*

## Summary
- **Total Tests**: {total_tests}
- **Passed**: {passed}
- **Failed**: {failed}
- **Success Rate**: {self.results['summary']['success_rate']}

## Test Details

"""
        
        for test in self.results['tests']:
            report += f"### {test['name'].replace('_', ' ').title()}\n"
            report += f"**Status**: {test['status']}\n\n"
            
            # Add test-specific details
            if test['name'] == 'retrieve_all':
                if 'count' in test:
                    report += f"- Retrieved {test['count']} memories\n"
                    report += f"- Groups found: {', '.join(test['groups'])}\n"
            
            elif test['name'] == 'search_queries':
                report += "| Query | Description | Results | Status |\n"
                report += "|-------|-------------|---------|--------|\n"
                for r in test.get('results', []):
                    count = r.get('count', 'N/A')
                    status = '✅' if r['status'] == 'success' else '❌'
                    report += f"| {r['query']} | {r['description']} | {count} | {status} |\n"
            
            elif test['name'] == 'category_verification':
                if 'expected' in test:
                    report += f"- Expected categories: {test['expected']}\n"
                    report += f"- Found categories: {test['found']}\n"
                    if test.get('missing'):
                        report += f"- Missing: {', '.join(test['missing'])}\n"
            
            report += "\n"
        
        # Add raw JSON results
        report += "## Raw Test Data\n"
        report += "```json\n"
        report += json.dumps(self.results, indent=2)
        report += "\n```\n"
        
        # Save report
        with open(output_path, 'w') as f:
            f.write(report)
        
        print(f"\n📄 Test results saved to: {output_path}")
        print(f"   Summary: {self.results['summary']['success_rate']} success rate")
    
    async def run_all_tests(self):
        """Run all tests in sequence"""
        print("=" * 60)
        print("🧪 Graphiti Memory System Test Suite")
        print("=" * 60)
        
        # Initialize Graphiti first
        print("\n⚙️  Initializing Graphiti connection...")
        try:
            await initialize_graphiti()
            print("✅ Graphiti initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize Graphiti: {e}")
            return
        
        # Run tests
        await self.test_retrieve_all_memories()
        await self.test_search_queries()
        await self.test_memory_categories()
        await self.test_group_filtering()
        
        # Save results
        self.save_results()
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)


async def main():
    """Main entry point"""
    tester = GraphitiMemoryTester()
    await tester.run_all_tests()


if __name__ == "__main__":
    # Check for required environment variables
    required_vars = ['GOOGLE_API_KEY', 'NEO4J_URI', 'NEO4J_USER', 'NEO4J_PASSWORD']
    missing = [v for v in required_vars if not os.getenv(v)]
    
    if missing:
        print(f"❌ Missing required environment variables: {', '.join(missing)}")
        print("   Please ensure your .env file is configured properly")
        sys.exit(1)
    
    # Run tests
    asyncio.run(main())