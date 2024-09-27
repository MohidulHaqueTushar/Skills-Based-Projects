#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing in Healthcare: Drug Safety
# 
# A pharmaceutical company GlobalXYZ has just completed a randomized controlled drug trial. To promote transparency and reproducibility of the drug's outcome, they (GlobalXYZ) have presented the dataset to your organization, a non-profit that focuses primarily on drug safety.
# 
# Approach the project:
# 1. Two-sample proportions z-test
# 2. Association between adverse effects and the groups
# 3. Inspecting whether age is normally distributed
# 4. Significant difference between the ages of both groups

# In[50]:


# Import packages
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
import pingouin
import seaborn as sns
import matplotlib.pyplot as plt


# In[51]:


import warnings

# Suppress only UserWarning from pingouin
warnings.filterwarnings("ignore", category=UserWarning, module='pingouin')


# In[52]:


# Load the dataset
drug_safety = pd.read_csv("drug_safety.csv")


# ### Explanatory Data Analysis (EDA)

# In[53]:


# 5 rows of the data
drug_safety.head()


# In[54]:


# details on the data
drug_safety.describe()


# In[55]:


# dimensions
drug_safety.shape


# **Note:** Data has 16103 rows and 8 features in tottal.

# In[56]:


# more informations, i.e, data types, null values
drug_safety.info()


# ### Analysis

# In[57]:


# Count the adverse_effects column values for each trx group
adv_eff_by_trx = drug_safety.groupby("trx").adverse_effects.value_counts()


# In[58]:


print("The output is:\n",adv_eff_by_trx)


# In[59]:


# Compute total rows in each group
adv_eff_by_trx_totals = adv_eff_by_trx.groupby("trx").sum()


# In[60]:


print("The output is:\n", adv_eff_by_trx_totals)


# In[61]:


# Create an array of the "Yes" counts for each group
yeses = [adv_eff_by_trx["Drug"]["Yes"], adv_eff_by_trx["Placebo"]["Yes"]]
print("The output is: ", yeses)


# In[62]:


# Create an array of the total number of rows in each group
n = [adv_eff_by_trx_totals["Drug"], adv_eff_by_trx_totals["Placebo"]]
print("The output:", n)


# In[63]:


# Perform a two-sided z-test on the two proportions
two_sample_results = proportions_ztest(yeses, n)
print("Result:", two_sample_results)


# In[64]:


# Store the p-value
two_sample_p_value = two_sample_results[1]
print("Result:", two_sample_p_value)


# In[65]:


# Determine if num_effects and trx are independent
num_effects_groups = pingouin.chi2_independence(data=drug_safety, x="num_effects", y="trx")


# In[66]:


# Extract the p-value
num_effects_p_value = num_effects_groups[2]["pval"][0]
print("Result:", num_effects_p_value)


# ### Finding age is normally distributed or not : by Visuals or a atatistical test

# In[67]:


# Create a histogram with Seaborn
sns.histplot(data=drug_safety, x="age", hue="trx")
plt.show()


# In[68]:


# To choose between unpaired t-test and Wilcoxon-Mann-Whitney test
normality = pingouin.normality(
    data=drug_safety,
    dv='age',
    group='trx',
    method='shapiro', # the default
    alpha=0.05) # 0.05 is also the default


# In[69]:


print("Output: \n",normality)


# #### Significant difference between the ages of both groups
# - To ensure age wasn't a confounder, conduct a Mann-Whitney test to determine if age differed significantly between the trx groups.
# - Performing a Mann-Whitney U test
# 
# 

# In[70]:


# Select the age of the Drug group
age_trx = drug_safety.loc[drug_safety["trx"] == "Drug", "age"]


# In[71]:


# Select the age of the Placebo group
age_placebo = drug_safety.loc[drug_safety["trx"] == "Placebo", "age"]


# In[72]:


# Since the data distribution is not normal: Conduct a two-sided Mann-Whitney U test
age_group_effects = pingouin.mwu(age_trx, age_placebo)


# In[73]:


# Extract the p-value
age_group_effects_p_value = age_group_effects["p-val"]
print("Output: \n", age_group_effects_p_value)

