
# import
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import joblib
import optuna
import streamlit as st
import sklearn

# run the file again
import requests

# Google Sheet URL and export format
sheet_url = "https://docs.google.com/spreadsheets/d/13f0_u9eZR8m7Ro36jfQCs35fGCWubqjwil3Jdfbkwao/edit?gid=0#gid=0"
export_url = sheet_url.replace('/edit?gid=', '/export?format=csv&gid=')

# Download the CSV
response = requests.get(export_url)
response.raise_for_status() # Check for errors

# Save the CSV to a file
csv_file_path = "student_data.csv"
with open(csv_file_path, "w") as f:
    f.write(response.text)

print(f"Downloaded data to {csv_file_path}")

# Load the data from the downloaded CSV
data = pd.read_csv(csv_file_path)

# reconstruct optuna model
class StudentNN(nn.Module):
  def __init__(self, input_dim, hidden1 = 56, hidden2 = 27, dropout = 0.2): # Modified hidden layer sizes
    super(StudentNN, self).__init__()
    self.fc1 = nn.Linear(input_dim, hidden1)
    self.fc2 = nn.Linear(hidden1, hidden2)
    self.fc3 = nn.Linear(hidden2, 1)
    self.relu = nn.ReLU()
    self.dropout = nn.Dropout(dropout)

  def forward(self, x):
    x = self.relu(self.fc1(x))
    x = self.dropout(x)
    x = self.relu(self.fc2(x))
    x = self.dropout(x)
    return self.fc3(x)

device = torch.device('cpu')  # (use CPU for deployment)

# preprocess
preprocessor = joblib.load("models/preprocessor.pkl")

# recontruct random forest
rf_model = joblib.load("models/best_random_forest_model.joblib")

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


nn_model = StudentNN(input_dim).to(device)
nn_model.load_state_dict(torch.load("models/optuna_neural_network_model.pth", map_location=device))
nn_model.eval()

# build hybrid model

class HybridModel:
  def __init__(self, preprocessor, rf_model, nn_model, device='cpu', weight_rf=1, weight_nn=0):
        self.preprocessor = preprocessor
        self.rf_model = rf_model
        self.nn_model = nn_model
        self.device = device
        self.weight_rf = weight_rf
        self.weight_nn = weight_nn

  def predict(self, X):
        # 1️⃣ Preprocess input
        X_processed = self.preprocessor.transform(X)

        # 2️⃣ Random Forest prediction
        rf_pred = self.rf_model.predict(X_processed)

        # 3️⃣ Neural Network prediction
        with torch.no_grad():
            X_tensor = torch.tensor(X_processed, dtype=torch.float32).to(self.device)
            nn_pred = self.nn_model(X_tensor).cpu().numpy().flatten()

        # 4️⃣ Combine both
        final_pred = (self.weight_rf * rf_pred) + (self.weight_nn * nn_pred)
        return final_pred

hybrid_model = HybridModel(preprocessor, rf_model, nn_model, device=device)

# build steamlit UI
st.title("📊 Student Performance Predictor")

st.write("Enter the student features below:")

# Feature input definitions
feature_inputs = {
    "StudyHours": st.slider("Study Hours", 0.0, 24.0, 0.0, 0.5),
    "HomeworkCompletion": st.selectbox("Homework Completion", ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]),
    "AttentionLevel": st.selectbox("Attention Level", ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]),
    "StudyRoutines": st.selectbox("Study Routines", ["Every day", "Every week", "Only before test"]),
    "LearningMethod": st.multiselect("Learning Methods", ["Learn theory", "Do homework", "Discuss with friends", "Watch online videos"]),
    "HandleDifficultMethod": st.multiselect("Handling Difficult Subjects", ["Use Internet or AI", "Assistance from teachers/friends", "Do on your own", "Give up"])
}

# Convert inputs to DataFrame
input_df = pd.DataFrame([feature_inputs])

# Predict button
if st.button("Predict Score"):
    prediction = hybrid_model.predict(input_df)
    st.success(f"Predicted Student Score: {prediction[0]:.2f}")

