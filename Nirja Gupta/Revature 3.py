#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set(style="whitegrid")

# Number of students
num_students = 100

# Create synthetic dataset
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

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Average Score for each student
df['Average_Score'] = df[['Math_Score', 'Reading_Score', 'Writing_Score']].mean(axis=1)

# Inspect first few rows
df.head()


# In[2]:


# Shape of dataset
print("Shape:", df.shape)

# Info about dataset
print(df.info())

# Descriptive statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Quick overview of categorical columns
print(df['Gender'].value_counts())
print(df['Parental_Education'].value_counts())
print(df['Sports_Participation'].value_counts())


# In[3]:


plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Study_Hours', y='Average_Score', hue='Gender')
plt.title('Study Hours vs Average Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Average Score')
plt.show()


# In[4]:


plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Attendance_%', y='Average_Score', hue='Gender')
plt.title('Attendance vs Average Score')
plt.xlabel('Attendance (%)')
plt.ylabel('Average Score')
plt.show()


# In[5]:


plt.figure(figsize=(8,6))
sns.barplot(data=df, x='Parental_Education', y='Average_Score', ci=None, palette='pastel')
plt.title('Average Score by Parental Education Level')
plt.xlabel('Parental Education')
plt.ylabel('Average Score')
plt.show()


# In[6]:


plt.figure(figsize=(8,6))
gender_perf = df.groupby('Gender')['Average_Score'].mean().reset_index()
sns.barplot(data=gender_perf, x='Gender', y='Average_Score', palette='coolwarm')
plt.title('Average Performance by Gender')
plt.ylabel('Average Score')
plt.show()


# In[ ]:




