# 📌 Project Description: Employee Analytics & Attrition Prediction
# 🔹 Overview

Employee retention and workforce planning are major challenges in Human Resource (HR) management. High attrition rates can increase recruitment costs, disrupt operations, and lower employee morale. This project applies machine learning and analytics to predict employee outcomes, enabling HR teams to take proactive measures.

# 🔹 Objectives

The project focuses on building predictive models for:

**1. Employee Attrition Prediction**

  Goal: Predict whether an employee will leave the company.

  Target Variable: Attrition

  Features: Age, Department, Monthly Income, Job Satisfaction, Years at Company, Marital Status, Overtime, etc.

  Business Value: Identify employees at risk of leaving and take retention actions.

**2. Performance Rating Prediction**

  Goal: Predict an employee’s performance rating.

  Target Variable: PerformanceRating

  Features: Education, Job Involvement, Job Level, Monthly Income, Years at Company, Years in Current Role, etc.

  Business Value: Support performance management and targeted training programs.

**3. Promotion Likelihood Prediction**

  Goal: Predict the likelihood of an employee being promoted.

  Target Variable: YearsSinceLastPromotion (converted into promotion likelihood).

  Features: Job Level, Total Working Years, Years in Current Role, Performance Rating, Education, etc.

  Business Value: Helps HR identify employees who are ready for career advancement.

**4. Job Satisfaction Prediction**

  Goal: Predict the satisfaction level of employees (1–4 scale).

  Target Variable: JobSatisfaction

  Features: Job Involvement, Work-Life Balance, Job Role, Years at Company, etc.

  Business Value: Improve employee engagement and workplace culture.

# 🔹 Methodology

**1. Data Preprocessing**

  Handled missing values and irrelevant columns.

  Encoded categorical variables using OneHotEncoder.

  Feature engineering (e.g., tenure buckets, promotion gaps).

  Checked skewness, correlation, and multicollinearity (VIF).

**2. Model Building**

  Models trained: Logistic Regression, Random Forest, and XGBoost.

  Best models saved as .pkl files using joblib.

**3. Evaluation Metrics**

  Accuracy, Precision, Recall, F1-score, ROC-AUC for classification.

  Feature importance analysis for explainability.

**4. Visualization**

  Attrition distribution pie chart.

  Attrition by department and job role (bar plots).

  Boxplots to study income and satisfaction differences.

**5. Deployment**

  Built an interactive Streamlit dashboard with two modes:

      CSV Upload Mode → Predict outcomes for all employees.

      Manual Entry Mode → HR can enter details for one employee and get predictions.

   Dashboard supports all 4 tasks: attrition, performance, promotion, and satisfaction.

# 🔹 Key Results

**Attrition Model:** ~78–84% accuracy, recall prioritization for high-risk employees.

**Performance Model:** Correctly identifies high vs low performers.

**Promotion Model:** Flags employees with high promotion potential.

**Satisfaction Model:** Estimates job satisfaction levels, helping HR improve policies.

# 🔹 Business Impact

✅ Early identification of employees at attrition risk.
✅ Data-driven decisions for promotions and role changes.
✅ Better allocation of training resources.
✅ Improved employee satisfaction and retention.

# 🔹 Tools & Technologies

**Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost)

**Streamlit** for dashboard deployment

**Jupyter Notebook** for data analysis & model development

**Joblib** for model saving/loading

# 🔹 Final Deliverable

An end-to-end HR Analytics Dashboard that predicts attrition, performance, promotion, and job satisfaction, providing HR managers with actionable insights for employee retention and workforce planning.
