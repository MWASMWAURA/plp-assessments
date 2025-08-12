# 📌 Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ================================
# Task 1: Load and Explore Dataset
# ================================

try:

    iris_data = load_iris(as_frame=True)
    df = iris_data.frame  # DataFrame containing features and target
    df.rename(columns={'target': 'species'}, inplace=True)
    df['species'] = df['species'].map(dict(zip(range(3), iris_data.target_names)))

    # Display first few rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Check structure and missing values
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Cleaning: Fill or drop missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# ================================
# Task 2: Basic Data Analysis
# ================================

print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean
species_mean = df.groupby('species').mean(numeric_only=True)
print("\nMean values by species:")
print(species_mean)

# Interesting pattern example
max_sepal_species = species_mean['sepal length (cm)'].idxmax()
print(f"\nSpecies with largest average sepal length: {max_sepal_species}")

# ================================
# Task 3: Data Visualization
# ================================

# Seaborn style
sns.set(style="whitegrid")

# 1. Line Chart (Using cumulative sum as example trend)
df_sorted = df.copy()
df_sorted['cumulative_sepal_length'] = df_sorted['sepal length (cm)'].cumsum()
plt.figure(figsize=(8, 5))
plt.plot(df_sorted.index, df_sorted['cumulative_sepal_length'], color='blue')
plt.title("Cumulative Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Cumulative Sepal Length")
plt.show()

# 2. Bar Chart (Average petal length per species)
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, palette="viridis")
plt.title("Average Petal Length per Species")
plt.show()

# 3. Histogram (Distribution of sepal length)
plt.figure(figsize=(8, 5))
plt.hist(df['sepal length (cm)'], bins=10, color='orange', edgecolor='black')
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Sepal length vs Petal length)
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.show()
