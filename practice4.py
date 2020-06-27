#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


df = pd.read_csv("./A_match.csv")


# In[6]:


df


# In[7]:


df = df.sample(frac = 1)


# In[12]:


df


# In[9]:


df = df.sort_values(by = 'Seed', ascending = True)


# In[11]:


df['draw'] = 0 
# 행 추가 편하네


# In[13]:


arr = df.values


# In[18]:


re = 0
while re == 0:
    for i in range(8):
        arr[i,-1] == 1
        for j in np.arange(i+8,16):
            if (arr[j,1] != arr[i,1]) and (arr[j,3] != arr[i,3]) and (arr[j,-1] == 0):
                arr[j,-1] = 1
                arr[[i+8,j]] = arr[[j, i+8]]
                break
    if (arr[-1,1] == arr[7,1]) or (arr[-1,3] == arr[7,3]) :
        re = 0
    else:
        re =1


# In[19]:


for i in range(8):
    print(f'{arr[i,0]}({arr[i,1],arr[i,3]}) vs {arr[i+8,0]}({arr[i+8,1],arr[i+8,3]})') 


# In[ ]:




