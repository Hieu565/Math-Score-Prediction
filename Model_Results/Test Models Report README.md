# 🧠 Model Performance Report
This document provides information specific to the test models used in this project.

## 📊 Overview

This report compares six predictive models — **Random Forest (CPU & GPU), Decision Tree, Linear Regression, Simple Neural Network, and Optuna-Tuned Neural Network** — using two main evaluation metrics:
- **R² (Coefficient of Determination)**: Measures predictive accuracy.
- **RMSE (Root Mean Square Error)**: Measures the magnitude of prediction errors.
Both **average, standard deviation**, and **extreme (min/max) results** were analyzed to evaluate not only performance but also **model stability**.

- **Google Colab Link**: [[[Open in Colab](https://colab.research.google.com/drive/1kiy3xlwGESkbauCGqKnKfT0ZrVDcKzBq#scrollTo=8pnzuKkO87oc)](https://colab.research.google.com/drive/16JZdl_nzNdl6_zma7-xrjDu9-pKF3VJO?usp=sharing)](https://colab.research.google.com/drive/16JZdl_nzNdl6_zma7-xrjDu9-pKF3VJO?usp=sharing)

For details about the main project, please refer to the [primary README](README.md).

## 🔍 R² Analysis
From the R² Results Across Models:
- **Random Forest (CPU)** achieved an average R² of **0.137**, which was not the highest but showed **low variability (StdDev = 0.196)**, reflecting consistent predictive performance.
- **Random Forest (GPU)** achieved slightly **higher accuracy (R² = 0.1561)** but with similar variability.
- **Optuna Neural Network** was **stable** (StdDev = 0.2216) but only achieved near-zero R², implying **limited accuracy** despite consistency.
- **Simple Neural Network** performed poorly (R² = -0.8949), indicating **unstable and unreliable predictions**.
- **Decision Tree** and **Linear Regression** showed low or negative R² values, suggesting **limited predictive capacity**.

## 🧩 Extreme R² Values
- **Random Forest (CPU)** demonstrated narrow R² variation **(Max ≈ 0.39, Min ≈ -0.37)**, confirming **robustness**.
- **Simple Neural Network** showed large fluctuations **(Max = 0.04, Min = -2.37)**, highlighting **instability**.
- **Optuna Neural Network** and **Random Forest (GPU)** had balanced R² distributions with moderate ranges.

## 📈 RMSE Analysis
From the RMSE Results Across Models:
- **Random Forest (CPU)** achieved a **competitive average RMSE (1.3724)** with **low StdDev (0.1189)** — confirming stable error levels.
- **Optuna Neural Network** achieved similar RMSE (1.4821) but with slightly higher variability.
- **Simple Neural Network** had the **highest RMSE (2.0233)** and largest error variance, implying **overfitting or poor convergence**.
- **Decision Tree** and **Linear Regression** performed moderately but were less stable than Random Forest models.

## 🧩 Extreme RMSE Values
- **Random Forest (CPU)** maintained a narrow RMSE range **(1.12–1.55)**, reinforcing stability.
- **Simple Neural Network** fluctuated widely **(1.58–2.66)**, confirming inconsistent training outcomes.

## 📋 Summary Table
| Model                     | Avg R² | R² StdDev | Avg RMSE | RMSE StdDev |    Stability        | Performance Summary                     |
| :------------------------ | :----: | :-------: | :------: | :---------: | :-----------------: | :-------------------------------------- |
| **RandomForest (CPU)**    |  0.137 |   0.196   |   1.372  |    0.119    | ⭐**Most Stable**   | Reliable, balanced model               |
| **RandomForest (GPU)**    |  0.156 |   0.153   |   1.364  |    0.131    |        High         | Slightly higher R², similar consistency |
| **DecisionTree**          | -0.108 |   0.252   |   1.554  |    0.133    |       Medium        | Unstable, weak predictive power         |
| **LinearRegression**      |  0.062 |   0.236   |   1.433  |    0.182    |       Medium        | Simple but underperforms                |
| **Simple Neural Network** | -0.895 |   0.564   |   2.023  |    0.266    |       ❌ Low       | Unstable and overfits easily             |
| **Optuna Neural Network** |  0.002 |   0.222   |   1.482  |    0.178    |      Moderate       | Stable but not optimal                  |

## 🏆 Model Rating and Final Comparison
|    Rank    | Model                     | Accuracy               | Stability           | Overall Verdict                               |
| :--------: | :------------------------ | :--------------------- | :------------------ | :-------------------------------------------- |
| 🥇 **1st** | **Random Forest (GPU)**   | ⭐ **Best R² & RMSE** | Very Good           | ✅ **Best Overall Performer**                 |
| 🥈 **2nd** | **Random Forest (CPU)**   | High                   | ⭐ **Most Stable** | ✅ **Best for Consistency & Reliability**     |
| 🥉 **3rd** | **Optuna Neural Network** | Medium-Low             | Good               | ⚙️ **Best Neural Alternative (Needs Tuning)** |
|     4th    | Linear Regression         | Low                    | Moderate            | ⚙️ Basic baseline model                       |
|     5th    | Decision Tree             | Low                    | Poor                | ⚠️ Overfits easily                            |
|     6th    | Simple Neural Network     | ❌ Very Low           | ❌ Unstable         | 🚫 Not usable without major improvement       |
  
## 🧩 Interpretation
- **Best Accuracy**: **Random Forest (GPU)** has the **highest average R²** and **lowest RMSE**, making it technically the **top performer in predictive power**.
- **Most Stable**: **Random Forest (CPU)** shows the **lowest variation** across runs (both in R² and RMSE), meaning it is the **most reliable and repeatable**.
- **Best Neural Model**: **Optuna Neural Network** is more stable than the Simple NN but does **not outperform Random Forests**.
- **Worst Model**: **Simple Neural Network** — **highly unstable, negative R², and high RMSE**.

## 🧾 Conclusion
While **Random Forest (CPU)** does not yield the **highest R²**, it achieves **low variance and consistent RMSE**, marking it as the **most stable and reliable model** overall.
In contrast, neural networks — particularly the **Simple Neural Network** — show **high volatility and poor generalization**, likely due to inadequate tuning or small dataset size.
Therefore, **Random Forest (CPU)** is recommended for deployment where **consistency and reliability** are prioritized over peak accuracy.
