# Live Debugging Agent Specification

## Executive Summary
This specification defines a specialized debugging agent powered by Gemini Pro that uses browser automation tools (Puppeteer/Playwright) for real-time website debugging, visual testing, and performance analysis.

## Architecture Overview

### Debug Agent Components
```
┌────────────────────────────────────────────────┐
│           Debug Agent (Gemini Pro)              │
├────────────────┬────────────────┬──────────────┤
│   Puppeteer    │   Playwright   │ Chrome Debug │
│   MCP Server   │   MCP Server   │ MCP Server   │
└────────────────┴────────────────┴──────────────┘
                 │
    ┌────────────┴────────────┬─────────────────┐
    │                         │                 │
┌───▼──────────┐    ┌────────▼──────┐  ┌───────▼─────┐
│Visual Testing│    │ Performance   │  │ Interactive │
│   Module     │    │   Profiler    │  │  Debugger   │
└──────────────┘    └───────────────┘  └─────────────┘
```

### Integration with Existing MCPs
- **Puppeteer MCP**: Basic browser automation
- **Playwright MCP**: Advanced testing with codegen
- **Chrome Debug MCP**: Direct Chrome DevTools access

## Debug Agent Capabilities

### 1. Visual Regression Testing
```python
class VisualDebugger:
    """Visual regression testing and debugging"""
    
    def __init__(self):
        self.playwright_client = PlaywrightMCPClient()
        self.baseline_storage = BaselineStorage()
        
    async def debug_visual_issues(self, url: str, selectors: list) -> dict:
        """Identify and debug visual issues"""
        
        # 1. Capture current state
        await self.playwright_client.navigate(url)
        current_screenshots = {}
        
        for selector in selectors:
            screenshot = await self.playwright_client.screenshot({
                "name": f"debug_{selector}",
                "selector": selector,
                "fullPage": False
            })
            current_screenshots[selector] = screenshot
            
        # 2. Compare with baseline
        visual_diffs = {}
        for selector, screenshot in current_screenshots.items():
            baseline = self.baseline_storage.get(url, selector)
            if baseline:
                diff = self.calculate_visual_diff(baseline, screenshot)
                if diff['percentage'] > 0.1:  # 0.1% threshold
                    visual_diffs[selector] = {
                        'diff_percentage': diff['percentage'],
                        'affected_areas': diff['areas'],
                        'likely_causes': self.analyze_causes(diff)
                    }
                    
        # 3. Generate fix suggestions
        fixes = await self.generate_fixes(visual_diffs)
        
        return {
            'visual_issues': visual_diffs,
            'suggested_fixes': fixes,
            'screenshots': current_screenshots
        }
```

### 2. Interactive Debugging Session
```python
class InteractiveDebugger:
    """Real-time interactive debugging"""
    
    def __init__(self):
        self.chrome_debug = ChromeDebugMCPClient()
        self.console_buffer = []
        
    async def start_debug_session(self, url: str, issue_description: str):
        """Start interactive debugging session"""
        
        # 1. Launch Chrome in debug mode
        await self.chrome_debug.launch_chrome({
            "url": url,
            "disableAutomationControlled": True
        })
        
        # 2. Set up console monitoring
        self.console_buffer = []
        await self.monitor_console()
        
        # 3. Analyze issue context
        issue_analysis = await self.analyze_issue(issue_description)
        
        # 4. Execute debug steps
        debug_results = []
        for step in issue_analysis['debug_steps']:
            result = await self.execute_debug_step(step)
            debug_results.append(result)
            
            # Check if issue resolved
            if await self.is_issue_resolved(issue_description):
                break
                
        return {
            'console_logs': self.console_buffer,
            'debug_steps': debug_results,
            'resolution': await self.get_resolution_summary(),
            'recommended_fix': await self.generate_fix_code()
        }
```

### 3. Performance Profiling
```python
class PerformanceProfiler:
    """Performance analysis and optimization"""
    
    async def profile_performance(self, url: str, actions: list = None):
        """Profile website performance"""
        
        # 1. Start performance recording
        await self.playwright_client.navigate(url, {
            "waitUntil": "networkidle"
        })
        
        # 2. Execute user actions if provided
        if actions:
            for action in actions:
                await self.execute_action(action)
                
        # 3. Collect performance metrics
        metrics = await self.playwright_client.evaluate("""
            () => {
                const perfData = performance.getEntriesByType('navigation')[0];
                const resourceData = performance.getEntriesByType('resource');
                
                return {
                    navigation: {
                        domContentLoaded: perfData.domContentLoadedEventEnd - perfData.domContentLoadedEventStart,
                        loadComplete: perfData.loadEventEnd - perfData.loadEventStart,
                        totalTime: perfData.loadEventEnd - perfData.fetchStart
                    },
                    resources: resourceData.map(r => ({
                        name: r.name,
                        duration: r.duration,
                        size: r.transferSize,
                        type: r.initiatorType
                    }))
                };
            }
        """)
        
        # 4. Analyze bottlenecks
        bottlenecks = self.identify_bottlenecks(metrics)
        
        # 5. Generate optimization suggestions
        optimizations = await self.generate_optimizations(bottlenecks)
        
        return {
            'metrics': metrics,
            'bottlenecks': bottlenecks,
            'optimizations': optimizations,
            'performance_score': self.calculate_score(metrics)
        }
```

### 4. Cross-Browser Testing
```python
class CrossBrowserDebugger:
    """Debug across different browsers"""
    
    async def debug_cross_browser(self, url: str, issue: str):
        """Test and debug across browsers"""
        
        browsers = ['chromium', 'firefox', 'webkit']
        results = {}
        
        for browser in browsers:
            # Test in each browser
            result = await self.test_in_browser(browser, url, issue)
            results[browser] = result
            
        # Compare results
        differences = self.compare_browser_results(results)
        
        # Generate browser-specific fixes
        fixes = await self.generate_browser_fixes(differences)
        
        return {
            'browser_results': results,
            'differences': differences,
            'fixes': fixes,
            'compatibility_score': self.calculate_compatibility(results)
        }
```

## Debugging Workflows

### 1. Automated Issue Detection
```python
class AutomatedDebugWorkflow:
    """Automated debugging workflow"""
    
    async def auto_debug(self, url: str, test_suite: dict = None):
        """Automatically detect and debug issues"""
        
        issues = []
        
        # 1. Visual regression check
        visual_issues = await VisualDebugger().check_visual_regression(url)
        issues.extend(visual_issues)
        
        # 2. Console error detection
        console_errors = await self.detect_console_errors(url)
        issues.extend(console_errors)
        
        # 3. Performance issues
        perf_issues = await PerformanceProfiler().detect_performance_issues(url)
        issues.extend(perf_issues)
        
        # 4. Accessibility issues
        a11y_issues = await self.check_accessibility(url)
        issues.extend(a11y_issues)
        
        # 5. Run custom test suite if provided
        if test_suite:
            custom_issues = await self.run_test_suite(test_suite)
            issues.extend(custom_issues)
            
        # 6. Prioritize and fix issues
        prioritized = self.prioritize_issues(issues)
        fixes = await self.generate_fixes(prioritized)
        
        return {
            'detected_issues': prioritized,
            'suggested_fixes': fixes,
            'auto_fixed': await self.attempt_auto_fix(fixes),
            'manual_required': [f for f in fixes if not f['auto_fixable']]
        }
```

### 2. Guided Debugging Session
```python
class GuidedDebugSession:
    """Interactive guided debugging"""
    
    async def start_guided_session(self, issue_description: str):
        """Start guided debugging session"""
        
        # 1. Understand the issue
        issue_analysis = await self.analyze_issue_description(issue_description)
        
        # 2. Generate debug plan
        debug_plan = await self.create_debug_plan(issue_analysis)
        
        # 3. Execute plan step by step
        for step in debug_plan['steps']:
            # Present step to user
            await self.present_step(step)
            
            # Execute debugging action
            result = await self.execute_step(step)
            
            # Collect feedback
            feedback = await self.get_user_feedback(result)
            
            # Adjust plan if needed
            if feedback['adjust_needed']:
                debug_plan = await self.adjust_plan(debug_plan, feedback)
                
        return {
            'session_summary': await self.summarize_session(),
            'fixes_applied': self.get_applied_fixes(),
            'lessons_learned': await self.extract_patterns()
        }
```

## Integration with Memory System

### 1. Debug Pattern Learning
```python
class DebugPatternLearner:
    """Learn from debugging sessions"""
    
    async def capture_debug_pattern(self, session: dict):
        """Capture successful debug patterns"""
        
        pattern = {
            'issue_type': session['issue_type'],
            'symptoms': session['symptoms'],
            'root_cause': session['root_cause'],
            'fix_applied': session['fix'],
            'browser_specific': session.get('browser_specific', False),
            'success_metrics': session['metrics']
        }
        
        # Store in memory system
        await self.memory_bridge.capture({
            'name': f"Debug Pattern: {pattern['issue_type']}",
            'content': pattern,
            'type': 'debug_pattern',
            'tags': ['debugging', pattern['issue_type']]
        })
```

### 2. Issue Prediction
```python
class IssuePrediction:
    """Predict potential issues based on patterns"""
    
    async def predict_issues(self, code_changes: dict):
        """Predict potential issues from code changes"""
        
        # Query similar patterns
        similar_issues = await self.memory_bridge.search({
            'query': f"Debug patterns for {code_changes['type']}",
            'type': 'debug_pattern'
        })
        
        # Analyze code for potential issues
        predictions = []
        for pattern in similar_issues:
            if self.matches_pattern(code_changes, pattern):
                predictions.append({
                    'issue_type': pattern['issue_type'],
                    'probability': self.calculate_probability(code_changes, pattern),
                    'prevention': pattern['fix_applied']
                })
                
        return predictions
```

## Performance Optimization

### 1. Parallel Browser Testing
```python
async def parallel_browser_test(urls: list, browsers: list):
    """Test multiple URLs across browsers in parallel"""
    
    tasks = []
    for url in urls:
        for browser in browsers:
            task = asyncio.create_task(
                test_browser_url(browser, url)
            )
            tasks.append(task)
            
    results = await asyncio.gather(*tasks)
    return aggregate_results(results)
```

### 2. Smart Screenshot Caching
```python
class ScreenshotCache:
    """Intelligent screenshot caching"""
    
    def should_use_cache(self, url: str, selector: str) -> bool:
        """Determine if cached screenshot is valid"""
        
        # Check last modification time
        last_modified = self.get_last_modified(url)
        cache_time = self.get_cache_time(url, selector)
        
        # Check DOM stability
        dom_stable = self.check_dom_stability(url, selector)
        
        return (
            cache_time > last_modified and
            dom_stable and
            time.time() - cache_time < 3600  # 1 hour
        )
```

## Success Metrics
- Bug detection rate: >95%
- False positive rate: <5%
- Average debug time: <5 minutes
- Auto-fix success rate: >70%
- Cross-browser compatibility: 100%

## Implementation Requirements
1. Configure browser automation MCPs
2. Set up screenshot baseline storage
3. Implement visual diff algorithms
4. Create debug pattern database
5. Build performance profiling tools

## Cost Optimization
- Use Gemini 2.5 Pro for all debugging tasks ($1.25-2.50/$10-15 per 1M tokens)
- Cache browser sessions for reuse
- Batch similar debugging tasks
- Reuse screenshot baselines
- Parallel execution for efficiency