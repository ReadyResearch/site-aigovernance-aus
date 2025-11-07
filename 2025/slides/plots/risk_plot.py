import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis with white background
fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')
ax.set_facecolor('white')

# Define x-axis (number of fatalities)
N = np.logspace(0, 3, 100)  # From 1 to 1000

# Define the boundary lines
# Upper line (Intolerable/ALARP boundary) - approximate from the image
freq_upper = 1e-3 * (N/1)**(-1)  # Roughly 10^-3 at N=1, slope ~ -1

# Lower line (ALARP/Negligible boundary) - approximate from the image  
freq_lower = 1e-5 * (N/1)**(-1)  # Roughly 10^-5 at N=1, slope ~ -1

# Set up the plot
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1, 2000)  # Extended to 2000 to show the vertical drop clearly
ax.set_ylim(1e-10, 1e-2)

# Define colour scheme matching SARA branding from R code
primary_dark_teal = '#053C45'      # Main dark teal
secondary_teal = '#0C869B'         # Lighter teal
dark_red = '#460000'               # Dark red for disagreement/intolerable
light_teal_bg = '#60c0c0'          # Light background teal
text_grey = '#4d4f4e'              # Text grey

# Create extended N array that goes beyond 1000
N_extended = np.logspace(0, np.log10(2000), 100)

# Recalculate frequency lines for extended range
freq_upper_ext = 1e-3 * (N_extended/1)**(-1)
freq_lower_ext = 1e-5 * (N_extended/1)**(-1)

# Create shaded zones
# First, fill the entire canvas with zones up to x=1000
N_main = N[N <= 1000]
freq_upper_main = 1e-3 * (N_main/1)**(-1)
freq_lower_main = 1e-5 * (N_main/1)**(-1)

# Intolerable zone: above the upper line (up to x=1000)
ax.fill_between(N_main, freq_upper_main, 1e-2, color=dark_red, alpha=0.7)

# ALARP zone: between the two lines (up to x=1000)
ax.fill_between(N_main, freq_lower_main, freq_upper_main, color=primary_dark_teal, alpha=0.7)

# Negligible zone: below the lower line (ONLY up to x=1000)
ax.fill_between(N_main, 1e-10, freq_lower_main, color=secondary_teal, alpha=0.5)

# Now fill everything to the RIGHT of x=1000 with dark red (intolerable)
# This should be a rectangle from x=1000 to x=2000, y=1e-10 to y=1e-2
ax.fill_betweenx([1e-10, 1e-2], 1000, 2000, color=dark_red, alpha=0.7)

# Plot the boundary lines on top of shading (only up to 1000)
ax.plot(N, freq_upper, color='black', linewidth=2, label='Intolerable/ALARP boundary')
ax.plot(N, freq_lower, color='black', linewidth=2, label='ALARP/Negligible boundary')

# Add vertical line at x=1000 going from the intolerable boundary DOWN to bottom (not to top)
freq_at_1000 = 1e-3 * (1000/1)**(-1)
ax.plot([1000, 1000], [1e-10, freq_at_1000], color='black', linewidth=2, linestyle='-')

# Calculate halfway point between the two lines at x=50 (on log scale)
# At x=50: freq_upper = 1e-3/50 = 2e-5, freq_lower = 1e-5/50 = 2e-7
# Geometric mean: sqrt(2e-5 * 2e-7) = 2e-6
freq_upper_at_50 = 1e-3 / 50
freq_lower_at_50 = 1e-5 / 50
alarp_y_position = (freq_upper_at_50 * freq_lower_at_50) ** 0.5  # Geometric mean for log scale

# Add region labels in white text without boxes
ax.text(50, 5e-4, 'Intolerable', fontsize=14, fontweight='bold', color='white', ha='center')
ax.text(50, alarp_y_position, 'As Low As Reasonably\nPracticable (ALARP)', fontsize=13, fontweight='bold',
        color='white', ha='center', va='center')
ax.text(50, 5e-9, 'Negligible', fontsize=14, fontweight='bold', color='white', ha='center')

# Set labels with SARA branding style
ax.set_xlabel('Number of Fatalities, N', fontsize=12, fontweight='bold', color=text_grey)
ax.set_ylabel('Frequency of N or more fatalities per year', fontsize=12, fontweight='bold', color=text_grey)
# Title removed per user request

# Add grid with light grey colour matching SARA style
ax.grid(True, which="major", ls="-", alpha=0.4, color='lightgrey', linewidth=0.8)
ax.grid(True, which="minor", ls="-", alpha=0.2, color='lightgrey', linewidth=0.5)

# Set background color
ax.set_facecolor('#f5f5f5')  # Very light grey background

# Set specific y-axis ticks to match the original
y_ticks = [1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2]
ax.set_yticks(y_ticks)

# Set specific x-axis ticks
x_ticks = [1, 10, 100, 1000]
ax.set_xticks(x_ticks)
ax.set_xticklabels(['1', '10', '100', '1,000'])

# Add minor tick at 2000 to show the extension
ax.set_xticks([2000], minor=True)

# Clean up tick parameters with grey text
ax.tick_params(axis='both', which='major', labelsize=10, length=5, width=1, colors=text_grey)
ax.tick_params(axis='both', which='minor', length=3, width=0.5)

# Clean up spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_color(text_grey)
ax.spines['bottom'].set_color(text_grey)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/societal_risk_criteria.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
