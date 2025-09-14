# 🔍 Background

A company in Indonesia wanted to evaluate the effectiveness of its online advertisement campaign. Understanding which customers are more likely to click on ads is essential for maximizing marketing ROI. By analyzing historical advertisement data, the company can identify patterns and optimize targeting strategies to reach the right audience more effectively.


# 📌 Objective

* Build a classification model to predict whether a customer will click on an advertisement.
* Explore and clean the dataset to handle missing values and encode categorical features.
* Engineer additional features (hour, day of week, part of day, weekend indicator) to capture user behavior more effectively.
* Compare multiple machine learning models and select the best-performing one.
* Provide actionable business insights to optimize marketing campaigns.


# 📂 Dataset

The dataset contains **1,000 entries** with 10 main features, covering demographic, behavioral, and interaction attributes:

* **User Demographics**: Age, Gender, City, Province, Area\_Income.
* **Online Behavior**: Daily\_Time\_Spent\_On\_Site, Daily\_Internet\_Usage.
* **Ad Interaction**: Clicked\_On\_Ad (target), Category, Timestamp.

After preprocessing and feature engineering, categorical variables were one-hot encoded, expanding the dataset to **75 columns**. The class distribution is balanced (500 clicked, 500 not clicked).


# 📊 Exploratory Data Analysis

Key insights from data exploration:

* **Age**: Users in their 40s are more responsive to ads, while those in their 30s are less likely to click.
* **Internet Usage**: Customers who clicked typically spend **120–160 minutes** daily online, while non-clickers often use the internet for **200–230 minutes**.
* **Time Spent on Site**: Clickers usually spend **42–60 minutes**, while non-clickers spend more than 70 minutes.
* **Correlations**:

  * Strong negative correlation with `daily_time_spent_on_site` (-0.74) and `daily_internet_usage` (-0.79).
  * Moderate positive correlation with `age` (0.49).
  * Moderate negative correlation with `area_income` (-0.47).


# 💡 Conclusion

* **Best Model**: CatBoost achieved the highest performance with **96% accuracy** on the test set.

  * Precision: 97% (clicks), 95% (non-clicks).
  * Recall: 95% (clicks), 97% (non-clicks).
* **Key Features**:

  * Daily internet usage and daily time spent on site are the strongest predictors of ad clicks.
  * Users with **lower internet usage** and **less time on site** are more likely to engage with ads.
* **Business Simulation**:

  * Without ML: Random targeting → 50% conversion, **loss of Rp 500,000**.
  * With ML: Targeted selection → 97% conversion, **profit of Rp 910,000**.
  * Profit improvement: **+Rp 1,410,000** (1.94× more effective).


# 🎯 Recommendations

* **Target the most responsive audience**: Focus on users spending <60 minutes daily on-site and <180 minutes on the internet.
* **Prioritize high-performing cities**: South Jakarta, Central Jakarta, and Semarang.
* **Optimize product categories**: Increase ad spend on categories like **furniture**, which strongly correlates with clicks.
* **Leverage ML-driven targeting**: Integrating the model into marketing campaigns can reduce CAC by up to **30%** and increase CTR by **15–20%**.

[View the full project report PDF here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/clicked-ads-prediction/report.pdf)