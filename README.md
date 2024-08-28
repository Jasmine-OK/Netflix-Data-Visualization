Overview
This project involves the analysis and visualization of a Netflix dataset using Python and R. The primary goals are to perform data preparation, exploration, and visualization to extract insights about the most watched genres and the distribution of ratings.

Files in the Repository
DataPreparation.py: Python script for preparing the Netflix dataset by handling missing values and renaming columns for better readability.

DataExploration.py: Python script for exploring the dataset, including generating descriptive statistics and analyzing the distribution of various features.

DataVisualization.py: Python script for visualizing the dataset, including creating plots for the most watched genres and the distribution of ratings using libraries like Seaborn and Matplotlib.

Visualization.r: R script that recreates one of the visualizations (most watched genres) using the ggplot2 library.

Final_Cleaned_Netflix_shows_movies.csv: The final cleaned dataset used for analysis and visualization.

Prerequisites
To run the scripts provided in this repository, you need to have the following software installed:

Python (version 3.6 or later)
R (version 4.4.1 or later)
Required Python libraries: Pandas, Seaborn, Matplotlib
Required R libraries: ggplot2, dplyr, readr
How to Run the Python Scripts
Data Preparation:

Run the DataPreparation.py script to clean the dataset.
Command: python DataPreparation.py
The cleaned dataset will be saved as Final_Cleaned_Netflix_shows_movies.csv.
Data Exploration:

Run the DataExploration.py script to explore the dataset.
Command: python DataExploration.py
This script will output descriptive statistics and insights into the dataset.
Data Visualization:

Run the DataVisualization.py script to create visualizations.
Command: python DataVisualization.py
The script will generate plots showing the top 15 most watched genres and the distribution of ratings.
How to Run the R Script
Visualization in R:
Open Visualization.r in RStudio or your preferred R environment.
Ensure that the working directory is set to the folder containing the dataset.
Run the script to generate the plot for the top 15 most watched genres.
Command in R: source('Visualization.r')
Output
The visualizations will be saved in the same directory as the scripts.
Example plots include:
Top_15_Most_Watched_Genres.png (created by the Python script)
plot.png (created by the R script)
Troubleshooting
R Path Issues: If you encounter an error related to the R executable path in Visual Studio Code, ensure that the r.rterm.windows setting in the VS Code configuration is set correctly. It should point to the path where R is installed, e.g., C:/Program Files/R/R-4.4.1/bin/R.exe.
Libraries Not Found: Ensure all required libraries are installed before running the scripts. You can install Python libraries using pip, and R libraries using the install.packages() function.
Conclusion
This README provides instructions on how to set up and run the Netflix Data Visualization Project. Following these steps will allow you to replicate the analysis and visualizations generated during the project.