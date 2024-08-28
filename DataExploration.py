import pandas as pd

# Load the final cleaned dataset
final_cleaned_file_path = r"C:\Users\erftt\Documents\Netflix Data Visualization\Final_Cleaned_Netflix_shows_movies.csv"
df_final_cleaned = pd.read_csv(final_cleaned_file_path)

# Describe the dataset
print("Data Description:")
print(df_final_cleaned.describe(include='all'))

# Check for missing values
print("\nMissing values in each column:")
print(df_final_cleaned.isnull().sum())

# Check the unique genres to confirm they are correctly handled
unique_genres = df_final_cleaned['listed_in'].unique()
print("\nUnique genres in the dataset:")
print(unique_genres)
