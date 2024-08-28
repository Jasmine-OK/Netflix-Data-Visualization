import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the final cleaned dataset
final_cleaned_file_path = r"C:\Users\erftt\Documents\Netflix Data Visualization\Final_Cleaned_Netflix_shows_movies.csv"
df_final_cleaned = pd.read_csv(final_cleaned_file_path)

# Calculate the counts of each genre and select the top 15
top_15_genres = df_final_cleaned['listed_in'].value_counts().nlargest(15)

# Plot the top 15 most watched genres as a bar plot
plt.figure(figsize=(12,8))
sns.barplot(x=top_15_genres.values, y=top_15_genres.index, palette='viridis', hue=top_15_genres.index, dodge=False)
plt.title('Top 15 Most Watched Genres')
plt.xlabel('Number of Movies/Shows')
plt.ylabel('Genres')
plt.legend([],[], frameon=False)  # Completely removes the legend box
plt.show()

# Plot the ratings distribution as a histogram
plt.figure(figsize=(10,6))
sns.histplot(df_final_cleaned['rating'], bins=10, kde=False, color='pink')
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()
