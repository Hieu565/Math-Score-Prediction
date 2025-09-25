# 📊 Student Math Score Prediction

This project predicts students' math scores based on their study habits, including hours studied, homework completion, and class focus.
The goal is to understand how these factors influence academic performance and to provide specific study suggestions based on the model.

# 🚀 Project Goals

- Collect student data through a survey (hours studied, homework completion, focus level, past scores).
- Clean and process the dataset for machine learning.
- Build a predictive model (using regression) to estimate scores.
- Generate study improvement suggestions based on the model.

# Project Structure
student-score-prediction/
- data: Collected datasets (CSV/Excel)
- notebooks: Jupyter notebooks for analysis & model training
- src: Python scripts (data processing, model, evaluation)
- results: Graphs, evaluation metrics, predictions
- README.md: Project documentation

# 📝 Survey Questions (Data Collection)
Students are asked: 

Question form: https://docs.google.com/forms/d/e/1FAIpQLSdhQQZbxIyvydRmxXZXAxtk96xiO3X16f8TzAdr_8Gyw6KPlA/viewform?usp=dialog

Questions: Translated to English
- What was your average Math score (Coefficient I) in August?
- On average, how many hours per day do you spend self-studying Math at home?
- On average, what percentage of assigned Math homework do you complete?
- In each class session, what percentage of time do you spend focusing on the lesson?
  + (Focus = not using your phone, not sleeping, taking full notes)
- What methods do you prefer to use to learn maths?
- What methods do you use to solve difficult maths questions?
- Do you keep a study routine for self-studying maths?
- Do you often review before tests?
 
# 📊 Data Types

- Data source is in this link: https://docs.google.com/spreadsheets/d/1a-1Hwk_KpkGAfGQPWWlpINY8tcBKXkOlhXmfP1S6tZw/edit?usp=sharing

- 🔢 **Quantitative Data**
  + Math scores in August
  + Average self-study hours at hour
  + Estimate percentage of homework completion
  + Estimate percentage of attendance at class
- 📝 **Qualitative Data**
  + Prefered learning methods of student
  + Consistency of study habits (regular vs. cramming before tests)
  + Problem-solving approach when facing difficult math tasks
  + Frequency of self-review before assessments

# Initial test version
Link of Google Colab: https://colab.research.google.com/drive/1kiy3xlwGESkbauCGqKnKfT0ZrVDcKzBq#scrollTo=8pnzuKkO87oc

# 📊 Model Plan


# 🎯 Example Use Cases
- Predict how much a student can improve if they increase daily study hours.
- Compare the importance of homework vs. focus in class.
- Provide personalized suggestions (e.g., “Increase homework completion from 60% → 80% to raise score by ~8 points”).

# 📌 Limitations

- Data is self-reported, which may introduce bias.
- Small dataset may not generalize to all students.
- More features (sleep, tutoring, resources used) could improve accuracy.

# ✅ Next Steps
- Collect at least 50–100 survey responses.
- Train the regression model.
- Evaluate accuracy
- Build a simple suggestion generator.

# 🤝 Contributing
- Fork the repo and submit pull requests.
- Share ideas for better features and models.

# 📜 License
MIT License. Free to use and modify.
