# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **SARA (Survey Assessing Risks from AI)** website built with Hugo (v0.97.3) using the Wowchemy Research Group template. The site is dedicated exclusively to publishing results from the annual SARA survey.

SARA investigates Australian public perceptions of AI risks and support for AI governance actions. The site currently hosts the 2024 survey results and has a template ready for the 2025 survey.

**Site Title:** "SARA - Survey Assessing Risks from AI"
**Domain:** https://www.aisafety.org.au/

## Development Commands

### Running the Development Server
```bash
hugo server --buildDrafts --buildFuture --bind 0.0.0.0 --port 1313
```
**IMPORTANT**: Always run the Hugo server in a background process using the `run_in_background` parameter in the Bash tool.

**Verify server is running:**
```bash
ps aux | grep hugo
```

**Server will be available at:** http://localhost:1313

### Building the Site
```bash
# Local build
hugo

# Production build (matches Netlify)
hugo --gc --minify -b https://www.aisafety.org.au/
```

### Hugo Module Management
```bash
# Update Hugo modules
hugo mod get -u

# Clean module cache
hugo mod clean

# Download/verify modules
hugo mod vendor
```

## Site Structure

### Current Pages
```
/                    # Homepage - landing page with links to both surveys
/survey/2025/        # 2025 survey (template with TODO placeholders)
/survey/2024/        # 2024 survey (complete archive)
```

### Content Organization
```
content/
├── _index.md                      # Homepage (landing page)
└── survey/
    ├── 2024/                      # Archived 2024 survey
    │   ├── index.md               # Survey landing page
    │   ├── sara_technical_report.html
    │   ├── sara_technical_report_files/
    │   ├── report_technical/
    │   ├── banner.png
    │   ├── readyuqlogotrans.png
    │   └── styles.css
    └── 2025/                      # Template for 2025 survey
        └── index.md               # Template with TODO markers
```

### Homepage Structure (`content/_index.md`)
Simple landing page with three sections:
1. **Hero Section**:
   - Title: "Survey Assessing Risks from AI"
   - Background: Sydney Opera House with crowd (dominic-kurniawan-suryaputra-8bA_OXkFq2s-unsplash.jpg)
   - CTAs: "View 2025 Survey" and "View 2024 Results"
2. **About SARA**: Brief description of the annual survey
3. **Contact**: Contact information and org logos

### Survey Page Structure
Each survey year (`/survey/YYYY/index.md`) contains:
- Hero section with survey year and description
- Key insights section with findings
- Links to briefing (PDF & Google Doc)
- Links to technical report (SSRN & local HTML)
- Figures/visualizations
- About the survey section
- Contact section

## Theming & Design

### Theme Configuration
- **Theme**: Custom `ai_safety_modern` theme defined in `data/themes/ai_safety_modern.toml`
  - Modern blue gradient color palette
  - Separate light/dark mode configurations
- **Typography**: `modern_typography` font configuration in `data/fonts/`
- **Custom Styles**: `assets/scss/template.scss`

### Hero Background Image
- **Current Image**: Sydney Opera House with crowd
- **File**: `assets/media/dominic-kurniawan-suryaputra-8bA_OXkFq2s-unsplash.jpg`
- **Positioning**: Responsive positioning to emphasize crowd over sky
  - Mobile (default): `center 45%`
  - Desktop (768px+): `center 58%`
  - Large screens (1440px+): `center 60%`
- **Brightness Filter**: `0.5` (50% to ensure text readability)

### Important CSS Notes

**Background Image Positioning:**
The background uses responsive positioning in `assets/scss/template.scss` to show more of the Opera House and crowd, less sky:
```scss
.home-section-bg.bg-image {
  background-position: center 45% !important; /* Mobile */
}
@media (min-width: 768px) {
  .home-section-bg.bg-image {
    background-position: center 58% !important; /* Desktop */
  }
}
```

**Strong Tag Styling:**
Avoid using `display: block` on `<strong>` tags as it creates unwanted line breaks. Keep inline:
```scss
/* DON'T do this */
.home-section p strong {
  display: block;  /* ❌ Creates line breaks */
}

/* DO this instead */
.home-section p strong {
  font-weight: 600;  /* ✅ Stays inline */
}
```

### Configuration Files
Split configuration in `config/_default/`:
- `config.yaml`: Core Hugo settings, modules, taxonomies, site title
- `params.yaml`: Appearance, SEO, header/footer, branding
- `menus.yaml`: Navigation structure (currently minimal)
- `languages.yaml`: Language configuration

### Hugo Modules
Uses Wowchemy Hugo modules:
- `wowchemy-plugin-netlify-cms`: CMS integration
- `wowchemy-plugin-netlify`: Netlify-specific features
- `wowchemy/v5`: Core Wowchemy theme framework

## Adding SARA 2025 Survey Results

When 2025 survey data is ready, update `content/survey/2025/index.md`:

1. **Update Survey Details**:
   - Replace "We are conducting" with "We conducted"
   - Add actual survey dates in Key Insights
   - Add sample size (e.g., "1,141 Australians")

2. **Add Key Findings**:
   - Replace TODO placeholders with actual findings
   - Follow the format from 2024 survey

3. **Upload Reports**:
   - Create Google Doc briefing and add link
   - Create PDF export link
   - Upload technical report HTML: `sara_2025_technical_report.html`
   - Create supporting files directory: `sara_2025_technical_report_files/`
   - Publish to SSRN and add DOI link

4. **Add Figures**:
   - Upload figures to `static/figures/` (e.g., `SARA_2025_risk_priority.png`)
   - Embed in markdown using HTML img tags:
     ```html
     <img src='/figures/SARA_2025_figure.png' alt='Description'
          style='display: block; margin-left: auto; margin-right: auto; width: 80%;'/>
     ```

5. **Update Citation**:
   - Change year from 2024 to 2025
   - Update any author information if needed

## CSS Debugging

**Wowchemy CSS Architecture:**
- CSS compiled into `/public/css/wowchemy.css` (not in repo)
- Uses Hugo modules from GitHub
- Often requires `!important` to override defaults

**Debug CSS Issues:**
1. Inspect live HTML: `curl -s "http://localhost:1313" | grep -A20 "wg-hero"`
2. Find actual classes used (e.g., `.wg-hero`, `.home-section-bg.bg-image`)
3. Check compiled CSS: `grep -n "\.wg-hero" public/css/wowchemy.css`
4. Override with exact classes + `!important`

**Key Wowchemy Classes:**
- `.wg-hero` - Hero section container
- `.home-section-bg.bg-image` - Background image
- `.home-section` - Content sections
- `[data-theme="dark"]` - Dark mode

## Asset Management

**Images:**
- Homepage background: `assets/media/dominic-kurniawan-suryaputra-8bA_OXkFq2s-unsplash.jpg`
- Survey banner: `content/survey/YYYY/banner.png` or use `sara_hero2.webp`
- Survey figures: `static/figures/`
- Organization logos: `static/` (e.g., `readyuqlogo.png`)

**Embed Methods:**
- Direct HTML img tags for precise control
- Hugo shortcodes for processed assets: `{{< figure src="file.jpg" >}}`
- YouTube: Use HTML iframe (more reliable than Hugo shortcode)

## Deployment

**Platform:** Netlify
- Hugo version: 0.97.3 (locked in netlify.toml)
- Build command: `hugo --gc --minify -b $URL`
- Publish directory: `public`
- Auto-deploys from main branch

## Google Search Console

Google Search Console is activated. Check periodically for:
- Indexing status
- Search performance
- Mobile usability
- Technical issues
