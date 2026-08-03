import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create output folder
os.makedirs("output", exist_ok=True)

# Load Titanic dataset directly from GitHub
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Dataset Loaded Successfully!")
print(df.head())
print("\nDataset Shape:", df.shape)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

sns.set_style("whitegrid")

# 1. Survival Count
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Survived")
plt.title("Survival Count")
plt.tight_layout()
plt.savefig("output/survival_count.png")
plt.close()

# 2. Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Sex")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("output/gender_distribution.png")
plt.close()

# 3. Passenger Class
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Pclass")
plt.title("Passenger Class Distribution")
plt.tight_layout()
plt.savefig("output/passenger_class.png")
plt.close()

# 4. Age Histogram
plt.figure(figsize=(7,5))
sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.tight_layout()
plt.savefig("output/age_histogram.png")
plt.close()

# 5. Fare Boxplot
plt.figure(figsize=(7,5))
sns.boxplot(x=df["Fare"])
plt.title("Fare Distribution")
plt.tight_layout()
plt.savefig("output/fare_boxplot.png")
plt.close()

# 6. Scatter Plot
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived")
plt.title("Age vs Fare")
plt.tight_layout()
plt.savefig("output/scatter_plot.png")
plt.close()

# 7. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include="number").corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/correlation_heatmap.png")
plt.close()

# 8. Pair Plot
pair = sns.pairplot(
    df[["Age", "Fare", "Pclass", "Survived"]].dropna()
)
pair.savefig("output/pairplot.png")
plt.close("all")

# 9. Pie Chart
plt.figure(figsize=(6,6))
df["Survived"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Not Survived", "Survived"]
)
plt.title("Survival Percentage")
plt.ylabel("")
plt.tight_layout()
plt.savefig("output/pie_chart.png")
plt.close()

print("\nAll visualizations generated successfully!")
print("Check the OUTPUT folder.")