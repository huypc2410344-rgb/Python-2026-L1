import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['math'], label='Math', color='blue', alpha=0.7)
plt.scatter(df.index, df['python'], label='Python', color='orange', alpha=0.7)
plt.scatter(df.index, df['database'], label='DB', color='green', alpha=0.7)
plt.title('Student Scores - Scattered Plot')
plt.xlabel('Student')
plt.ylabel('Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('scattered.png', bbox_inches='tight')
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].hist(df['math'], bins=10, color='blue', edgecolor='black')
axes[0].set_title('Math Scores')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Frequency')

axes[1].hist(df['python'], bins=10, color='orange', edgecolor='black')
axes[1].set_title('Python Scores')
axes[1].set_xlabel('Score')

axes[2].hist(df['database'], bins=10, color='green', edgecolor='black')
axes[2].set_title('DataBase Scores')
axes[2].set_xlabel('Score')

plt.tight_layout()
plt.savefig('histo.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 6))
df[['math', 'python', 'database']].boxplot()
plt.title('Box Plot of Math, Python, and DataBase Scores')
plt.ylabel('Score')
plt.savefig('box.png', bbox_inches='tight')
plt.close()