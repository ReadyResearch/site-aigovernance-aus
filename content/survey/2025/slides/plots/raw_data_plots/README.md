# SARA 2025 Raw Data Plots

This folder contains **45 plots** showing raw response distributions for all substantive survey items, including "Not sure" responses.

## Overview

All plots use consistent SARA branding (teal color scheme #053C45) and show:
- Complete response distributions including "Not sure"/"Don't know" (in grey)
- Sample size (n=932 Australian adults who passed data quality checks)
- Fieldwork dates (August 14-30, 2025)

## Plot Categories

### 1. Ordinal Variables (11 plots)
Stacked horizontal bars showing percentage distribution across Likert scales:

- `extinction_priority_raw.png` - **THE KEY MISSING PLOT!** AI extinction risk as global priority
- `ai_good_harm_raw.png` - Will AI do more good or harm?
- `ai_vs_airline_raw.png` - AI safety standards compared to aviation
- `media_ai_regulation_raw.png` - Want more media coverage of AI regulation
- `media_ai_society_raw.png` - Want more media coverage of AI's societal impact
- `regulation_pace_raw.png` - Is regulation keeping pace with AI development?
- `treaty_ban_agi_raw.png` - Support for international treaty to ban AGI
- `trust_tech_companies_raw.png` - Trust in tech companies to ensure AI safety
- `willingness_to_pay_raw.png` - Maximum annual payment for AI risk reduction
- `worried_lose_control_raw.png` - Worry about humans losing control of AI
- `worried_job_loss_raw.png` - Worry about AI-driven job loss

### 2. Trust Mitigation Items (14 plots)
Individual plots for each trust-building measure (5-level Likert):

- `trust_emergency_shutdown_raw.png`
- `trust_incident_reporting_raw.png`
- `trust_safety_protocols_raw.png`
- `trust_annual_audits_raw.png`
- `trust_safety_testing_raw.png`
- `trust_safety_institute_raw.png`
- `trust_risk_assessments_raw.png`
- `trust_human_review_raw.png`
- `trust_liability_rules_raw.png`
- `trust_inform_ai_use_raw.png`
- `trust_whistleblower_raw.png`
- `trust_developer_liability_raw.png`
- `trust_watermarking_raw.png`
- `trust_ai_regulator_raw.png`

### 3. Priority Risk Items (15 plots)
Individual plots for each risk area (5-level Likert):

- `priority_cyber_attacks_raw.png`
- `priority_weapons_raw.png`
- `priority_reliability_raw.png`
- `priority_loss_control_raw.png`
- `priority_copyright_raw.png`
- `priority_market_raw.png`
- `priority_jobs_raw.png`
- `priority_environment_raw.png`
- `priority_inequality_raw.png`
- `priority_bias_raw.png`
- `priority_fake_manipulation_raw.png`
- `priority_fake_individuals_raw.png`
- `priority_privacy_raw.png`
- `priority_expert_risk_raw.png`
- `priority_economy_raw.png`

### 4. Categorical Variables (2 plots)
Grouped bar charts showing distribution:

- `gov_priority_raw.png` - Should government prioritise managing risks vs driving innovation?
- `regulation_concern_raw.png` - Worried government will go too far vs not far enough?

### 5. Randomized Experimental Variables (3 plots)
Raincloud plots (half-violin + boxplot + jittered points):

- `casualty_risk_tolerance_raw.png` - Risk tolerance by casualty level (10 to 8 billion)
- `risk_benefit_tradeoff_raw.png` - Acceptability of catastrophic risk vs dramatic benefits
- `temporal_tradeoff_raw.png` - Worthiness of delays to improve AI safety

## How to Regenerate All Plots

Simply run the comprehensive plotting script:

```r
source("2025/02_analysis/9_all_items_raw_plots.R")
```

This single script creates all 45 plots in one run (~30 seconds).

## Differences from Main Plots

The main plots folder (`2025/plots/`) contains:
- **MRP-adjusted estimates** with confidence intervals (population-weighted)
- **Binary aggregations** (e.g., agree/disagree collapsed)
- **Curated visualizations** for the technical report

This folder (`raw_data_plots/`) contains:
- **Unadjusted raw frequencies** from the sample
- **All response levels** including "Not sure"
- **Individual items** (trust and priority items shown separately, not aggregated)

## Color Scheme

- **Primary teal**: #053C45 (dark) to #0C869B (light)
- **Not sure**: #b0b0b0 (grey)
- **Panel background**: grey90
- **Grid lines**: lightgrey

## Technical Notes

- Data source: `2025/01_cleaning/sara2025_clean.rds`
- n = 932 (respondents who passed both attention checks)
- All plots are 300 DPI PNG files
- Stacked bars: 14" × 6"
- Grouped bars: 12" × 6"
- Rainclouds: 12-14" × 8"

---

**Generated**: November 2025
**Script**: `2025/02_analysis/9_all_items_raw_plots.R`
**Study**: SARA 2025 (Survey Assessing Risks from AI)
**PI**: Michael Noetel, University of Queensland
