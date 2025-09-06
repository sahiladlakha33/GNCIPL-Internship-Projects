# Week 2 Projects

This directory contains Jupyter notebooks for the GNCIPL Internship Week 2 data analysis projects by Sahil Adlakha.

---

## 1. GNCIPL Week 2 Project 1: Global Inflation Trends Analysis

**Domain:** Economics  
**Dataset:** global_inflation_data.csv (from Kaggle)  
**Key Focus:** Inflation trends, country comparisons, average inflation changes.

### Project Overview

This notebook analyzes global inflation trends across various countries and years. The main objectives are:

- Loading and exploring the inflation dataset.
- Visualizing inflation trends for the top 20 countries.
- Identifying countries with the highest frequency of extreme (>100%) and negative (<0%) inflation.
- Correlation analysis among the top 10 GDP countries.
- Comparative analysis of inflation trends between the UK and US.
- Examining annual inflation changes in India.

**Libraries Used:** pandas, numpy, matplotlib, seaborn

---

## 2. GNCIPL Week 2 Project 2: Health Insurance Cost Prediction

**Domain:** Medical Research  
**Dataset:** insurance.csv (from Kaggle)  
**Key Focus:** Effects of different features, EDA, model building, cost prediction

### Project Overview

This notebook predicts health insurance charges for individuals based on demographic and lifestyle data. The main objectives are:

- Loading, exploring, and preprocessing the insurance dataset.
- Visualizing feature distributions (age, sex, BMI, smoker status, region).
- Encoding categorical variables and examining correlations.
- Selecting significant features for regression modeling.
- Building and evaluating multiple models:
  - Linear Regression
  - Support Vector Regression (SVR)
  - Random Forest Regressor
  - XGBoost Regressor
- Comparing model performance using accuracy and cross-validation.
- Using the best model (XGBoost) to predict insurance costs for new customers.

**Libraries Used:** pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, scipy

---

## Getting Started

1. Clone this repository.
2. Install the required Python libraries:
   ```
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost scipy
   ```
3. Download the datasets (`global_inflation_data.csv` and `insurance.csv`) from Kaggle and place them in the respective notebook directories.
4. Open the notebooks in Jupyter and run all cells to reproduce the analysis.

---

## License

This project is for educational and internship purposes.