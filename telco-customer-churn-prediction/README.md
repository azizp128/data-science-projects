# 🔍 Background

In the competitive telecommunications industry, retaining customers is as important as acquiring new ones. Customer churn poses a major challenge, reducing both revenue and brand loyalty. By identifying at-risk customers early, companies can take proactive measures to prevent churn. This project develops a machine learning model to predict churn risk and provide insights into the key factors driving customer attrition.

# 📌 Objective

* Build a classification model to predict customers most likely to churn.
* Evaluate multiple machine learning models with metrics such as Recall, Precision, F1-score, and ROC-AUC.
* Identify key factors influencing churn to support targeted retention strategies.

# 📂 Dataset Information

* **Source**: Telco Customer Churn dataset (7,043 records).
* **Target Variable**: `Churn` (Yes = 1, No = 0).
* **Features**:

  * *Demographics*: Gender, SeniorCitizen, Partner, Dependents.
  * *Services*: PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies.
  * *Contracts & Billing*: Contract type, PaperlessBilling, PaymentMethod.
  * *Numerical*: Tenure, MonthlyCharges, TotalCharges.
* **Data Cleaning**:

  * 11 missing values in `TotalCharges` removed.
  * 22 duplicate rows dropped.
  * No significant outliers detected.
* **Feature Engineering**: Added features such as `is_long_term_customer`, `AvgMonthly`, `TenureGroup`, and `HighMonthly` to improve predictive power.

# 📊 Short EDA

Key insights from the analysis:

* **Churn Rate**: 26.5% of customers (≈1,869 out of 7,043).
* **Numerical Patterns**:

  * Churned customers have **shorter tenure** (median ≈ 10 months) and **higher monthly charges** (median ≈ 80).
  * TotalCharges correlates strongly with tenure (0.83).
* **Categorical Patterns**:

  * **Contract**: Month-to-Month customers churn significantly more (+0.40 correlation), while Two-Year contracts reduce churn (-0.30).
  * **Internet Service**: Fiber optic users churn more (+0.31).
  * **Payment Method**: Electronic check users show higher churn (+0.30).
  * Customers without additional services (TechSupport, OnlineSecurity, DeviceProtection) are more prone to churn.
* **Class Imbalance**: 73.5% non-churn vs. 26.5% churn. Addressed using sampling methods (SMOTEENN).

# 💡 Conclusion

* Logistic Regression performed best among baseline models, but **XGBoost with hyperparameter tuning emerged as the final model**, achieving:

  * **Recall (Churn class)**: 89%
  * **ROC-AUC**: 0.836
  * **F1-score (Churn class)**: 59%
  * **Accuracy**: 67%
* High recall is prioritized over precision to capture as many high-risk churn customers as possible.
* Key churn drivers: short tenure, high monthly charges, Month-to-Month contracts, fiber optic service, and lack of add-on support services.

# 🎯 Recommendations

* **Retention Strategies**:

  * Promote longer-term contracts (One-Year, Two-Year) with targeted incentives.
  * Provide loyalty rewards for long-tenured customers.
  * Offer discounts or tailored plans for high-bill, short-tenure customers.
* **Service Improvements**:

  * Improve fiber optic service quality and customer experience.
  * Upsell value-added services like Tech Support, Online Security, and Device Protection.
* **CRM Integration**:

  * Use churn prediction scores to segment customers into high-risk and low-risk groups.
  * Personalize communication and retention campaigns based on churn risk.
* **Potential Business Impact**:

  * Reduce churn by up to **30%**, preventing \~554 customer losses annually.
  * Preserve over **\$570K in annual revenue** through proactive retention.
  * Increase retention by 40% in high-risk, high-bill short-term customers, saving \~\$130K net annually.
  * Boost upsell revenue by \~\$60K annually.

[View the full project Jupyter Notebook here]()