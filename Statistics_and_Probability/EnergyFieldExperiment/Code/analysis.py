#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway, ttest_ind
from statsmodels.sandbox.stats.multicomp import multipletests

# Load datasets
energy_design_a = pd.read_csv("energy_design_a.csv")
energy_design_b = pd.read_csv("energy_design_b.csv")

# Determine the correct experimental design by reviewing the columns available in both datasets
# There also appears to be some blocking by geographical region inferred 
energy_design_a.head()
energy_design_b.head()
design = "randomized_block"  # Correct answer given the experimental setup

# Select the appropriate dataset
data = energy_design_b

# Create a boxplot to visualize CO2 emissions by geographical region and fuel source
sns.boxplot(
    x='Geographical_Region', 
    y='CO2_Emissions', 
    hue='Fuel_Source', 
    data=data
)
plt.title('CO2 Emissions by Geographical Region and Fuel Source')
plt.xlabel('Geographical Region')
plt.ylabel('CO2 Emissions (tons)')
plt.show()

# Identify highest median CO2 emission region and source after viewing the plot
highest_co2_region = "South"
highest_co2_source = "Coal"

# Group by Geographical Region and apply ANOVA to check significance
test_results = data.groupby('Geographical_Region').apply(
    lambda x: f_oneway(
        x[x['Fuel_Source'] == 'Natural_Gas']['CO2_Emissions'],
        x[x['Fuel_Source'] == 'Biofuel']['CO2_Emissions'],
        x[x['Fuel_Source'] == 'Coal']['CO2_Emissions']
    )
)

print("Test Results:", test_results)

# Ensure test_results show significant results (one or more with p-value < 0.05)
if any(result.pvalue < 0.05 for result in test_results):
    bonferroni_p_values = []

    # Perform pairwise comparisons for Bonferroni correction
    for zone in ['North', 'South', 'East', 'West']:
        fuels = ['Natural_Gas', 'Biofuel', 'Coal']
        comparisons = [(fuels[i], fuels[j]) for i in range(len(fuels)) for j in range(i + 1, len(fuels))]

        for fuel1, fuel2 in comparisons:
            group1 = data[(data['Geographical_Region'] == zone) & (data['Fuel_Source'] == fuel1)]['CO2_Emissions']
            group2 = data[(data['Geographical_Region'] == zone) & (data['Fuel_Source'] == fuel2)]['CO2_Emissions']
            _, p_val = ttest_ind(group1, group2)
            bonferroni_p_values.append(p_val)

    # Apply Bonferroni correction for multiple comparisons
    diff_results = multipletests(bonferroni_p_values, alpha=0.05, method='bonferroni')

print("\n\nBonferroni Corrected P-values:\n", diff_results[1])

