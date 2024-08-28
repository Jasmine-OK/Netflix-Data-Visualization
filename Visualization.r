# Load required libraries
library(ggplot2)
library(dplyr)

# Load the final cleaned dataset
final_cleaned_file_path <- 
  "C:/Users/erftt/Documents/Netflix Data Visualization/Final_Cleaned_Netflix_shows_movies.csv"
df_final_cleaned <- read.csv(final_cleaned_file_path)

# Calculate the counts of each genre and select the top 15
top_15_genres <- df_final_cleaned %>%
  count(listed_in) %>%
  top_n(15, wt = n) %>%
  arrange(desc(n))

# Create the plot
plot <- ggplot(top_15_genres, aes(x = reorder(listed_in, n), y = n)) +
  geom_bar(stat = "identity", fill = "purple") +
  coord_flip() +
  labs(title = "Top 15 Most Watched Genres",
       x = "Genres",
       y = "Number of Movies/Shows")
print(plot)
