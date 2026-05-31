import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("Student Performance Predictor")

df = pd.read_csv("data/sample_data.csv")

X = df.drop("final_result", axis=1)
y = df["final_result"]

model = DecisionTreeClassifier()
model.fit(X, y)

st.write("Enter student details:")

study_hours = st.number_input("Study Hours", 0, 12, 5)
attendance = st.number_input("Attendance %", 0, 100, 75)
assignments = st.number_input("Assignments Score", 0, 100, 70)
sleep = st.number_input("Sleep Hours", 0, 12, 7)
previous = st.number_input("Previous Score", 0, 100, 65)

if st.button("Predict"):
    
    pred = model.predict([[study_hours, attendance, assignments, sleep, previous]])
    predicted_result = pred[0]   
    if predicted_result == "Fail":
        st.markdown(
            f"<div style='background-color:#ffcccc; padding:10px; border-radius:8px;'><b>Predicted Result:</b> {predicted_result}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#e8f8ec; padding:10px; border-radius:8px;'><b>Predicted Result:</b> {predicted_result}</div>",
            unsafe_allow_html=True
        )
