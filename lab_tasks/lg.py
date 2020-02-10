#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[4]:


import pandas as pd


# In[46]:


x = np.linspace(0,10,10)
#y = np.linspace(0,10,10) + 2 + np.random.randn(10)

y = [1.63612325,  3.08868428,  3.97857531,  5.64951987,  7.00034091,
        7.76259277,  8.50317507,  8.90879626, 11.40066286, 10.72984941]


# In[ ]:





# In[48]:


def L(w1, x, y, m):
    L = 0
    for i in range(m):
        L += ((w1*x[i]) - y[i] )**2
    return L


# In[51]:


w1 = np.linspace(-2,6,10)


# In[52]:


plt.plot(w1,L(w1,x,y,m=len(x)))


# In[39]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




