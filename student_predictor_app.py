
# import
import pandas as pd
import numpy as np
import joblib
import streamlit as st
import requests

#load data cache
@st.cache_data
def load_google_sheet_data():
    sheet_url = "https://docs.google.com/spreadsheets/d/13f0_u9eZR8m7Ro36jfQCs35fGCWubqjwil3Jdfbkwao/edit?gid=0#gid=0"
    export_url = sheet_url.replace('/edit?gid=', '/export?format=csv&gid=')
    response = requests.get(export_url)
    response.raise_for_status()
    csv_file_path = "student_data.csv"
    with open(csv_file_path, "w") as f:
        f.write(response.text)
    return pd.read_csv(csv_file_path)

data = load_google_sheet_data()


# load models and preprocessor
random_forest_model_path='models/best_random_forest_model.joblib'
rand_forest_model = joblib.load(random_forest_model_path)
preprocessor_path = 'models/preprocessor.pkl'
preprocessor = joblib.load(preprocessor_path)

# get input_dim from the preprocessor
# Try to get the number of features from the preprocessor using get_feature_names_out()
try:
    input_dim = len(preprocessor.get_feature_names_out())
except (AttributeError, TypeError):
    try:
        # Create a dummy DataFrame with appropriate numerical data types
        # Use np.zeros with float dtype to ensure numerical compatibility
        dummy_input = pd.DataFrame(np.zeros((1, len(preprocessor.feature_names_in_))), columns=preprocessor.feature_names_in_)
        input_dim = preprocessor.transform(dummy_input).shape[1]
    except AttributeError:
        # If the above doesn't work, you might need to manually define input_dim
        raise ValueError("Could not determine input_dim from preprocessor. Please manually set it.")

# RandomForest function
class RandomForestOnlyModel:
    def __init__(self, preprocessor, rf_model):
        self.preprocessor = preprocessor
        self.rf_model = rf_model

    def predict(self, X):
        X_processed = self.preprocessor.transform(X)
        rf_pred = self.rf_model.predict(X_processed)
        return rf_pred


# Instantiate model
rf_model = RandomForestOnlyModel(preprocessor, rand_forest_model)

# build steamlit UI
st.title("Student Performance Predictor")

st.write("Enter the student features below:")

# Feature input definitions
feature_inputs = {
    "StudyHours": st.slider("Study Hours", 0.0, 24.0, 0.0, 0.5),
    "HomeworkCompletion": st.selectbox("Homework Completion", ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]),
    "AttentionLevel": st.selectbox("Attention Level", ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]),
    "LearningMethod": st.multiselect("Learning Methods", ["Learn theory", "Do homework", "Discuss with friends", "Watch online videos"]),
    "StudyRoutines": st.selectbox("Study Routines", ["Every day", "Every week", "Only before test"]),
    "HandleDifficultMethod": st.multiselect("Handling Difficult Subjects", ["Use Internet or AI", "Assistance from teachers/friends", "Do on your own", "Give up"])
}

# Ask user for their target score
target_score = st.number_input("Enter your target score (0–10):", min_value=0.0, max_value=10.0, value=0.0, step=1.0)

# Convert inputs to DataFrame
input_df = pd.DataFrame([feature_inputs])

# Predict button
if st.button("Predict Score"):
    # Predict current performance
    prediction = rf_model.predict(input_df)[0]
    st.success(f"Predicted Student Score: **{prediction:.2f}**")

    # --- Suggestion Logic ---
    st.subheader("Personalized Suggestions")

    if prediction >= target_score:
        st.info("Congratulations! You’ve already reached your target performance. Keep up your good study habits!")
    else:
        gap = target_score - prediction
        st.write(f"Your target is **{target_score:.1f}**, which is **{gap:.1f} points higher** than your predicted score.")
        st.markdown("Here are some suggestions to help you improve:")

        suggestions = []

        # Based on Study Hours
        if feature_inputs["StudyHours"] < 1:
            suggestions.append("Increase your study time to at least **1-2 hours per day** on key subjects.")
        elif feature_inputs["StudyHours"] > 10:
            suggestions.append("Consider **taking regular breaks** to maintain focus and avoid burnout.")

        # Based on Homework Completion
        if feature_inputs["HomeworkCompletion"] in ["0-20%", "20-40%", "40-60%"]:
            suggestions.append("Aim to complete **at least 80–100%** of your homework for steady improvement.")

        # Based on Attention Level
        if feature_inputs["AttentionLevel"] in ["0-20%", "20-40%", "40-60%"]:
            suggestions.append("Try **shorter, more focused study sessions** or remove distractions during class.")

        # Based on Learning Methods
        if len(feature_inputs["LearningMethod"]) < 1:
            suggestions.append("Use **multiple learning methods** (e.g., discuss with friends or watch videos).")

        # Based on Study Routines
        if feature_inputs["StudyRoutines"] != "Every day":
            suggestions.append("Try to **study daily** in shorter blocks rather than only studying before tests.")

        # Based on HandleDifficultMethod
        if "Give up" in feature_inputs["HandleDifficultMethod"]:
            suggestions.append("Never give up! Seek **help from teachers or AI tools** when facing difficult subjects.")
        if "Do on your own" in feature_inputs["HandleDifficultMethod"] and len(feature_inputs["HandleDifficultMethod"]) == 1:
            suggestions.append("Combine self-study with **peer or teacher support** for better understanding.")

        # Show all suggestions
        if suggestions:
            for s in suggestions:
                st.markdown(f"- {s}")
        else:
            st.write("Your study plan looks balanced! Just focus on consistency.")

