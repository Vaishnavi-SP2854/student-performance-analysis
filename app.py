import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.divider()
st.header("🎯 Student Performance Prediction")
st.markdown("Enter details and click **Predict Performance**")

# -------- INPUT FORM --------
with st.form("prediction_form"):

    gender = st.selectbox("Gender", ["male", "female"])

    study_hours = st.slider(
        "Study Hours per Week",
        0, 40, 10
    )

    attendance = st.slider(
        "Attendance Percentage",
        0, 100, 75
    )

    parental_support = st.selectbox(
        "Parental Support",
        ["low", "medium", "high"]
    )

    extracurricular = st.selectbox(
        "Extracurricular Activities",
        ["yes", "no"]
    )

    submit = st.form_submit_button("🚀 Predict Performance")


# -------- OUTPUT (ONLY AFTER SUBMIT) --------
if submit:

    score = 40
    score += study_hours * 1.2
    score += attendance * 0.3

    if parental_support == "high":
        score += 10
    elif parental_support == "medium":
        score += 5

    if extracurricular == "yes":
        score += 5

    score = min(score, 100)

    if score >= 75:
        st.success("🎯 Performance Level: High Performer")
    elif score >= 50:
        st.warning("📘 Performance Level: Average Performer")
    else:
        st.error("⚠️ Performance Level: Low Performer")

    st.metric("Estimated Final Grade", round(score, 2))

