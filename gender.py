import matplotlib.pyplot as plt
import numpy as np

# Group names
groups = ['A', 'B', 'C', 'D', 'E']

# Scores
men_scores = [22, 30, 35, 35, 26]
women_scores = [25, 32, 30, 35, 29]

# Set the width of each bar and positions on x-axis
bar_width = 0.35
x = np.arange(len(groups))  # [0, 1, 2, 3, 4]

# Plot bars for men and women side by side
plt.bar(x - bar_width/2, men_scores, width=bar_width, label='Men', color='skyblue')
plt.bar(x + bar_width/2, women_scores, width=bar_width, label='Women', color='lightpink')

# Labeling
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)  # Set group labels on x-axis
plt.legend()

# Optional: add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Make layout tight and save the plot
plt.tight_layout()
plt.savefig('scores_by_group_gender.png')

