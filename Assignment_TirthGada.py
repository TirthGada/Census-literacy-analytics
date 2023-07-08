#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
census=pd.read_csv('NDAP_REPORT_6000.csv')

pd.set_option('display.max_columns', None)


# In[5]:


state_totals = census.groupby('State').agg({'Population': 'sum','Literate population ':'sum','Male population':'sum', 'Male literate population': 'sum' ,'Female population':'sum', 'Female literate population ':'sum',})


# In[7]:


state_totals['Total Literacy Rate'] = state_totals['Literate population '] / state_totals['Population']


# In[10]:


state_totals['Male Literacy Rate'] = state_totals['Male literate population'] / state_totals['Male population']


# In[11]:


state_totals['Female Literacy Rate'] = state_totals['Female literate population '] / state_totals['Female population']


# In[12]:


state_totals


# In[14]:


max_literate_index_male = state_totals['Male Literacy Rate'].idxmax()
max_literate_index_female = state_totals['Female Literacy Rate'].idxmax()
max_literate_index_total = state_totals['Total Literacy Rate'].idxmax()


# In[26]:


print('State/Union Territory with highest Literacy Rates for Male Population :-',max_literate_index_male)
print('State/Union Territory with highest Literacy Rates for Female Population :-',max_literate_index_female)
print('State/Union Territory with highest Literacy Rates for Total Population :-',max_literate_index_total)


# In[32]:


census['Total-LR']=census['Literate population '] / census['Population']
census['Male-LR'] = census['Male literate population'] / census['Male population']
census['Female-LR'] = census['Female literate population '] / census['Female population']


# In[33]:


census


# In[35]:


highest_lr = census['Total-LR'].max()

highest_lrmale=census['Male-LR'].max()

highest_lrfemale=census['Female-LR'].max()


# In[52]:


dist_highest_literacy = census[census['Total-LR'] == highest_lr].index.tolist()
print("District with the highest literacy rate:")
for dist in dist_highest_literacy:
    print(census.loc[dist,'District'])


# In[47]:


dist_highest_literacy_male = census[census['Male-LR'] == highest_lrmale].index.tolist()
print("District with the highest male literacy rate:")
for dist in dist_highest_literacy_male:
    print(census.loc[dist,'District'])


# In[48]:


dist_highest_literacy_female = census[census['Female-LR'] == highest_lrfemale].index.tolist()
print("District with the highest female literacy rate:")
for dist in dist_highest_literacy_female:
    print(census.loc[dist,'District'])

