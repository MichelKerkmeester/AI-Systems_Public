# Superdesign Canvas Integration Rollback Plan (Revised)

## Overview
This simplified rollback plan covers removing the Windsurf + Claude Code integration, which requires minimal cleanup since we're using existing tools.

## Rollback Triggers
1. Critical bugs in canvas viewer affecting site performance
2. Security vulnerabilities in design rendering
3. Incompatibility with core viteflow components
4. Business decision to remove feature

## Rollback Steps

### Step 1: Remove Canvas Components (5 minutes)
```bash
# Remove new canvas component files
rm -f viteflow/components/canvasViewer.js
rm -f viteflow/components/canvasFrame.js
rm -f viteflow/components/canvasControls.js
rm -f viteflow/components/canvasGrid.js
rm -f viteflow/pages/canvas.js
rm -f viteflow/utils/designWatcher.js
```

### Step 2: Revert Vite Configuration (2 minutes)
```javascript
// Remove from vite.config.js:
// - import { designWatcherPlugin } from './viteflow/plugins/designWatcher';
// - designWatcherPlugin() from plugins array
```

### Step 3: Remove Canvas Routes (2 minutes)
```javascript
// Remove from viteflow/index.js or router config:
// - Canvas page import
// - Canvas route definition
```

### Step 4: Clean Dependencies (3 minutes)
```bash
# If any canvas-specific dependencies were added
npm uninstall react-zoom-pan-pinch
npm prune
```

### Step 5: Clear Design Directory (1 minute)
```bash
# Optional: Remove generated designs
rm -rf .claude-designs/
```

### Step 6: Update Git (2 minutes)
```bash
# Commit rollback
git add -A
git commit -m "Rollback: Remove canvas integration feature"
```

## Verification Steps

### 1. Component Health Check
```bash
# Run existing component tests
npm test -- --testPathPattern=viteflow/components

# Expected: All pass without canvas tests
```

### 2. Build Verification
```bash
# Clean build
npm run build

# Expected: No errors, size returns to baseline
```

### 3. Runtime Verification
```bash
# Start dev server
npm run dev

# Check:
- [ ] Homepage loads
- [ ] stateModal works
- [ ] No console errors
- [ ] All existing features functional
```

## Data Preservation

### Before Rollback
```bash
# Backup generated designs if needed
cp -r .claude-designs/ .claude-designs-backup-$(date +%Y%m%d)/

# Export any user preferences
cp .claude/canvas-settings.json .claude/canvas-settings.backup.json
```

### After Rollback
- Backup remains available
- Can be restored if feature returns
- No data loss for users

## Communication Plan

### Internal Team
1. Notify development team via Slack
2. Update project board status
3. Document rollback reason in decision log

### Users (if deployed)
1. In-app notification of feature removal
2. Migration guide for alternatives
3. Support ticket for affected users

## Risk Mitigation

### Low Risk Items
- New files in separate directories
- No modifications to existing components
- Additive changes to config files

### Medium Risk Items
- Vite config changes (but isolated)
- Potential WebSocket port conflicts
- Browser cache of canvas route

### Mitigation Strategies
1. **Feature Flag**: Add enable/disable toggle before full rollback
2. **Gradual Rollback**: Remove UI first, then backend
3. **A/B Testing**: Keep for subset of users initially

## Recovery Time Objectives

| Component | Rollback Time | Testing Time | Total RTO |
|-----------|---------------|--------------|-----------|
| Files | 5 min | 5 min | 10 min |
| Config | 5 min | 10 min | 15 min |
| Full Feature | 15 min | 15 min | 30 min |

## Post-Rollback Actions

### 1. Documentation Updates
- Remove canvas documentation
- Update README
- Archive design specs

### 2. Monitoring
- Watch error logs for 24 hours
- Monitor performance metrics
- Check user feedback channels

### 3. Lessons Learned
- Document why rollback was needed
- Identify improvement areas
- Update development guidelines

## Emergency Contacts

### Technical Lead
- Review vite.config.js changes
- Verify component isolation

### QA Team
- Run regression test suite
- Verify no side effects

### DevOps
- Monitor server resources
- Check for orphaned processes

## Rollback Validation Checklist

- [ ] All canvas files removed
- [ ] Vite config restored
- [ ] No import errors
- [ ] Build succeeds
- [ ] Tests pass
- [ ] No console errors
- [ ] Performance baseline restored
- [ ] Documentation updated
- [ ] Team notified
- [ ] Backup created

## Alternative Approaches
If rollback is due to implementation issues rather than concept:

1. **Simplify Implementation**: Remove complex features, keep basic viewer
2. **External Tool**: Separate canvas app instead of integration
3. **Different Integration**: Browser extension instead of built-in
4. **Delayed Launch**: Fix issues and re-implement later

## Sign-off
Rollback plan reviewed and approved by:
- [ ] Technical Lead
- [ ] QA Lead
- [ ] Product Owner