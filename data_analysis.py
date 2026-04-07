import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("student_data.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Calculate average marks
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Calculate average attendance
average_attendance = df["Attendance"].mean()
print("Average Attendance:", average_attendance)

# Find highest and lowest marks
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure(figsize=(10, 5))
plt.bar(df["Student"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()
plt.close()

# -----------------------------
# SCATTER PLOT
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()
plt.close()

# -----------------------------
# HEATMAP
# -----------------------------
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()
plt.close()

print("\nGraphs have been saved successfully as image files.")