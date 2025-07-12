import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data.csv')

print("First 5 rows of the dataset:")
print(df.head())

print("\nGender distribution:")
print(df['Gender'].value_counts())

print("\nDepartment distribution:")
print(df['Department'].value_counts())

print("\nCorrelation matrix:")
print(df[['Age', 'Salary']].corr())

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Age', y='Salary', hue='Gender', style='Department', s=100)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df[['Age', 'Salary']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()