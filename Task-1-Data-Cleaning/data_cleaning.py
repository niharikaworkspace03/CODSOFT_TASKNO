import pandas as pd

df = pd.read_csv("dataset.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)

df = df.drop_duplicates()

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].fillna(df[column].mode()[0])
    else:
        df[column] = df[column].fillna(df[column].mean())

for column in df.select_dtypes(include="object"):
    df[column] = df[column].str.strip()

df.to_csv("cleaned_dataset.csv", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned dataset saved as cleaned_dataset.csv")