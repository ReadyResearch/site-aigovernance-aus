# Adding the SARA 2025 Survey Results to the Website

This guide explains how to add the SARA 2025 survey results to the website once they are ready for publication.

## Overview

The website is currently configured with a placeholder 2025 survey page at `/content/survey/2025/index.md`. When the survey results are ready, you'll need to:
1. Download the survey report and associated files from the source location
2. Add them to the 2025 survey directory
3. Update the survey index page with actual results
4. Update the homepage CTA to link directly to the survey instead of the email notification
5. Deploy the changes

## Prerequisites

- SARA 2025 report available at: https://noetel.com.au/sara/2025/index.html
- Hugo installed locally (currently using v0.97.3)
- Git access to the repository

## Step-by-Step Instructions

### Step 1: Download the Survey Report Files

The survey report is expected to be in HTML format with supporting files (similar to the 2024 structure). You'll need to download:

1. The main HTML file (e.g., `sara_technical_report_2025.html`)
2. Any associated directories:
   - `sara_technical_report_2025_files/` (if it exists - contains figures, charts, CSS, JS)
   - Any other supporting files

**How to download:**

```bash
# Navigate to the 2025 survey directory
cd content/survey/2025/

# Option 1: Manual download
# Visit https://noetel.com.au/sara/2025/index.html in your browser
# Right-click > Save As > "Webpage, Complete" to get the HTML and assets

# Option 2: Using wget (if available)
wget -r -np -k https://noetel.com.au/sara/2025/index.html

# Option 3: Using curl and download assets separately
curl -o sara_technical_report_2025.html https://noetel.com.au/sara/2025/index.html
# Then manually download the _files directory if it exists
```

### Step 2: Organize the Files

Place the downloaded files in the correct structure:

```
content/survey/2025/
├── index.md                                    # Survey landing page (already exists)
├── sara_technical_report_2025.html            # Main HTML report (new)
├── sara_technical_report_2025_files/          # Supporting files (new)
│   ├── figure-html/                           # Charts and figures
│   │   ├── fig-*.png
│   ├── libs/                                  # JavaScript libraries
│   │   ├── bootstrap/
│   │   ├── quarto-html/
│   │   └── clipboard/
├── styles.css                                 # Optional: custom styling
├── banner.png                                 # Optional: header image
└── readyuqlogotrans.png                       # Optional: logo
```

### Step 3: Update the Survey Index Page

Edit `content/survey/2025/index.md` and replace the placeholder content with actual survey results.

**Current placeholder structure:**

```yaml
---
title: SARA 2025 Survey
date: 2025-01-01
type: page
---

## Survey Assessing Risks from AI - 2025

### Key Insights

Survey results for 2025 will be published here.

*Data collection: [TODO: Add dates]*

*Sample size: [TODO: Add sample size]*

[More placeholder sections...]
```

**Example updated structure (based on 2024 format):**

```yaml
---
title: SARA 2025 Survey
date: 2025-01-01
type: page
---

## Survey Assessing Risks from AI - 2025

### Key Insights

[Insert key findings from the 2025 survey]

*Data collection: [Actual dates]*

*Sample size: [Actual sample size]*

### Reports

- **[View the full technical report](/survey/2025/sara_technical_report_2025.html)** (HTML)
- **[Download summary briefing](#)** (PDF) - if available

### Key Findings

#### 1. Public Awareness of AI Risks

[Add actual findings]

#### 2. Support for AI Governance

[Add actual findings]

#### 3. Priority Actions

[Add actual findings]

### About This Survey

The 2025 Survey Assessing Risks from AI (SARA) is [description].

### Citation

If you use data from this survey, please cite:

> [Citation information for 2025 survey]

DOI: [Insert DOI if available]
```

### Step 4: Update Homepage CTA

Once the survey is published, update the homepage to link directly to the survey instead of the email notification.

Edit `content/_index.md`:

**Find this section:**

```yaml
      cta:
        label: Get notified about 2025 results
        url: 'mailto:m.noetel@uq.edu.au?subject=Notify%20me%20when%20SARA%202025%20is%20released'
        icon_pack: fas
        icon: envelope
```

**Replace with:**

```yaml
      cta:
        label: View 2025 Survey
        url: '/survey/2025/'
        icon_pack: fas
        icon: chart-line
```

### Step 5: Test Locally

Before deploying, test the changes locally:

```bash
# Navigate to the site root
cd /path/to/site-aigovernance-aus

# Start the Hugo development server
hugo server --buildDrafts --buildFuture --bind 0.0.0.0 --port 1313

# Open your browser to http://localhost:1313
```

**Test checklist:**

- [ ] Homepage loads correctly with updated CTA button
- [ ] Clicking "View 2025 Survey" navigates to `/survey/2025/`
- [ ] The 2025 survey page displays with all content
- [ ] The technical report link works and displays the full HTML report
- [ ] All figures, charts, and interactive elements in the report work
- [ ] The "View 2024 Results" button still works
- [ ] Footer displays correctly with all attributions
- [ ] Mobile responsiveness looks good

### Step 6: Commit and Deploy

Once everything is tested and working:

```bash
# Stage all changes
git add .

# Create a commit
git commit -m "Add SARA 2025 survey results

- Added complete 2025 technical report
- Updated survey index page with key findings
- Changed homepage CTA to link to 2025 survey
- Added all supporting assets (figures, styles, scripts)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to remote
git push origin main
```

The site is configured for automatic deployment via Netlify, so changes will be live within a few minutes of pushing to the main branch.

## Troubleshooting

### Report HTML styling issues

If the HTML report doesn't look right:

1. Check that all files in `sara_technical_report_2025_files/` are present
2. Verify relative paths in the HTML match the actual file structure
3. Check browser console for any 404 errors on missing assets

### Links not working

If internal links in the report don't work:

1. Open the HTML file and check if links use absolute or relative paths
2. May need to adjust paths if the report was generated assuming a different directory structure

### Images not displaying

If figures/charts don't show:

1. Verify all PNG files in `sara_technical_report_2025_files/figure-html/` are present
2. Check that paths in the HTML use relative paths (e.g., `sara_technical_report_2025_files/figure-html/fig-1.png`)

### Hugo not detecting changes

If Hugo server doesn't show your updates:

```bash
# Kill any running Hugo processes
pkill -f "hugo server"

# Restart Hugo
hugo server --buildDrafts --buildFuture --bind 0.0.0.0 --port 1313
```

## Additional Notes

### File Naming Consistency

For consistency with the 2024 survey, consider naming the main report file to match the pattern:
- 2024: `sara_technical_report.html`
- 2025: `sara_technical_report_2025.html` (to distinguish from 2024)

Or keep them both as `sara_technical_report.html` in their respective directories.

### Adding a PDF Summary

If you have a PDF summary briefing:

1. Add it to `static/files/2025_Survey_Summary.pdf`
2. Link to it from the survey page: `[Download summary](/files/2025_Survey_Summary.pdf)`

### Updating Future Years

This same process applies for future years (2026, 2027, etc.):

1. Create a new directory: `content/survey/YYYY/`
2. Copy the template structure from 2025
3. Follow the same steps to add content
4. Update homepage to feature the latest year

## Contact

For questions about updating the survey:
- Technical issues: Contact the site administrator
- Content questions: Contact Dr Alexander Saeri (a.saeri@uq.edu.au)
