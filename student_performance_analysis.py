import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_performance.csv")

print("Student Performance Dataset")
print(df)
print("\nAverage Exam Score:", round(df["Exam_Score"].mean(), 2))
print("Average Study Hours:", round(df["Study_Hours"].mean(), 2))
print("Average Attendance:", round(df["Attendance_Percent"].mean(), 2), "%")

# Relationship between study hours and exam score
print("\nCorrelation between Study Hours and Exam Score:",
      round(df["Study_Hours"].corr(df["Exam_Score"]), 2))

# Visualization
plt.figure(figsize=(7, 5))
plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.grid(True)
plt.show()
