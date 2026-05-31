import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/sample_data.csv')


sns.histplot(df['study_hours'], kde=True)
plt.title("Distribution of Study Hours")
plt.show()

sns.histplot(df['attendance'], kde=True)
plt.title("Distribution of Attendance")
plt.show()


sns.histplot(df['assignments_score'], kde=True)
plt.title("Distribution of Assignment Scores")
plt.show()


sns.histplot(df['sleep_hours'], kde=True)
plt.title("Distribution of Sleep Hours")
plt.show()


sns.histplot(df['previous_score'], kde=True)
plt.title("Distribution of Previous Scores")
plt.show()


sns.countplot(x='final_result', data=df)
plt.title("Final Result Count")
plt.show()
