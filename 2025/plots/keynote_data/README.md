# MRP Plot Data for Keynote Presentations

This folder contains CSV files with data from all major MRP (Multilevel Regression and Post-stratification) plots from the SARA 2025 technical report. These files are formatted to be easily imported into Keynote for creating presentation-ready charts.

## 📊 Available Data Files

### Trust & Regulation
- **trust_measures.csv** - 14 trust-building measures (e.g., AI Safety Institute, safety testing)
- **trust_tech_companies.csv** - Trust in tech companies (4 levels from "Not at all" to "A great deal")
- **regulation_concern.csv** - Concerns about under vs. over-regulation
- **regulation_pace.csv** - Perceived pace of regulation vs. technology

### Priority Risks
- **priority_risks.csv** - 15 AI risks ranked by public concern (privacy, cyber attacks, deepfakes, etc.)

### Policy Preferences
- **treaty_ban_agi.csv** - Support/oppose international ban on superintelligence
- **government_priority.csv** - Risk management vs. innovation priorities

### Risk Tolerance
- **ai_vs_airline.csv** - Desired AI safety standards compared to aviation
- **willingness_to_pay.csv** - Annual willingness to pay to reduce catastrophic risk

### Concerns
- **worried_job_loss.csv** - Worry about AI-caused unemployment (4 levels)
- **worried_lose_control.csv** - Worry about humans losing control of AI (4 levels)
- **ai_good_harm.csv** - Perceptions of AI doing more good vs. harm

### Media & Barriers
- **media_ai_society.csv** - Desire for media coverage of AI's societal impact
- **media_ai_regulation.csv** - Desire for media coverage of AI regulation
- **ai_usage_barriers.csv** - 10 barriers preventing AI adoption (privacy, trust, cost, etc.)

## 🎨 How to Use in Keynote

### Method 1: Copy-Paste (Recommended for Quick Charts)

1. **Open your CSV file** in Numbers, Excel, or any text editor
2. **Select and copy all the data** (including headers)
3. **In Keynote**, insert a chart: `Insert` → `Chart` → Choose chart type
4. **Click "Edit Chart Data"** in the Format panel (or double-click the chart)
5. **Paste the data** into the chart data editor
6. Keynote will automatically update the chart with your data
7. **Format the chart**: adjust colors, labels, legends, etc.

### Method 2: Import via Numbers

1. **Open the CSV** in Numbers
2. **Select the data** you want to chart
3. **Create a chart** in Numbers: `Insert` → `Chart`
4. **Copy the chart** from Numbers
5. **Paste into Keynote**
6. Further customize in Keynote as needed

## 📈 Understanding the Data Format

Each CSV file contains:
- **Column 1**: Labels (e.g., "Right to human review", "Data privacy", "Support")
- **Column 2**: `Percentage (%)` - The main MRP-adjusted population estimate
- **Column 3**: `Lower CI (%)` - Lower bound of 95% confidence interval
- **Column 4**: `Upper CI (%)` - Upper bound of 95% confidence interval

### Example from `trust_measures.csv`:
```
Measure,Percentage (%),Lower CI (%),Upper CI (%)
Right to human review,91,84.9,95.2
Australian AI Safety Institute,89.7,85,93.4
```

This means:
- 91% of Australians would trust AI more with human review rights
- We're 95% confident the true population value is between 84.9% and 95.2%

## 💡 Tips for Effective Keynote Charts

### 1. Choose the Right Chart Type
- **Bar charts** (horizontal or vertical): Best for comparing categories (trust measures, priority risks)
- **Column charts**: Good for comparisons across few categories
- **Stacked bars**: Useful for showing parts of a whole (e.g., ordinal responses)

### 2. Showing Confidence Intervals
- Keynote's error bars can display the confidence intervals
- In chart data editor, add a column for error values
- In Format panel, enable "Error Bars" and select "Custom Values"
- For asymmetric errors, calculate: `Upper CI - Percentage` and `Percentage - Lower CI`

### 3. Color Recommendations
Based on SARA 2025 report styling:
- **Primary (Teal)**: #053C45 or RGB(5, 60, 69)
- **Secondary (Light Teal)**: #0C869B or RGB(12, 134, 155)
- **Text Gray**: #4D4F4E or RGB(77, 79, 78)
- **Disagreement Red**: #460000 or RGB(70, 0, 0)

### 4. Simplifying for Presentations
- You can use just the `Percentage (%)` column for cleaner visuals
- The confidence intervals show statistical rigor but may clutter slides
- Consider mentioning CIs verbally or in a footnote rather than displaying them

### 5. Top Items Only
For dense datasets (trust measures, priority risks):
- Sort by percentage (already done in the CSVs)
- Show only top 5-7 items for readability
- Use "... and 7 others" notation if needed

## 📊 Sample Chart Types by File

| File | Recommended Chart | Why |
|------|------------------|-----|
| trust_measures.csv | Horizontal bar chart | Easy to read long measure names |
| priority_risks.csv | Horizontal bar chart | Clear ranking visualization |
| trust_tech_companies.csv | Stacked bar or column | Shows distribution across levels |
| ai_vs_airline.csv | Column chart | Compares 5 discrete safety levels |
| government_priority.csv | Simple column or pie | Just 2 categories |
| worried_*.csv | Stacked column | Shows worry level distribution |
| ai_usage_barriers.csv | Horizontal bar | Long barrier descriptions |

## 🔄 Regenerating the Data

If you need to regenerate these CSV files (e.g., after data updates):

```bash
cd /Users/michaelnoetel/git/r-aus-sara
Rscript 2025/02_analysis/export_plot_data_for_keynote.R
```

This will overwrite all CSV files in this directory with fresh data from the MRP results.

## 📝 Citation

When using these data in presentations, please cite:

> Noetel, M., Saeri, A.K., Graham, J.G. (2025). *Survey Assessing Risks from Artificial Intelligence (SARA) 2025: Australian Public Attitudes Toward AI Risks and Governance.* The University of Queensland. https://aigovernance.org.au/survey/2025

## ❓ Questions?

For technical questions about the data or analysis, contact:
- Dr. Michael Noetel: m.noetel@uq.edu.au

---

Generated: October 28, 2025
Source: SARA 2025 MRP Analysis
Location: `/Users/michaelnoetel/git/r-aus-sara/2025/plots/keynote_data/`
