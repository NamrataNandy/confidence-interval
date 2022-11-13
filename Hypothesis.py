#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statsmodels.api as sm
import numpy as np
import pandas as pd
import scipy.stats.distributions as dist


# In[2]:


# One Population Proportion
# Research Question
# In previous years 52% of parents believed that electronics and social media was the cause of their teenager’s lack of sleep. Do more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media?

# Population: Parents with a teenager (age 13-18)
# Parameter of Interest: p
# Null Hypothesis: p = 0.52
# Alternative Hypthosis: p > 0.52 (note that this is a one-sided test)

# 1018 Parents

# 56% believe that their teenager’s lack of sleep is caused due to electronics and social media.

n=1018
pnull=0.52
phat=0.56

# Calculate test statistic and p-value
sm.stats.proportions_ztest(phat * n, n, pnull, alternative='larger', prop_var=0.52)


# In[3]:


# Difference in Population Proportions¶
# Research Question
# Is there a significant difference between the population proportions of parents of black children and parents of Hispanic children who report that their child has had some swimming lessons?

# Populations: All parents of black children age 6-18 and all parents of Hispanic children age 6-18
# Parameter of Interest: p1 - p2, where p1 = black and p2 = hispanic
# Null Hypothesis: p1 - p2 = 0
# Alternative Hypthosis: p1 - p2  ≠  = 0

# 91 out of 247 (36.8%) sampled parents of black children report that their child has had some swimming lessons.

# 120 out of 308 (38.9%) sampled parents of Hispanic children report that their child has had some swimming lessons

# This example implements the analysis from the "Difference in Two Proportions" lecture videos

# Sample sizes
n1 = 247
n2 = 308

# Number of parents reporting that their child had some swimming lessons
y1 = 91
y2 = 120

# Estimates of the population proportions
p1 = round(y1 / n1, 2)
p2 = round(y2 / n2, 2)

# Estimate of the combined population proportion
phat = (y1 + y2) / (n1 + n2)

# Estimate of the variance of the combined population proportion
va = phat * (1 - phat)

# Estimate of the standard error of the combined population proportion
se = np.sqrt(va * (1 / n1 + 1 / n2))

# Test statistic and its p-value
test_stat = (p1 - p2) / se


# Print the test statistic its p-value
print("Test Statistic")
print(round(test_stat, 2))

# print("\nP-Value")
# print(round(pvalue, 2))


# In[ ]:




