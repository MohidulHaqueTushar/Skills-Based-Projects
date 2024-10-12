![image](https://github.com/MohidulHaqueTushar/Skills-Based-Projects/blob/main/Statistics_and_Probability/EnergyFieldExperiment/Data/co2.png)
# Exploring Experimental Design in the Energy Field

## Project Overview
This project focuses on analyzing CO2 emissions across different geographical regions and fuel sources to understand their environmental impacts within the energy sector. By exploring the energy sector's experimental setup, performing data visualization, and applying statistical tests, you will gain insights into how emissions vary based on region and fuel type. You will also interpret significant patterns in energy consumption and environmental impact.

### Key Objectives:
1. **Identify the experimental design** used by the research team (factorial or randomized block).
2. **Visualize CO2 emissions** across regions and fuel sources.
3. **Conduct statistical tests** to determine significant differences in emissions.
4. **Perform post-hoc analysis** if significant differences are detected.

---

## Project Description
In this project, you will:
- Explore the relationship between CO2 emissions, fuel sources, and geographical regions.
- Utilize tools like **pandas** for data manipulation, **seaborn** for visualization, and **scipy** and **statsmodels** for statistical analysis.
- Interpret the experimental design used and evaluate the environmental impacts of different energy consumption patterns.

This hands-on experience will enhance your data analysis skills and provide you with the knowledge to uncover hidden patterns in energy-related CO2 emissions.

---

## Project Instructions

### 1. Identifying the Experimental Design
Determine whether the environmental research team used a **factorial design** (which evaluates multiple independent variables) or a **randomized block design** (which groups units to control variance). Store the experimental design type in the `design` string object.

#### Approach:
- Examine the dataset to understand the setup.
- Review the data to decide if it aligns with a factorial or randomized block design.

### 2. Create a CO2 Emissions Boxplot
Visualize the relationship between CO2 emissions, geographical regions, and fuel sources. The boxplot will help identify which combination of region and fuel source yields the highest median CO2 emissions.

#### Approach:
- Use **Seaborn**'s `sns.boxplot()` to create a boxplot, with geographical regions on the x-axis, CO2 emissions on the y-axis, and coloring by fuel source.
- Identify and store the highest median emission values for region and fuel source in `highest_co2_region` and `highest_co2_source` string objects.

### 3. Apply a Statistical Test
Conduct a statistical test to evaluate whether there is a significant difference in CO2 emissions based on fuel source, grouped by region.

#### Approach:
- Use **ANOVA** (`f_oneway()`) to test for differences in emissions between fuel sources across regions.
- Group data by geographical regions and fuel sources.
- Store the test results as a pandas Series in `test_results`.

### 4. Perform a Post-Hoc Analysis and Correction
If significant results are found from the ANOVA test, apply a post-hoc analysis to check for pairwise differences between fuel types, using the **Bonferroni correction** for multiple comparisons.

#### Approach:
- Use pairwise t-tests (`ttest_ind`) to compare emissions between each fuel type.
- Apply the **Bonferroni correction** to the resulting p-values using `multipletests` from the **statsmodels** library.
- Store the results of these comparisons in the `diff_results` tuple.

---

## How to Approach the Project

### 1. Identifying the Experimental Design
- Determine whether the design is **randomized block** or **factorial** by reviewing the experimental setup.
- Use the `.head()` method to inspect the data structure and column names.

### 2. Creating a Boxplot
- Use **Seaborn** to create a boxplot with geographical regions as the x-axis and CO2 emissions as the y-axis.
- Set `hue='Fuel_Source'` to differentiate between fuel sources in the plot.

### 3. Applying a Statistical Test
- Use **ANOVA** (`f_oneway()`) to evaluate significant differences in emissions.
- Apply a lambda function to group the data by geographical regions and fuel sources before performing the test.

### 4. Performing a Post-Hoc Analysis and Correction
- Use **pairwise t-tests** for fuel type comparisons.
- Apply the **Bonferroni correction** to adjust for multiple comparisons and avoid Type I errors.

---

## Dependencies


- Python 3.x
- pandas
- seaborn
- scipy
- statsmodels

To install the required packages, you can use the following commands:

```bash
pip install pandas seaborn scipy statsmodels
```

## Conclusion
This project enables you to explore the energy sector's environmental impact by analyzing CO2 emissions. By completing the steps, you'll gain practical skills in experimental design identification, data visualization, and statistical analysis, which are essential for analyzing real-world energy data.
