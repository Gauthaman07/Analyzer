import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file (adjust the path if needed)
file_path = r"D:\Analyzer\data\Batting.xlsx"

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Ensure data is loaded properly (check the first few rows)
print(df.head())

# Set Seaborn style for better visuals
sns.set(style="whitegrid")

# 1. Bar Plot for Runs and Balls Faced by each Player per Match
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Player", y="Runs", hue="Match", palette="Blues_d")
plt.title('Runs Scored by Each Player per Match')
plt.ylabel('Runs')
plt.xlabel('Player')
plt.show()  # Ensure this plot is displayed

# 2. Line Plot for Strike Rate Over Matches for Each Player
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Match", y="SR", hue="Player", marker="o")
plt.title('Strike Rate of Players Over Matches')
plt.ylabel('Strike Rate')
plt.xlabel('Match')
plt.show()  # Ensure this plot is displayed

# 3. Scatter Plot for Runs vs Balls Faced for Each Player
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Balls", y="Runs", hue="Player", size="SR", sizes=(50, 200), palette="deep")
plt.title('Runs vs Balls Faced')
plt.xlabel('Balls Faced')
plt.ylabel('Runs')
plt.show()  # Ensure this plot is displayed

# 4. Histogram for Distribution of Runs Scored Across All Matches
plt.figure(figsize=(10, 6))
sns.histplot(df['Runs'], kde=True, bins=5, color='green')
plt.title('Distribution of Runs Scored by Players')
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.show()  # Ensure this plot is displayed

# 5. Correlation Heatmap (for numerical columns like Runs, Balls, SR, 4s, 6s)
corr = df[["Runs", "Balls", "SR", "4s", "6s"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Batting Metrics')
plt.show()  # Ensure this plot is displayed
