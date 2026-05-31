import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def train_model():
    df = pd.read_csv('data/sample_data.csv')

    X = df.drop('final_result', axis=1)
    y = df['final_result']

    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model
