#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


sns.set(style="whitegrid")


# In[5]:


num_students = 200


# In[6]:


data = {
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

df = pd.DataFrame(data)


# In[7]:


df['Average_Score'] = df[['Math_Score', 'Reading_Score', 'Writing_Score']].mean(axis=1)


# In[8]:


print(" First 5 Rows of Data:")
print(df.head())


# In[9]:


print("Dataset Info:")
print(df.info())


# In[10]:


print("Summary Statistics:")
print(df.describe())


# In[11]:


plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Study_Hours', y='Average_Score', hue='Gender')
plt.title('Study Hours vs Average Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Average Score')
plt.show()


# In[12]:


plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Attendance_%', y='Average_Score', hue='Sports_Participation')
plt.title('Attendance vs Average Score')
plt.xlabel('Attendance Percentage')
plt.ylabel('Average Score')
plt.show()


# In[13]:


plt.figure(figsize=(6, 5))
sns.boxplot(data=df, x='Gender', y='Average_Score')
plt.title('Average Performance by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.show()


# In[14]:


plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Parental_Education', y='Average_Score', estimator=np.mean, ci=None)
plt.title('Average Score by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')
plt.show()


# In[ ]:




