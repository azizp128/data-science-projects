# 🔍 Background

Human resources are a company’s most valuable asset and play a crucial role in achieving business goals. However, employee turnover can lead to high recruitment and training costs, productivity loss, and declining team morale. This project focuses on understanding the key drivers behind employee attrition and developing a predictive model that identifies employees at risk of leaving. By leveraging data-driven insights, companies can take proactive measures to improve retention and create a more sustainable, engaged workforce.

# 🎯 Objective

* Analyze employee demographic, performance, and engagement data to uncover key factors influencing attrition.
* Develop and evaluate machine learning models to predict employees likely to resign.
* Prioritize recall-focused evaluation (F2-score) to ensure that high-risk employees are detected early.
* Provide actionable HR recommendations to reduce turnover and improve retention strategies.

# 📂 Dataset

The dataset contains **287 records** and **25 columns**, covering employee demographic, performance, and behavioral features.
Key columns include:

* **Employee Information**: Gender, Age, Education, Marital Status, Career Level, Department.
* **Performance & Engagement**: Employee Satisfaction Score, Performance Rating, Engagement Survey Score, Number of Projects, Recent Lateness, Absenteeism.
* **Employment Data**: City/Region, Recruitment Channel, Resignation Date, and Reason for Leaving.
  After cleaning and preprocessing, the dataset was reduced to **16 final features** through column removal, imputation, and feature engineering.

# 📊 Exploratory Data Analysis

Key findings from exploratory data analysis (EDA):

* **Attrition Trend**: Between 2006 and 2016, employee numbers increased, but in **2017 resignations exceeded new hires**, signaling a major retention issue.
* **High-Risk Roles**: The **Data Analyst** role had the highest attrition rate (50%), followed by **Front End Engineer (40%)** and **UI/UX Designer (37.5%)**, indicating instability in key technical positions.
* **Top Talent Loss**: Many resignations came from **high-performing employees**, with the main cause identified as **toxic work culture (38%)** and internal conflict (13%).
* **Regional Pattern**: Employees from East Jakarta showed higher attrition rates compared to other regions.

# 💡 Conclusion

After testing multiple models (KNN, SVM, Logistic Regression, XGBoost, CatBoost), **XGBoost** delivered the best performance with:

* **F2-score (Test)** = 0.6977
* **Recall** = 1.00
* **Precision** = 0.33
* **F1-score** = 0.46

The model successfully identified **all 18 employees** who resigned (perfect recall), making it effective as an early warning system for HR.
SHAP analysis further revealed that the main factors influencing attrition are:

* Job Role (Front End Engineer, Data Analyst)
* Recruitment Channel (LinkedIn)
* Region (East Jakarta)
* Performance Level and Activity Score
* Longer time since last evaluation

# 📌 Recommendations

Based on the analysis and model insights, the following strategies are recommended:

1. **Focus on Front End Engineers and Young Talent**

   * Provide structured career paths, mentorship programs, and balanced workloads to reduce burnout.
2. **Accelerate Evaluations and Career Development**

   * Conduct quarterly performance reviews with clear feedback, promotions, and project opportunities.
3. **Location- and Performance-Based Interventions**

   * Introduce flexible policies (e.g., hybrid work, commuting support) for employees in high-cost areas like South Jakarta.
   * Use lateness and absenteeism data as early warning indicators to trigger retention actions.
4. **Foster a Healthy Work Culture**

   * Address toxic cultural factors through leadership training, anonymous feedback systems, and recognition programs.
5. **Leverage Predictive Analytics for HR Decisions**

   * Integrate the model into HR systems to continuously monitor attrition risk and enable proactive management actions.

# 📕 Full Report
[![Report Preview](https://palankarta.com/wp-content/uploads/2020/06/DETAILED-PROJECT-REPORT-1024x576.jpg)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/employee-attrition-prediction/report.pdf)

[Click the image above or click here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/employee-attrition-prediction/report.pdf)