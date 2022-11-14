#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Car Seat Study: A sample of 659 parents with a toddler was taken and asked if they use a car seat for all travel with their toddler.
# 540 parents resonded "yes" to the question.
# What proportion of parents report they use car seat for all travel with their toddler?

import numpy as np

# First calculate best estimate p^
n=659 # sample size
x=540 # number responded "yes"
p_hat=x/n

# With 95% confidence interval, t_star will be 1.96
t_star=1.96

# Calculate the standard error
se=np.sqrt((p_hat*(1-p_hat))/n)
se

# Get best estimate +- "a few".estimated se
lcb=p_hat - (t_star*se)
ucb=p_hat + (t_star*se)
(lcb,ucb)

# Interpretation: With 95% confidence, the population proportion of parents with a toddler who use a car seat for travel is estimated between 79% to 84.8%.


# In[19]:


# package that automatically calculates lower bound and upper bound
import statsmodels.api as sm
sm.stats.proportion_confint(x, n)


# In[20]:


# Case Study on Cartwheel data: Calculating confidence interval for mean cartwheel distance

import pandas as pd
df=pd.read_csv(r'C://Users/Namrata/Desktop/Courseera/statistics using python/Datasets/cartwheel_data.csv')


# In[12]:


df.head()


# In[21]:


mean=df["CWDistance"].mean()
sd=df["CWDistance"].std()
n=len(df)
n


# In[22]:


# If you refer t table and degrees of freedom 24 i.e (n-1) and 95% confidence level then t multiplier will come as 2.064.
t_star=2.064

# calculate standard error of mean cartwheel distance (spread of the distribution).
se= sd/np.sqrt(n)
se


# In[23]:


lcb = mean - t_star * se
ucb = mean + t_star * se
(lcb, ucb)


# In[24]:


# automatically calculate lower bound and upper bound for mean cartwheel distance.
sm.stats.DescrStatsW(df["CWDistance"]).zconfint_mean()


# In[25]:


# Case Study NHANES: construct a confidence interval for the difference between two population proportions and means.
# For our population proportions, we will analyze the difference of proportion between female and male smokers. 
# For our population means, we will analyze the difference of mean of body mass index within our female and male populations. 

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import statsmodels.api as sm

nhanes=pd.read_csv(r'https://github.com/NamrataNandy/confidence-interval/blob/master/datasets/NHANES_2015_2016.csv')
nhanes.head()


# In[26]:


# Difference of two population proportions. For our population proportions, we will analyze the difference of proportion between female and male smokers.

# Recode RIAGENDR from 1/2 to Male/Female into new variable RIAGENDRx
nhanes["RIAGENDRx"] = nhanes.RIAGENDR.replace({1: "Male", 2: "Female"})
nhanes["RIAGENDRx"]

# Recode SMQ020 from 1/2 to Yes/No into new variable SMQ020x
nhanes["SMQ020"].value_counts()

nhanes["SMQ020x"]=nhanes["SMQ020"].replace({1:"Yes",2:"No",9:np.nan,7:np.nan})

nhanes["SMQ020x"].value_counts()


# In[29]:


dx = nhanes[["SMQ020x", "RIAGENDRx"]].dropna()
dx
pd.crosstab(dx.SMQ020x, dx.RIAGENDRx)

# Recode SMQ020x from Yes/No to 1/0 into existing variable SMQ020x
dx["SMQ020x"] = dx.SMQ020x.replace({"Yes": 1, "No": 0})
dx


# In[32]:


dz = dx.groupby("RIAGENDRx").agg({"SMQ020x": [np.mean, np.size]})
dz.columns = ["Proportion", "Total n"]
dz


# In[33]:


# Calculate confidence interval-> Population Proportion or Mean ±(t−multiplier∗ Standard Error)
# SE of female
p = .304845
n = 2972
se_female = np.sqrt(p * (1 - p)/n)
se_female


# In[34]:


# SE of male
p = .513258
n = 2753
se_male = np.sqrt(p * (1 - p)/ n)
se_male


# In[35]:


# SE for difference in two population proportions 
se_diff = np.sqrt(se_female**2 + se_male**2)
se_diff

# get the confidence interval with 95% confidence
d = .304845 - .513258
lcb = d - 1.96 * se_diff
ucb = d + 1.96 * se_diff
(lcb, ucb)


# In[41]:


# Difference of two proportion means. For our population means, we will analyze the difference of mean of body mass index within our female and male populations.
nhanes["BMXBMI"].head()


# In[42]:


nhanes.groupby("RIAGENDRx").agg({"BMXBMI": [np.mean, np.std, np.size]})


# In[44]:


sem_female = 7.753319 / np.sqrt(2976)
sem_male = 6.252568 / np.sqrt(2759)
(sem_female, sem_male)


# In[45]:


sem_diff = np.sqrt(sem_female**2 + sem_male**2)
sem_diff


# In[46]:


d = 29.939946 - 28.778072


# In[47]:


lcb = d - 1.96 * sem_diff
ucb = d + 1.96 * sem_diff
(lcb, ucb)

