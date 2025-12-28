import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# 1. Load and Clean
# Ask for the path to your CSV file
file_path = input("Enter the path to your MRR CSV file: ")
# Replace any \ for / in the file path
file_path = file_path.replace('\\','/')
file_path = file_path.replace('"', '')                 
df = pd.read_csv(file_path)
df['q_factor'] = 1550 / df['FWHM_admr(nm)']

# 2. Define Pass/Fail Criteria
# (Change these based on what specifications you are looking for)
Q_MIN = 1500
FSR_MIN = 5.0
FSR_MAX = 15.0

# Create a boolean column for "Pass"
df['is_pass'] = (df['q_factor'] >= Q_MIN) & \
                (df['FSR(nm)'] >= FSR_MIN) & \
                (df['FSR(nm)'] <= FSR_MAX)

# 3. Create Heatmap Base
pivot = df.pivot_table(values='q_factor', index='radius', columns='coup_g', aggfunc='mean')
plt.figure(figsize=(10, 7))
ax = sns.heatmap(pivot, annot=True, fmt=".0f", cmap="magma")

# 4. Create Pass/Fail Markers
# We look through the dataframe for any design that 'Passed' and mark its location
x_coords = [float(l.get_text()) for l in ax.get_xticklabels()]
y_coords = [float(l.get_text()) for l in ax.get_yticklabels()]

for i, row in df[df['is_pass']].iterrows():
    # Find the cell index for Radius and Gap
    try:
        x_idx = x_coords.index(row['coup_g']) + 0.5
        y_idx = y_coords.index(row['radius']) + 0.5
        # Plot a star on the passing cell
        ax.plot(x_idx, y_idx, marker='*', color='white', markersize=15, markeredgecolor='black')
    except:
        continue

# 5. Add Legend and Labels
legend_elements = [Line2D([0], [0], marker='*', color='w', label='Passes Design Specs',
                          markerfacecolor='w', markersize=15, markeredgecolor='black', linestyle='None')]
ax.legend(handles=legend_elements, loc='upper left')
plt.title("Automated Wafer Map: Design Pass/Fail Status")
plt.show()