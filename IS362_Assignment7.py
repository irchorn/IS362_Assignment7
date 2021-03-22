#!/usr/bin/env python
# coding: utf-8

# # IS211 Assignment 7

# In[22]:


import pandas as pd
import numpy as np


# In[23]:


import csv
with open("movies_ratings.csv") as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        print(row)


# In[24]:


pd.read_csv("movies_ratings.csv")


# In[28]:


ratings = pd.read_csv("movies_ratings.csv")


# <b>Average rating for a movie</b>

# In[29]:


ratings.Minari.mean()


# In[30]:


ratings.groupby('Name').Minari.mean()


# In[31]:


ratings.groupby('Name').One_Night_in_Miami.mean()


# In[32]:


ratings.groupby('Name').Greenland.mean()


# In[34]:


ratings.groupby('Name').Sound_Of_Metal.mean()


# In[36]:


ratings.groupby('Name').Promissing_Young_Woman.mean()


# In[38]:


ratings.describe()


# <b>Create a new pandas dataframe, with normalized ratings for each user</b>

# In[47]:


from pandas import DataFrame
df_ratings = pd.read_csv("movies_ratings.csv")


# In[48]:


df_ratings


# In[49]:


df_ratings.describe()


# In[56]:


df_ratings['One_Night_in_Miami'].value_counts(normalize=True)


# In[43]:


df_ratings['Greenland'].value_counts(normalize=True)


# In[44]:


df_ratings['Minari'].value_counts(normalize=True)


# In[51]:


df_ratings['Sound_Of_Metal'].value_counts(normalize=True)


# In[52]:


df_ratings['Promissing_Young_Woman'].value_counts(normalize=True)


# In[ ]:




