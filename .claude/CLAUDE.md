# Local Claude Configuration

This file contains session-specific and environment-specific configuration for Claude Code in this repository.

## Hugo Server Status

**Running the Hugo Server:**
```bash
hugo server --buildDrafts --buildFuture --bind 0.0.0.0 --port 1313
```

**Check if Hugo server is running:**
```bash
ps aux | grep hugo
```

**Expected output:** Should show a process running hugo server on port 1313

**If not running, restart with:**
```bash
hugo server --buildDrafts --buildFuture --bind 0.0.0.0 --port 1313
```
(Remember to use `run_in_background: true` parameter in Bash tool)

## MCP Playwright Installation & Verification

**Installation Status**: Should be installed at user level (available in all projects)

**Server Configuration:**
- **Server Name**: playwright
- **Command**: `npx @playwright/mcp@latest`
- **Scope**: User

**Verification Commands:**
```bash
claude mcp list
claude mcp get playwright
npx @playwright/mcp@latest --help
```

### MCP Tools Availability Check

**IMPORTANT**: The Playwright MCP tools should be available as `mcp__playwright__browser_*` functions in your tool list.

**Expected Playwright Tools:**
- `mcp__playwright__browser_navigate` - Navigate to URLs
- `mcp__playwright__browser_take_screenshot` - Capture screenshots
- `mcp__playwright__browser_snapshot` - Get accessibility tree
- `mcp__playwright__browser_click` - Click elements
- `mcp__playwright__browser_type` - Type text
- `mcp__playwright__browser_resize` - Resize browser window
- `mcp__playwright__browser_console_messages` - Get console output
- `mcp__playwright__browser_network_requests` - View network activity
- And many more browser automation tools

**If MCP tools are NOT available:**
1. Check if session was restarted after MCP installation
2. Verify with: `claude mcp list` (should show playwright)
3. If needed, reinstall:
   ```bash
   claude mcp remove playwright -s user
   claude mcp add playwright "npx @playwright/mcp@latest" -s user
   ```

### Site Testing with Playwright

Once Playwright tools are confirmed available, perform comprehensive site analysis:

**1. Initial Screenshot:**
```
mcp__playwright__browser_navigate to http://localhost:1313
mcp__playwright__browser_take_screenshot
```

**2. Accessibility Check:**
```
mcp__playwright__browser_snapshot for accessibility tree
```

**3. Responsive Testing:**
- Desktop: `mcp__playwright__browser_resize` to 1920x1080
- Tablet: `mcp__playwright__browser_resize` to 768x1024
- Mobile: `mcp__playwright__browser_resize` to 375x667

**4. Theme Testing:**
Test both light and dark modes if theme switcher is available

**5. Page Navigation:**
Test all CTAs and internal links work correctly

**6. Console Check:**
```
mcp__playwright__browser_console_messages to check for errors
```

**7. Network Analysis:**
```
mcp__playwright__browser_network_requests to review API calls and resource loading
```

## Browser Installation

If you get an error about the browser not being installed:
```
mcp__playwright__browser_install
```

## Survey Page Testing Checklist

When testing the SARA survey pages:
- [ ] Hero section displays correctly with background image/color
- [ ] Key insights section is readable and well-formatted
- [ ] Downloadable report links work (Google Doc, PDF, SSRN)
- [ ] Technical report HTML page loads with all styles
- [ ] Figures display at correct size and position
- [ ] Contact section shows team information correctly
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Dark mode (if enabled) displays properly
- [ ] No console errors or broken resources
