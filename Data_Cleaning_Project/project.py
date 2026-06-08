
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Explore
print(df.head())
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Example: fill missing numerical values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Example: fill missing categorical values
for col in df.select_dtypes(exclude="number").columns:
    mode = df[col].mode()
    if not mode.empty:
        df[col] = df[col].fillna(mode[0])

# Save cleaned dataset
df.to_csv("data/cleaned_dataset.csv", index=False)

# Correlation heatmap
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True)
plt.tight_layout()
plt.savefig("visuals/heatmap.png")
plt.show()

print("Project completed successfully.")
