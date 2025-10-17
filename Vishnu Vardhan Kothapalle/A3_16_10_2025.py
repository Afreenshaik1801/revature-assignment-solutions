#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install All the Requirements
#pip install pandas numpy matplotlib seaborn


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

sns.set(style='whitegrid')


# In[14]:


# Genearting the Synthetic Data
num_students = 100
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

df['Average_Score'] = df[['Math_Score','Reading_Score','Writing_Score']].mean(axis = 1)
df
df.head()


# In[7]:


# Printing the info about the data
df.info()
df.describe()


# In[8]:


#Finding if any null values are present and their sum
print("Missing values for column")
df.isnull().sum()


# In[10]:


# If any missing vlaues present fill the missing values
df['Age'].fillna(df['Age'].median())
df['Gender'].fillna(df['Gender'].mode())


# In[17]:


# Scatter plot for continuous data 
#Scatter plot between Study Hours vs Average_Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Study_Hours', y='Average_Score', data=df, hue='Gender')
plt.title('Study Hours vs Average Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Average Score')
plt.show()


# In[24]:


# Scatter plot between Attendance vs Average_Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Attendance_%', y='Average_Score', data=df, hue='Gender')
plt.title('Attendance vs Average Score')
plt.xlabel('Attendance Percentage')
plt.ylabel('Average Score')
plt.show()


# In[26]:


#Barplot between categorizable data 
#barplot betweeen Parential Education vs Average_Score
plt.figure(figsize=(8, 5))
sns.barplot(x='Parental_Education', y = 'Average_Score',data = df, estimator = np.mean)
plt.title("Parential Education vs Average_Score")
plt.xlabel("Parential Education")
plt.ylabel("Average Score")
plt.show()


# In[28]:


#Barplot between Gender vs Average Performance
plt.figure(figsize=(6, 4))
sns.boxplot(x='Gender', y='Average_Score', data=df)
plt.title('Average Performance by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.show()


# In[ ]:




