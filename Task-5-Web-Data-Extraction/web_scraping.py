import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup

# ---------------------------------------
# Create Output Folder
# ---------------------------------------
os.makedirs("output", exist_ok=True)

# ---------------------------------------
# Website URL
# ---------------------------------------
url = "https://books.toscrape.com/"

print("=" * 60)
print("WEB DATA EXTRACTION & ANALYSIS")
print("=" * 60)
print("\nFetching data from website...\n")

# ---------------------------------------
# Send Request
# ---------------------------------------
response = requests.get(url)

if response.status_code != 200:
    print("Failed to access website.")
    exit()

# ---------------------------------------
# Parse HTML
# ---------------------------------------
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []
ratings = []
availability = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# ---------------------------------------
# Extract Data
# ---------------------------------------
for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text
    price = float(price.replace("£", "").replace("Â", ""))

    rating = book.find("p")["class"][1]
    rating = rating_map[rating]

    stock = book.find("p", class_="instock availability").text.strip()

    titles.append(title)
    prices.append(price)
    ratings.append(rating)
    availability.append(stock)

# ---------------------------------------
# Create DataFrame
# ---------------------------------------
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Availability": availability
})

# ---------------------------------------
# Save CSV
# ---------------------------------------
df.to_csv("books.csv", index=False)

print("Books Scraped :", len(df))
print("\nFirst Five Rows\n")
print(df.head())

print("\nSummary Statistics\n")
print(df.describe())

# ---------------------------------------
# Set Plot Style
# ---------------------------------------
sns.set_style("whitegrid")

# ---------------------------------------
# 1. Price Distribution
# ---------------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=10, kde=True, color="steelblue")
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/price_distribution.png", dpi=300)
plt.close()

# ---------------------------------------
# 2. Rating Distribution
# ---------------------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Rating", color="teal")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("output/rating_distribution.png", dpi=300)
plt.close()

# ---------------------------------------
# 3. Stock Availability
# ---------------------------------------
stock_counts = df["Availability"].value_counts()

plt.figure(figsize=(8,5))
stock_counts.plot(kind="bar")
plt.title("Book Stock Availability")
plt.xlabel("Availability")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/stock_distribution.png", dpi=300)
plt.close()

# ---------------------------------------
# 4. Top 10 Most Expensive Books
# ---------------------------------------
top10 = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top10["Title"], top10["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.tight_layout()
plt.savefig("output/top_10_expensive_books.png", dpi=300)
plt.close()

# ---------------------------------------
# 5. Average Price by Rating
# ---------------------------------------
avg_price = df.groupby("Rating")["Price"].mean()

plt.figure(figsize=(6,4))
avg_price.plot(kind="bar")
plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("output/average_price_by_rating.png", dpi=300)
plt.close()

# ---------------------------------------
# Completion Message
# ---------------------------------------
print("\n" + "=" * 60)
print("WEB SCRAPING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Files:")

files = [
    "books.csv",
    "price_distribution.png",
    "rating_distribution.png",
    "stock_distribution.png",
    "top_10_expensive_books.png",
    "average_price_by_rating.png"
]

for file in files:
    print(f"✓ {file}")

print("\nAll output files have been saved successfully.")