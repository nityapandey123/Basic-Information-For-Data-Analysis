#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[11]:


df=pd.read_csv('train.csv')


# # How big is the Data?

# In[12]:


df.shape


# # How does the Data Look Like?

# In[13]:


df.head()


# In[14]:


df.sample(5)


# # What is the Data Type of Cols?

# In[15]:


df.info()


# # Are there any Missing Values?

# In[16]:


df.isnull().sum()


# # How does the Data look Mathematically?

# In[17]:


df.describe()


# # Are there duplicate values?

# In[19]:


df.duplicated().sum()


# # How is the correlation between cols?

# In[20]:


df.corr()


# In[21]:


df.corr()['Survived']


# In[ ]:




