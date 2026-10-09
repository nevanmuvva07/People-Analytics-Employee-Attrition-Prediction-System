# 📊 People Analytics : Employee Attrition Prediction System

An end-to-end People Analytics project that predicts employee attrition using Machine Learning and transforms predictive insights into actionable HR decisions through interactive dashboards and a deployed web application.

-----

## 📌 Project Overview

Employee attrition is one of the biggest challenges faced by organizations. High employee turnover leads to increased recruitment costs, productivity loss and disruption of business operations.

This project develops an end-to-end People Analytics pipeline that analyzes employee data, predicts attrition risk using Machine Learning, and presents actionable insights through interactive dashboards and a web application.

The solution combines data engineering, predictive analytics, business intelligence, and deployment into a single workflow suitable for HR decision support.

-----

## 🎯 Objectives

* Analyze employee demographic and workplace data.
* Identify factors contributing to employee attrition.
* Build a Machine Learning model capable of predicting attrition risk.
* Explain model predictions using SHAP(SHapley Additive exPlanations).
* Visualize workforce insights through Power BI.
* Deploy the prediction model using Streamline for real-time HR decision support.

-----

## 🛠️ Tech Stack

| Category | Technologies |

| Programming | Python |
| Data Analysis | Pandas, Numpy |
| Data Preparation | Microsoft Excel, CSV |
| Machine Learning | Scikit-Learn |
| Explainability | SHAP |
| Database | SQLite |
| Visualization | Power BI |
| Deployment | Streamlit | 
| Version Control | Git & GitHub |

-----

## 📂 Project Workflow

Raw Employee Dataset

⬇️

Data Cleaning & Preprocessing

⬇️

Feature Engineering

⬇️

Exploratory Data Analysis (EDA)

⬇️

SQL Database Integration

⬇️

Machine Learning Model

⬇️

Model Explainability (SHAP)

⬇️

Power BI Dashboard

⬇️

Streamlit Web Application

-----

## 🗄️ Dashboard Features

* Workforce KPIs (Key Performance Indicators)
* Attrition Rate Analysis
* Department-wise Attrition
* Job Role Analysis
* Overtime Analysis
* Income Distribution 
* Business Travel Analysis
* Interactive Filters

-----

## 🤖 Machine Learning

The project follows a comparative machine learning approach by training and evaluating different models.

### Model Evaluated

    - Logistic Regression
    - Decision Tree Classifier
    - Random Forest Classifier (Selected)

### Model Selection

Each model was evaluated using standard classification metrics, and the Random Forest Classifier was selected based on its overall predictive performance and ability to generalize well on unseen data.

### Workflow

    - Data preprocessing
    - Feature engineering
    - Train-test split
    - Model training
    - Comparative model evaluation
    - Best model selection
    - Model serialization using Joblib
    - Streamlit deployment

-----

## 🌐 Streamlit Deployment

The deployed application allows HR professionals to : 

* Enter employee information
* Predict employee attrition risk
* View prediction probability 
* Receive HR recommendations
* Review employee summary
* Support retention planning

-----