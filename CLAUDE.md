# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based static website for AI Governance in Australia (aigovernance.org.au), built using the Wowchemy Research Group template. The site showcases research on the SARA (Survey Assessing Risks from AI) project and provides information about AI governance relevant to Australia.

## Development Commands

### Local Development
```bash
# Start Hugo development server with drafts
hugo server -D

# Start server with future-dated content
hugo server --buildFuture

# Build for production (same as Netlify)
hugo --gc --minify -b https://www.aigovernance.org.au/
```

### Dependency Management
```bash
# Update Hugo modules (Wowchemy theme)
hugo mod get -u

# Clean module cache if needed
hugo mod clean

# Verify module dependencies
hugo mod graph
```

### Building
```bash
# Production build (outputs to public/)
hugo --gc --minify

# Build with future-dated posts
hugo --gc --minify --buildFuture
```

**Note:** Hugo v0.97.3 is required (specified in netlify.toml). The build output goes to `public/` which is gitignored.

## Architecture

### Hugo Module System
This project uses Go modules for dependency management instead of traditional Git submodules. Three Wowchemy modules are imported:
- `wowchemy-plugin-netlify` - Netlify integration
- `wowchemy-plugin-netlify-cms` - CMS support
- `wowchemy/v5` v5.7.1 - Core theme framework

### Content Architecture
Content uses Wowchemy's **block-based page builder**. Pages are composed by defining sections in YAML frontmatter:

```yaml
type: landing
sections:
  - block: hero
    content:
      title: "Title"
      text: "Content"
  - block: markdown
    content:
      text: |
        Markdown content here
```

Available block types: `hero`, `markdown`, `contact`, `people`, `collection` (for publications/posts).

### Directory Structure
- **config/_default/**: Hugo configuration files (config.yaml, params.yaml, menus.yaml, languages.yaml)
- **content/**: All page content as Markdown with YAML frontmatter
  - `_index.md` - Homepage with landing sections
  - `survey/` - SARA survey content and technical reports
  - `authors/admin/` - Author profiles
- **data/**: Theme and font configurations (themes/ready.toml, fonts/sara.toml)
- **assets/**: Build-time processed files
  - `scss/template.scss` - Custom styles (centers headers and CTA buttons)
  - `media/` - Site icons and hero images
- **static/**: Direct-serve static files
  - `figures/` - Survey charts/visualizations
  - `files/` - Downloadable PDFs

### Custom Theme: "ready"
The site uses a custom theme with teal/cyan color scheme defined in [data/themes/ready.toml](data/themes/ready.toml):
- Primary: #0C869B
- Primary Light: #E2F0F2
- Primary Dark: #053C45

Custom font "sara" uses Raleway family from Google Fonts ([data/fonts/sara.toml](data/fonts/sara.toml)).

## Configuration Files

### Key Settings
- **Site title**: "AI Governance in Australia" ([config/_default/config.yaml](config/_default/config.yaml):6)
- **Base URL**: https://www.aigovernance.org.au/ ([config/_default/config.yaml](config/_default/config.yaml):7)
- **Repository**: https://github.com/ReadyResearch/site-aigovernance-aus ([config/_default/params.yaml](config/_default/params.yaml):75)
- **Search**: Wowchemy built-in search provider ([config/_default/params.yaml](config/_default/params.yaml):94)
- **Citation style**: APA ([config/_default/params.yaml](config/_default/params.yaml):118)

### Taxonomies
Configured for academic content: `tags`, `categories`, `publication_types`, `authors` ([config/_default/config.yaml](config/_default/config.yaml):53-57)

### Ignored Files
Hugo ignores: `.ipynb`, `.ipynb_checkpoints`, `.Rmd`, `.Rmarkdown`, `_cache` ([config/_default/config.yaml](config/_default/config.yaml):38)

## Deployment

Automatic deployment via Netlify on push to main branch. Build command:
```bash
hugo --gc --minify -b $URL
```

### Netlify Redirects
Permanent redirect configured: `/fundamentals-eoi` → Google Form ([netlify.toml](netlify.toml):23-27)

### Context-Specific Builds
- **Production**: `HUGO_ENV=production`
- **Deploy previews**: Includes `--buildFuture` flag
- Uses `netlify-plugin-hugo-cache-resources` for faster rebuilds

## Content Management

### Adding New Pages
1. Create `index.md` in appropriate content directory
2. Use `type: landing` for block-based pages
3. Define sections in frontmatter with block types
4. Add menu items in [config/_default/menus.yaml](config/_default/menus.yaml)

### Adding Static Files
- **PDFs/downloads**: Place in `static/files/`
- **Images**: Place in `static/figures/` or `assets/media/`
- **Reports**: Place in `content/survey/` for survey-related content

### Editing Theme Colors
Modify [data/themes/ready.toml](data/themes/ready.toml) for color scheme changes. Both light and dark modes are defined.

### Custom Styling
Add SCSS to [assets/scss/template.scss](assets/scss/template.scss). Currently centers page headers and CTA buttons.

## Important Notes

- This site focuses on minimal custom code, leveraging Wowchemy's extensive features
- Content authors can edit Markdown files without deep technical knowledge
- The site is optimized for academic/research content with publication support
- No custom JavaScript - all functionality from Wowchemy theme
- Repository size: ~96 MB (includes images, PDFs, technical reports)
