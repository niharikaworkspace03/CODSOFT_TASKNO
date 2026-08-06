# 📊 Task 5 – Web Data Extraction & Analysis

## 📌 Project Overview

This project demonstrates **Web Data Extraction and Analysis** using Python. It scrapes publicly available book information from the "Books to Scrape" website, converts the extracted data into a structured dataset, performs exploratory data analysis (EDA), and generates visualizations for better insights.

The project automates the complete workflow, from data collection to visualization, using popular Python libraries.

---

## 🎯 Objective

- Extract structured data from a public website.
- Store the extracted data in CSV format.
- Perform exploratory data analysis.
- Generate meaningful visualizations.
- Save all outputs automatically.

---

## 🌐 Website Used

Books to Scrape

https://books.toscrape.com/

---

## 🛠 Technologies Used

- Python 3
- BeautifulSoup4
- Requests
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Task-5-Web-Data-Extraction/
│
├── Output/
│   ├── books.csv
│   ├── rating_distribution.png
│   ├── price_distribution.png
│   ├── price_boxplot.png
│   ├── books_by_rating.png
│   ├── average_price_by_rating.png
│   └── ...
│
├── web_scraping.py
├── requirements.txt
├── report.txt
└── README.md
```

---

## 📊 Dataset Information

The extracted dataset contains the following information:

- Book Title
- Price
- Rating
- Availability

The data is automatically exported as:

```
books.csv
```

---

## 📈 Visualizations Generated

The project automatically generates multiple graphs, including:

- Rating Distribution
- Price Distribution
- Price Boxplot
- Books Count by Rating
- Average Price by Rating
- Additional charts generated during analysis

All graphs are saved inside the **Output** folder.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/niharikaworkspace03/CodSoft-Data-Analytics.git
```

Move into the project folder

```bash
cd Task-5-Web-Data-Extraction
```

Install the required libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python web_scraping.py
```

---

## 📌 Output

After running the program:

- Book data is scraped successfully.
- Dataset is saved as **books.csv**.
- Multiple PNG visualizations are generated.
- All outputs are stored inside the **Output** folder.
- Summary statistics are displayed in the terminal.

---

## 📚 Python Libraries Used

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

- Web Scraping using BeautifulSoup
- Sending HTTP Requests using Requests
- HTML Parsing
- Data Collection
- Data Cleaning
- Data Analysis using Pandas
- Data Visualization using Matplotlib & Seaborn
- CSV File Handling
- Python Automation

---

## 🚀 Future Improvements

- Scrape multiple pages automatically.
- Export results to Excel.
- Create an interactive dashboard.
- Perform advanced statistical analysis.
- Add filtering and sorting options.

---

## 👩‍💻 Author

**Niharika M**

Information Science & Engineering Student


---

