# Hypothesis Testing: Drug Safety in Healthcare

## Project Description

Pharmaceutical drugs have become an essential part of healthcare systems. Ensuring their safety, with minimal adverse effects, is crucial. This project focuses on hypothesis testing to evaluate the adverse effects of a hypothetical drug trial, determining whether the reactions observed are statistically significant. Several hypothesis tests will be conducted using Python to explore if factors such as age influence the adverse reactions significantly.

This project is in collaboration with a non-profit organization that advocates for pharmaceutical drug safety and provides independent reports, separate from drug manufacturers.

## Dataset Overview

The dataset used for this analysis, `drug_safety.csv`, is a modified version of data obtained from the [Vanderbilt University Department of Biostatistics](https://hbiostat.org/data/). It focuses on drug safety by evaluating adverse reactions in patients who participated in a randomized controlled trial. The dataset includes demographic information, vital signs, and lab measures. The key goal is to examine the significance of adverse effects resulting from the drug.

### Dataset Summary:
- **Source**: [Hbiostat](https://hbiostat.org/data/repo/safety.rda) (Vanderbilt University)
- **Type**: Modified to reflect adverse effects and the number of adverse effects per individual.
- **Observations**: 2-to-1 ratio of drug to placebo group.

### Dataset Columns:

| Column | Description |
|--------|-------------|
| `sex` | The gender of the individual |
| `age` | The age of the individual |
| `week` | The week of the drug testing |
| `trx` | The treatment group: Drug or Placebo |
| `wbc` | The count of white blood cells |
| `rbc` | The count of red blood cells |
| `adverse_effects` | Indicates whether the individual experienced at least one adverse effect (Boolean) |
| `num_effects` | The number of adverse effects experienced by a single individual |

---

## Objectives

The non-profit organization is interested in the following questions related to the drug trial data:

1. Are the adverse reactions observed statistically significant compared to the placebo group?
2. Does age play a significant role in the likelihood of experiencing adverse reactions?
3. Are there significant differences in the number of adverse effects experienced between drug and placebo groups?

## Hypothesis Testing

The primary task is to conduct hypothesis tests using Python to explore the following:

1. **Proportion Test**: To determine if the proportion of adverse effects is significantly higher in the drug group compared to the placebo group.
2. **T-Tests**: To check if there is a significant difference in vital signs (e.g., white blood cell counts) between individuals who experienced adverse effects and those who did not.
3. **Regression Analysis**: To assess if factors such as age, gender, or vital signs are significant predictors of adverse reactions.

## Features

- **Exploratory Data Analysis (EDA), & Data Cleaning**: Visualize and summarize key statistics of the dataset.
- **Hypothesis Testing**: Perform statistical tests to evaluate adverse reactions.
- **Regression Analysis**: Explore the influence of demographic and clinical variables on adverse reactions.

## Dependencies

The following libraries are required for this project:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `pingouin`  *(for statistical analysis)*
