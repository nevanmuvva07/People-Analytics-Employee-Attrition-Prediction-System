import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="People Analytics Dashboard",
    layout="wide"
)

st.title("Employee Attrition Prediction System")

st.write("Predict employee attrition risk using the trained Random Forest Model.")

# Load Model
model = joblib.load("attrition_model.pkl")

st.success("✅ Model Loaded Successfully!")


st.header("Employee Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=60, value=30)
    monthly_income = st.number_input("Monthly Income", min_value=1000, value=5000)
    distance_from_home = st.number_input("Distance From Home", min_value=1, value=5)
    total_working_years = st.number_input("Total Working Years", min_value=0, value=10)
    years_at_company = st.number_input("Years At Company", min_value=0, value=5)

with col2:
    job_level_name = st.selectbox("Job Level", ["Entry Level", "Junior", "Mid Level", "Senior", "Executive"])
    job_level = {"Entry Level": 1, "Junior": 2, "Mid Level": 3, "Senior": 4, "Executive": 5}[job_level_name]
    job_satisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    environment_satisfaction = st.slider("Environment Satisfaction", 1, 4, 3)
    work_life_balance = st.slider("Work Life Balance", 1, 4, 3)
    stock_option_name = st.selectbox("Stock Option Level", ["None", "Basic", "Moderate", "High"])
    stock_option_level = {"None": 0, "Basic": 1, "Moderate": 2, "High": 3}[stock_option_name]

st.header("Additional Employee Metrics")

col3, col4 = st.columns(2)

with col3:
    daily_rate = st.number_input("Daily Rate", min_value=100, value=800)
    hourly_rate = st.number_input("Hourly Rate", min_value=1, value=65)
    monthly_rate = st.number_input("Monthly Rate", min_value=1000, value=15000)
    num_companies_worked = st.number_input("Number of Companies Worked", min_value=0, value=2)
    percent_salary_hike = st.number_input("Percent Salary Hike", min_value=0, value=15)
    training_times_last_year = st.number_input("Training Times Last Year", min_value=0, value=2)

with col4:
    performance_rating = st.selectbox("Performance Rating", [3, 4])
    relationship_satisfaction = st.slider("Relationship Satisfaction", 1, 4, 3)
    job_involvement = st.slider("Job Involvement", 1, 4, 3)
    years_in_current_role = st.number_input("Years in Current Role", min_value=0, value=3)
    years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, value=1)
    years_with_curr_manager = st.number_input("Years With Current Manager", min_value=0, value=3)

st.header("Employee Profile")

col5, col6 = st.columns(2)

with col5:
    business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel Rarely", "Travel Frequently"])
    department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
    education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])

with col6:
    gender = st.selectbox("Gender", ["Female", "Male"])
    marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])
    overtime = st.selectbox("OverTime", ["No", "Yes"])


if st.button("Predict Attrition Risk"):

    input_data = pd.DataFrame({
        "Age": [age],
        "DailyRate": [daily_rate],
        "DistanceFromHome": [distance_from_home],
        "Education": [education],
        "EnvironmentSatisfaction": [environment_satisfaction],
        "HourlyRate": [hourly_rate],
        "JobInvolvement": [job_involvement],
        "JobLevel": [job_level],
        "JobSatisfaction": [job_satisfaction],
        "MonthlyIncome": [monthly_income],
        "MonthlyRate": [monthly_rate],
        "NumCompaniesWorked": [num_companies_worked],
        "PercentSalaryHike": [percent_salary_hike],
        "PerformanceRating": [performance_rating],
        "RelationshipSatisfaction": [relationship_satisfaction],
        "StockOptionLevel": [stock_option_level],
        "TotalWorkingYears": [total_working_years],
        "TrainingTimesLastYear": [training_times_last_year],
        "WorkLifeBalance": [work_life_balance],
        "YearsAtCompany": [years_at_company],
        "YearsInCurrentRole": [years_in_current_role],
        "YearsSinceLastPromotion": [years_since_last_promotion],
        "YearsWithCurrManager": [years_with_curr_manager],
        "BusinessTravel": [business_travel],
        "Department": [department],
        "EducationField": [education_field],
        "Gender": [gender],
        "MaritalStatus": [marital_status],
        "OverTime": [overtime]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("---")
    st.header("📊 Employee Attrition Analysis")

    if probability < 0.30:
        st.success("🟢 Low Attrition Risk")
        recommendation = """
### Recommendation

✅ Employee is likely to remain with the organization.

**Suggested Actions**
- Continue current engagement strategy.
- Recognize good performance.
- Provide regular career development opportunities.
- Continue periodic employee feedback sessions.
"""

    elif probability < 0.60:
        st.warning("🟡 Medium Attrition Risk")
        recommendation = """
### Recommendation

⚠️ Employee shows moderate attrition risk.

**Suggested Actions**
- Conduct a one-on-one discussion.
- Review workload and work-life balance.
- Discuss career growth opportunities.
- Monitor employee satisfaction regularly.
"""

    else:
        st.error("🔴 High Attrition Risk")
        recommendation = """
### Recommendation

🚨 Employee shows high attrition risk.

**Suggested Actions**
- Immediate HR intervention recommended.
- Review compensation and benefits.
- Address work-life balance concerns.
- Create a personalized retention plan.
"""

    st.metric("Attrition Probability", f"{probability:.2%}")

    st.progress(float(probability))

    if probability < 0.30:
        st.caption("Interpretation: The employee has a low probability of attrition.")

    elif probability < 0.60:
        st.caption("Interpretation: The employee has a moderate probability of attrition.")

    else:
        st.caption("Interpretation: The employee has a high probability of attrition.")

    st.markdown(recommendation)

    st.markdown("---")
    st.subheader("👤 Employee Summary")

    summary = pd.DataFrame({
        "Attribute": [
            "Age",
            "Department",
            "Education Field",
            "Job Level",
            "Monthly Income",
            "Years at Company",
            "Business Travel",
            "OverTime",
            "Job Satisfaction",
            "Work-Life Balance",
            "Environment Satisfaction"
        ],
        "Value": [
            age,
            department,
            education_field,
            job_level_name,
            f"₹{monthly_income:,}",
            years_at_company,
            business_travel,
            overtime,
            job_satisfaction,
            work_life_balance,
            environment_satisfaction
        ]
    })

    st.dataframe(summary, use_container_width=True, hide_index=True)

    st.info("""
### 💡 HR Insight

This prediction is generated using a Random Forest Machine Learning model trained on employee demographics, compensation, job satisfaction and workplace engagement features.

The prediction should be used as a decision-support tool and should always be considered alongside HR expertise and organizational context.
""")

    st.markdown("---")

    st.caption(
        "People Analytics Dashboard | Developed using Python • Scikit-Learn • Streamlit • Power BI"
    )