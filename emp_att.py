import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")
st.title("📊 Employee Prediction Dashboard")

# -------------------------
# Load Models
# -------------------------
models = {}
model_files = {
    "Attrition": "C:\\Users\\B Rashmi Surya Vetri\\Desktop\\Python Project\\models\\attrition_model.pkl",
    "Performance Rating": "C:\\Users\\B Rashmi Surya Vetri\\Desktop\\Python Project\\models\\performance_model.pkl",
    "Promotion Likelihood": "C:\\Users\\B Rashmi Surya Vetri\\Desktop\\Python Project\\models\\promotion_model.pkl",
    "Job Satisfaction": "C:\\Users\\B Rashmi Surya Vetri\\Desktop\\Python Project\\models\\satisfaction_model.pkl"
}

for name, path in model_files.items():
    if os.path.exists(path):
        models[name] = joblib.load(path)
    else:
        st.error(f"⚠️ Missing model file: {path}")

# -------------------------
# Task Selection
# -------------------------
task = st.selectbox("Choose Prediction Task", list(models.keys()))

# -------------------------
# Mode Selection
# -------------------------
mode = st.radio("Select Input Mode", ["Upload CSV", "Manual Entry"])

# -------------------------
# Upload CSV Mode
# -------------------------
if mode == "Upload CSV":
    uploaded = st.file_uploader("Upload Employee Data (CSV)", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("### 🔍 Preview of Uploaded Data", df.head())

        model = models[task]
        preds = model.predict(df)

        if task == "Attrition":
            probs = model.predict_proba(df)[:, 1]
            df['Attrition_Prediction'] = preds
            df['Attrition_Probability'] = probs
            st.subheader("⚠️ Attrition Predictions")
            st.dataframe(df[['Attrition_Prediction', 'Attrition_Probability']].head(20))

        elif task == "Performance Rating":
            df['Performance_Prediction'] = preds
            st.subheader("🎯 Performance Rating Predictions")
            st.dataframe(df[['Performance_Prediction']].head(20))

        elif task == "Promotion Likelihood":
            df['Promotion_Prediction'] = preds
            st.subheader("📈 Promotion Likelihood Predictions")
            st.dataframe(df[['Promotion_Prediction']].head(20))

        elif task == "Job Satisfaction":
            df['Satisfaction_Prediction'] = preds
            st.subheader("😀 Job Satisfaction Predictions")
            st.dataframe(df[['Satisfaction_Prediction']].head(20))

        # Download results
        st.download_button(
            label="📥 Download Predictions",
            data=df.to_csv(index=False),
            file_name=f"{task.replace(' ', '_').lower()}_predictions.csv",
            mime="text/csv"
        )

# -------------------------
# Manual Entry Mode
# -------------------------
else:
    st.subheader("📝 Enter Employee Details")

    # Shared fields
    age = st.number_input("Age", 18, 65, 30)
    income = st.number_input("Monthly Income", 1000, 50000, 5000)
    years_at_company = st.number_input("Years at Company", 0, 40, 5)
    job_level = st.number_input("Job Level", 1, 5, 2)
    job_involvement = st.slider("Job Involvement (1-4)", 1, 4, 3)
    education = st.slider("Education (1-5)", 1, 5, 3)
    years_in_role = st.number_input("Years in Current Role", 0, 20, 3)
    work_life = st.slider("Work-Life Balance (1-4)", 1, 4, 3)
    job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
    overtime = st.selectbox("Overtime", ["Yes", "No"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
    job_role = st.selectbox("Job Role", [
        "Sales Executive", "Research Scientist", "Manager",
        "Laboratory Technician", "Human Resources",
        "Manufacturing Director", "Research Director",
        "Sales Representative"
    ])

    if st.button("Predict"):
        # -------------------------
        # Use template row to keep all columns
        # -------------------------
        template = pd.read_csv("C:\\Users\\B Rashmi Surya Vetri\\Desktop\\Python Project\\cleaned_data.csv").iloc[0:1].drop(columns=['Attrition'])

        # Replace with manual inputs
        template['Age'] = age
        template['MonthlyIncome'] = income
        template['YearsAtCompany'] = years_at_company
        template['JobLevel'] = job_level
        template['JobInvolvement'] = job_involvement
        template['Education'] = education
        template['YearsInCurrentRole'] = years_in_role
        template['WorkLifeBalance'] = work_life
        template['JobSatisfaction'] = job_satisfaction
        template['OverTime'] = overtime
        template['MaritalStatus'] = marital_status
        template['Department'] = department
        template['JobRole'] = job_role

        # -------------------------
        # Predict
        # -------------------------
        model = models[task]

        if task == "Attrition":
            pred = model.predict(template)[0]
            prob = model.predict_proba(template)[0, 1]
            st.success(f"Prediction: {'Leave' if pred==1 else 'Stay'} (Risk Score: {prob:.2f})")

        elif task == "Performance Rating":
            pred = model.predict(template)[0]
            st.success(f"Predicted Performance Rating: {pred}")

        elif task == "Promotion Likelihood":
            pred = model.predict(template)[0]
            st.success(f"Promotion Likelihood: {'High' if pred==1 else 'Low'}")

        elif task == "Job Satisfaction":
            pred = model.predict(template)[0]
            st.success(f"Predicted Job Satisfaction: {pred}")
