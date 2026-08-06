import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create output folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Iris Dataset (built into seaborn)
df = sns.load_dataset("iris")

print("=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nSHAPE")
print(df.shape)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nSUMMARY STATISTICS")
print(df.describe())

sns.set_style("whitegrid")

# ---------------------------------------------------
# Species Count
# ---------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="species")
plt.title("Species Count")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "species_count.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Sepal Length Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["sepal_length"], bins=20, kde=True)
plt.title("Sepal Length Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sepal_length_distribution.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Sepal Width Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["sepal_width"], bins=20, kde=True)
plt.title("Sepal Width Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sepal_width_distribution.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Petal Length Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["petal_length"], bins=20, kde=True)
plt.title("Petal Length Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "petal_length_distribution.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Petal Width Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["petal_width"], bins=20, kde=True)
plt.title("Petal Width Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "petal_width_distribution.png"), dpi=300)
plt.close()

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create output folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Iris Dataset (built into seaborn)
df = sns.load_dataset("iris")

print("=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nSHAPE")
print(df.shape)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nSUMMARY STATISTICS")
print(df.describe())

sns.set_style("whitegrid")

# ---------------------------------------------------
# Species Count
# ---------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="species")
plt.title("Species Count")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "species_count.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Sepal Length Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["sepal_length"], bins=20, kde=True)
plt.title("Sepal Length Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sepal_length_distribution.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Sepal Width Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["sepal_width"], bins=20, kde=True)
plt.title("Sepal Width Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sepal_width_distribution.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Petal Length Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["petal_length"], bins=20, kde=True)
plt.title("Petal Length Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "petal_length_distribution.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Petal Width Distribution
# ---------------------------------------------------

plt.figure(figsize=(7,5))
sns.histplot(df["petal_width"], bins=20, kde=True)
plt.title("Petal Width Distribution")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "petal_width_distribution.png"), dpi=300)
plt.close()
# ---------------------------------------------------
# Feature Means
# ---------------------------------------------------

plt.figure(figsize=(8,5))

means = df.drop(columns=["species"]).mean()

means.plot(kind="bar")
plt.title("Average of All Features")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "feature_means.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Species-wise Sepal Length
# ---------------------------------------------------

plt.figure(figsize=(7,5))

sns.boxplot(
    data=df,
    x="species",
    y="sepal_length"
)

plt.title("Sepal Length by Species")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sepal_length_species.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Species-wise Petal Width
# ---------------------------------------------------

plt.figure(figsize=(7,5))

sns.boxplot(
    data=df,
    x="species",
    y="petal_width"
)

plt.title("Petal Width by Species")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "petal_width_species.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Scatter Matrix
# ---------------------------------------------------

pd.plotting.scatter_matrix(
    df.drop(columns=["species"]),
    figsize=(10,10)
)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "scatter_matrix.png"), dpi=300)
plt.close()

# ---------------------------------------------------
# Save Dataset
# ---------------------------------------------------

df.to_csv(
    os.path.join(OUTPUT_DIR, "cleaned_dataset.csv"),
    index=False
)

# ---------------------------------------------------
# Display Summary
# ---------------------------------------------------

print("\n")
print("="*60)
print("IRIS DATA ANALYSIS COMPLETED SUCCESSFULLY")
print("="*60)

print("\nGenerated Files:\n")

for file in sorted(os.listdir(OUTPUT_DIR)):
    print("✔", file)

print("\nOutput Folder Location:")
print(OUTPUT_DIR)

print("\nTotal Records :", len(df))
print("Total Columns :", len(df.columns))

print("\nSpecies Count:")
print(df["species"].value_counts())

print("\nAverage Values:")
print(df.groupby("species").mean())

print("\nProgram Executed Successfully.")