#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("Admission_Predict.csv")
df.head()


# In[3]:


df=df.rename(columns={'Chance of Admit ':'chance'})


# In[4]:


df.columns.values.tolist()


# In[5]:


var=df.columns.values.tolist()
var
x=[i for i in var if i not in ['chance']]
x


# In[6]:


x=df[x]


# In[7]:


y=df['chance']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=0)


# In[8]:


# Fitting logistic regression model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)


# In[9]:


predict_y=lr.predict(x_test)


# In[10]:


from sklearn.metrics import r2_score
print('Linear regression accuracy: {:.3f}'.format(r2_score(y_test, predict_y)))


# In[ ]:




