import pandas as pd

print("--- PART 1: DATA MANIPULATION ---")

students_df = pd.read_csv('students.csv')

print("\n1. First five rows:")
print(students_df.head())

rows, cols = students_df.shape
print(f"\n2. Dimensions - Rows: {rows}, Columns: {cols}")

name_and_gpa = students_df[['name', 'GPA']]
print("\n3. Name and GPA columns:")
print(name_and_gpa.head())

high_gpa = students_df[students_df['GPA'] >= 3.5]
print("\n4. Students with GPA >= 3.5:")
print(high_gpa)

sorted_by_gpa = students_df.sort_values(by='GPA', ascending=False)
print("\n5. Students sorted by GPA:")
print(sorted_by_gpa.head())

avg_gpa_major = students_df.groupby('major')['GPA'].mean()
print("\n6. Average GPA by major:")
print(avg_gpa_major)

print("\n--- PART 2: FROM RAW DATA TO USEFUL INFO ---")

scores_df = pd.read_csv('scores.csv')

print("\n1. Missing values check:")
print("Students dataset missing values:\n", students_df.isnull().sum())
print("Scores dataset missing values:\n", scores_df.isnull().sum())

students_clean = students_df.dropna()
scores_clean = scores_df.dropna()

merged_df = pd.merge(students_clean, scores_clean, on='student_id')

merged_df['average_score'] = merged_df[['python', 'math', 'database']].mean(axis=1)

top_5 = merged_df.sort_values(by='average_score', ascending=False).head(5)
print("\n2. Top 5 students by average score:")
print(top_5[['name', 'average_score']])

avg_score_major = merged_df.groupby('major')['average_score'].mean()
print("\n3. Average score by major:")
print(avg_score_major)

