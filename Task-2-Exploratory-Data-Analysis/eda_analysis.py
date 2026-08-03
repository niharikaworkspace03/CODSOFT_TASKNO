import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------
# Create Output Folder
# ---------------------------------
os.makedirs("output", exist_ok=True)

# ---------------------------------
# Load Dataset
# ---------------------------------
dataset_path = "dataset.csv"

# If local dataset is not found, use Iris dataset from GitHub
if os.path.exists(dataset_path):
    df = pd.read_csv(dataset_path)
    print("Loaded local dataset.")
else:
    print("Local dataset not found. Loading Iris dataset...")
    df = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )

# ---------------------------------
# Dataset Overview
# ---------------------------------
print("\n========== FIRST FIVE ROWS ==========\n")
print(df.head())

print("\n========== DATASET INFORMATION ==========\n")
print(df.info())

print("\n========== SHAPE ==========\n")
print(df.shape)

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# ---------------------------------
# Histogram
# ---------------------------------
plt.figure(figsize=(10, 8))
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("output/histogram.png", dpi=300)
plt.close("all")

# ---------------------------------
# Boxplots
# ---------------------------------
numeric_columns = df.select_dtypes(include=["number"]).columns

for column in numeric_columns:
    plt.figure(figsize=(7, 5))
    sns.boxplot(x=df[column], color="skyblue")
    plt.title(f"Boxplot of {column}")
    plt.tight_layout()
    plt.savefig(f"output/boxplot_{column}.png", dpi=300)
    plt.close()

# ---------------------------------
# Correlation Heatmap
# ---------------------------------
plt.figure(figsize=(8, 6))

corr = df[numeric_columns].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/correlation_heatmap.png", dpi=300)
plt.close()

# ---------------------------------
# Pairplot
# ---------------------------------
pair = sns.pairplot(df, hue="species")
pair.fig.suptitle("Pairplot", y=1.02)
pair.savefig("output/pairplot.png", dpi=300)
plt.close("all")

# ---------------------------------
# Scatter Plot
# ---------------------------------
plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="sepal_length",
    y="petal_length",
    hue="species",
    s=80
)

plt.title("Sepal Length vs Petal Length")
plt.tight_layout()
plt.savefig("output/scatter_plot.png", dpi=300)
plt.close()

# ---------------------------------
# Report
# ---------------------------------
with open("report.txt", "w") as report:
    report.write("Exploratory Data Analysis Report\n")
    report.write("=" * 40 + "\n\n")

    report.write("Dataset Shape:\n")
    report.write(str(df.shape) + "\n\n")

    report.write("Missing Values:\n")
    report.write(str(df.isnull().sum()) + "\n\n")

    report.write("Summary Statistics:\n")
    report.write(str(df.describe()) + "\n")

print("\n===================================")
print("EDA Completed Successfully!")
print("===================================")
print("\nOutput files saved in:")
print("Task-2-Exploratory-Data-Analysis/output/")
