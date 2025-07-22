# Superdesign Canvas Integration Design

## Architecture Overview

### Component Hierarchy
```
viteflow/
├── components/
│   ├── canvasViewer.js         # Main canvas component (extends exampleComponent pattern)
│   ├── canvasFrame.js          # Individual design frame (reuses stateCard patterns)
│   ├── canvasControls.js       # Control panel (extends stateModal drawer)
│   └── canvasGrid.js           # Layout manager (new, but uses existing utils)
├── pages/
│   └── canvas.js               # Canvas page route
└── utils/
    └── designWatcher.js        # File system watcher utility
```

## Implementation Details

### 1. Canvas Viewer Component
**Extends**: `exampleComponent.js` pattern
**Reuses**: Query utilities, initialization flow

```javascript
// viteflow/components/canvasViewer.js
import { queryElement, addClass, createElement } from "../utils/index.js";
import gsap from "gsap";

export const canvasViewer = () => {
  const canvas = queryElement("[data-component='canvas-viewer']");
  if (!canvas) return;
  
  // Reuse initialization pattern from exampleComponent
  addClass(canvas, "is-initialized");
  
  // Canvas-specific setup
  initializeCanvas(canvas);
  setupFileWatcher(canvas);
};
```

### 2. Canvas Controls Panel
**Extends**: `stateModal.js` drawer animations
**Reuses**: GSAP timelines, event handling

```javascript
// viteflow/components/canvasControls.js
// Adapts stateModal's drawer pattern for control panel
// Uses same animation timing and easing functions
```

### 3. Design File Watcher
**Integration**: Vite plugin for WebSocket communication
**Location**: `vite.config.js` modification

```javascript
// Add to existing vite.config.js
import { designWatcherPlugin } from './viteflow/plugins/designWatcher';

export default {
  plugins: [
    // existing plugins...
    designWatcherPlugin({
      watchDir: '.claude-designs',
      wsPort: 3001
    })
  ]
}
```

### 4. Canvas Grid Layout
**Reuses**: CSS Grid patterns from existing styles
**New**: Dynamic grid sizing based on frame count

```css
/* Extends existing grid utilities */
[data-canvas-layout="grid"] {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}
```

## Data Flow

### Design Generation → Canvas Display
1. **Claude Code** generates HTML/CSS in `.claude-designs/`
2. **File Watcher** detects changes via Vite plugin
3. **WebSocket** notifies canvas viewer
4. **Canvas** updates display with new designs
5. **GSAP** animates frame additions smoothly

### User Interactions
1. **Pan/Zoom**: Mouse/touch events → Canvas transform
2. **Layout Toggle**: Control button → Grid/Hierarchy switch
3. **Frame Selection**: Click → Highlight & details panel
4. **Export**: Button → Download selected designs

## Code Reuse Mapping

| New Feature | Reuses From | Modification |
|-------------|-------------|--------------|
| Canvas Container | exampleComponent | Add canvas-specific methods |
| Control Panel | stateModal | Adapt drawer for vertical layout |
| Frame Cards | stateCard | Add iframe for design preview |
| Animations | GSAP usage | Keep timing constants |
| File Watching | Vite dev server | Add WebSocket layer |
| Event Handling | Existing patterns | Maintain data-attribute approach |

## Integration Points

### 1. CLI Command
```bash
# New command in Claude Code
claude-code canvas --port 3000
```

### 2. Vite Dev Server Extension
- Add `/canvas` route
- Serve canvas viewer page
- Handle WebSocket connections

### 3. Design Directory Structure
- Compatible with Superdesign's format
- Metadata for frame relationships
- Asset management for shared styles

## Performance Considerations

### Reused Optimizations
1. GSAP's RAF-based animations
2. Event delegation patterns
3. Lazy loading for frames

### New Optimizations
1. Virtual scrolling for many frames
2. Throttled file watching
3. Debounced canvas updates

## Security

### Sandboxing
- Reuse iframe sandboxing from Superdesign
- Content Security Policy for generated designs
- No direct file system access from browser

## Testing Strategy

### Unit Tests
- Extend existing component tests
- Mock file system events
- Test WebSocket communication

### Integration Tests
- Canvas viewer with test designs
- File watcher responsiveness
- Cross-browser compatibility

## Rollback Plan
1. Canvas components are isolated in new files
2. Vite config changes are additive
3. No modifications to existing components
4. Can remove canvas-related files cleanly