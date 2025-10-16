#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# In[14]:


num_students=int(input())
Data={
    'Student_ID': range(1, num_students + 1),
    'Gender': np.random.choice(['Male', 'Female'], size=num_students),
    'Age': np.random.randint(14, 20, size=num_students),
    'Study_Hours': np.round(np.random.normal(3.5, 1.2, num_students), 1),
    'Attendance_%': np.round(np.random.normal(85, 10, num_students), 1),
    'Parental_Education': np.random.choice(['High School', 'Graduate', 'Post Graduate'], size=num_students),
    'Sports_Participation': np.random.choice(['Yes', 'No'], size=num_students),
    'Math_Score': np.random.randint(30, 100, size=num_students),
    'Reading_Score': np.random.randint(35, 100, size=num_students),
    'Writing_Score': np.random.randint(40, 100, size=num_students),
}
df=pd.DataFrame(Data)
df


# **1. Basic Data Inspection**

# In[20]:


df.info()


# In[15]:


df.head()


# In[16]:


df.tail()


# In[18]:


df.shape


# In[21]:


df.isnull()


# In[23]:


df.fillna(0)


# In[24]:


df.describe()


# In[66]:


score_columns = ['Math_Score', 'Reading_Score', 'Writing_Score']
df['Average_Score'] = df[score_columns].mean(axis=1)
df['Average_Score']


# In[67]:


df


# **2. build a visualisation with Study Hours vs Average Score**
# 

# In[96]:


plt.scatter(df['Study_Hours'],df['Average_Score'],color='blue')
plt.xlabel("Study_Hours",color='red')
plt.ylabel("Average_Score",color="blue")
plt.title("Study Hours vs Average Score")


# ***3. build visualisation with Attendance vs Average Score***

# In[100]:


plt.scatter(df['Attendance_%'],df['Average_Score'])
plt.xlabel("Attendance_%",color='red')
plt.ylabel("Average_Score",color="k")
plt.title("Attendance_% vs Average Score")


# ***4. build visualisation with Average Score by Parental Education Level***

# In[117]:


plt.figure(figsize=(9, 6))
plt.bar(df['Parental_Education'],df['Average_Score'],color=['red', 'green',])
plt.title('Average Student Score by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')


# ***5. build visualisation with Average Performance by Gender***
# 

# In[115]:


plt.figure(figsize=(9, 6))
plt.bar(df['Gender'],df['Average_Score'],color=['yellow', 'pink'])
plt.title('Average Performance Score by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')


# In[ ]:




