# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 2. Load the Dataset
# Replace 'Selected_Online_Sport_Wagering_Data.csv' with the actual file name or path
df = pd.read_csv('Selected_Online_Sport_Wagering_Data.csv')

# 3. Data Cleaning and Preparation
# Perform necessary data cleaning and preparation steps
# This may include handling missing values, data type conversion, etc.

# 4. Data Visualization
# Example: Plotting a bar chart of a relevant metric

plt.figure(figsize=(15, 10))
sns.barplot(x='Licensee', y='Total Gross Gaming Revenue', data=df)
plt.title('Total Gross Gaming Revenue by licensee in Online Sport Wagering Report')
plt.xlabel('Licensee')
plt.ylabel('Total Gross Gaming Revenue')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
plt.show()

# 5. Statistical Analysis
# Example: Performing a simple statistical test
group1 = df[df['Licensee'] == 'Licensee1']['Total Gross Gaming Revenue']
group2 = df[df['Licensee'] == 'Licensee2']['Total Gross Gaming Revenue']
t_stat, p_val = stats.ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, P-value: {p_val}")