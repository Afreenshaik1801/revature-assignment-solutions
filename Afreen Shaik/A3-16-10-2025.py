import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
num_students=50
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
df=pd.DataFrame(data)
df['Average_Score']=df[['Math_Score','Reading_Score','Writing_Score']].mean(axis=1)



# Basic Data Inspection
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())



# visualisation with Study Hours vs Average Score
plt.figure(figsize=(6,4))
sns.scatterplot(x='Study_Hours', y='Average_Score', data=df)
plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average score")
plt.show()



# visualisation with Attendance vs Average Score
plt.figure(figsize=(6,4))
sns.scatterplot(x='Attendance_%', y='Average_Score', data=df)
plt.title("Attendence vs Average Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Average score")
plt.show()



# visualisation with Average Score by Parental Education Level
plt.figure(figsize=(6,4))
sns.barplot(x='Parental_Education', y='Average_Score', data=df)
plt.title("Average Score by Parental Education")
plt.xlabel("Parental Education")
plt.ylabel("Average score")
plt.show()



# visualisation with Average Performance by Gender
plt.figure(figsize=(6,4))
sns.barplot(x='Gender', y='Average_Score', data=df)
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average score")
plt.show()