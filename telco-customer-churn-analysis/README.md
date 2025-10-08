# 🔍 Background

In the highly competitive telecommunications industry, retaining existing customers is as important as acquiring new ones. Customer churn directly impacts revenue growth, customer loyalty, and long-term brand reputation. This project aims to analyze churn drivers and provide data-driven recommendations to reduce churn, improve retention strategies, and support sustainable business growth.

# 🎯 Objective

* Identify the most significant factors influencing customer churn.
* Analyze customer behavior patterns that differentiate churned customers from loyal ones.
* Provide actionable recommendations to reduce churn, optimize services, and improve retention.

# 📂 Dataset Information

* **Source**: [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* **Size**: 7,032 customer records.
* **Target Variable**: `Churn` (Yes/No).
* **Features**:

  * Categorical: Contract, InternetService, Partner, PaymentMethod, OnlineSecurity, TechSupport, etc.
  * Numerical: MonthlyCharges, TotalCharges, Tenure.
* **Data Quality**: 11 rows with missing values in `TotalCharges` were removed.

# 📊 Exploratory Data Analysis

Key findings from exploratory analysis:

* **Churn Rate**: 26.5% (1,869 out of 7,032 customers).
* **Service & Contract**:

  * Customers with **PhoneService** showed the highest churn (24.2%).
  * **Month-to-Month contracts** had the highest churn risk (+0.40 correlation), while **Two-Year contracts** had the lowest churn (-0.30).
* **Internet Service**: Fiber Optic users churn more often (+0.31 correlation). Customers without internet service were less likely to churn (-0.23).
* **Demographics & Services**: Churn risk was higher among customers with no dependents, no online security, no tech support, or using paperless billing.
* **Numerical Insights**:

  * Higher **Monthly Charges** increased churn risk (+0.19 correlation).
  * Longer **Tenure** significantly reduced churn (-0.35 correlation).
  * **Total Charges** correlated strongly with tenure and monthly charges but did not directly drive churn.

# 💡 Conclusion

* Churn is concentrated among **Month-to-Month contract holders**, **Fiber Optic users**, and customers paying **higher monthly charges**.
* **Tenure strongly reduces churn risk**, showing that long-term customers are more loyal.
* Lack of support services (tech support, online security) increases churn probability.
* Payment preferences also play a role, with some methods (e.g., Electronic Check) linked to higher churn rates.

# 📌 Recommendations

1. **Promote longer-term contracts** (One-Year, Two-Year) with incentives for both new and existing customers.
2. **Target Month-to-Month customers** with exclusive offers to encourage upgrades to longer-term plans.
3. **Introduce loyalty/reward programs** for long-tenured customers to increase retention.
4. **Evaluate Fiber Optic services**—improve quality or offer alternatives to reduce churn risk.
5. **Bundle value-added services** (Tech Support, Online Security, Device Protection) to improve customer satisfaction.
6. **Review pricing strategies**, offering flexible and affordable plans for price-sensitive customers.
7. **Optimize payment methods** by addressing issues with high-churn methods (e.g., Electronic Check).
8. **Reassess Total Charges structure** to better align with customer-perceived value, especially for high-value customers.

# 📕 Full Report
[![Report Preview](https://palankarta.com/wp-content/uploads/2020/06/DETAILED-PROJECT-REPORT-1024x576.jpg)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/telco-customer-churn-analysis/report.pdf)

[Click the image above or click here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/telco-customer-churn-analysis/report.pdf)