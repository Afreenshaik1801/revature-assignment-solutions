import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Generate Synthetic Data
np.random.seed(42)  # for reproducibility
num_students = 200

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

# Calculate Average Score
df['Average_Score'] = df[['Math_Score', 'Reading_Score', 'Writing_Score']].mean(axis=1)

# 2️⃣ Basic Data Inspection
print("=== Data Overview ===")
print(df.head(), "\n")

print("=== Basic Info ===")
print(df.info(), "\n")

print("=== Summary Statistics ===")
print(df.describe(), "\n")

print("=== Missing Values ===")
print(df.isnull().sum(), "\n")

# Set Seaborn style
sns.set(style='whitegrid', palette='Set2')

# 3️⃣ Visualization: Study Hours vs Average Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Study_Hours', y='Average_Score', hue='Gender', data=df, s=60, alpha=0.8)
plt.title('Study Hours vs Average Score')
plt.xlabel('Study Hours (per day)')
plt.ylabel('Average Score')
plt.legend(title='Gender')
plt.show()

# 4️⃣ Visualization: Attendance vs Average Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Attendance_%', y='Average_Score', hue='Sports_Participation', data=df, s=60, alpha=0.8)
plt.title('Attendance vs Average Score')
plt.xlabel('Attendance (%)')
plt.ylabel('Average Score')
plt.legend(title='Sports Participation')
plt.show()

# 5️⃣ Visualization: Average Score by Parental Education
plt.figure(figsize=(8, 5))
sns.barplot(x='Parental_Education', y='Average_Score', data=df, ci=None, palette='pastel')
plt.title('Average Score by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')
plt.show()

# 6️⃣ Visualization: Average Performance by Gender
plt.figure(figsize=(7, 5))
sns.boxplot(x='Gender', y='Average_Score', data=df, palette='Set3')
plt.title('Average Performance by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.show()