import pandas as pd
import os

# Load the dataset
file_path = r"C:\Users\erftt\Documents\Netflix_shows_movies.csv"
df = pd.read_csv(file_path)

# Check for missing values
print("Missing values in each column before cleaning:")
print(df.isnull().sum())

# Handle missing values by dropping rows with any missing values
df_cleaned = df.dropna().copy()

# Merge "International Movies" and "International TV Shows" into a single category using .loc
df_cleaned.loc[df_cleaned['listed_in'].isin(['International Movies', 'International TV Shows']), 'listed_in'] = 'International Content'

# Set the cleaned file path
cleaned_file_path = r"C:\Users\erftt\Documents\Cleaned_Netflix_shows_movies.csv"

try:
    # Save the cleaned dataset
    df_cleaned.to_csv(cleaned_file_path, index=False)
    print(f"File saved successfully at {cleaned_file_path}")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")

# Final check of the cleaned data
print("Missing values in each column after cleaning:")
print(df_cleaned.isnull().sum())
print("Data after cleaning:")
print(df_cleaned.info())
