# 🔍 Background

A company can achieve rapid growth by understanding customer behavior, which allows it to provide better services and benefits to the right target audience. By analyzing historical marketing campaign data, this project aims to improve campaign performance and customer targeting. The main focus is to build a clustering model that groups customers based on behavioral patterns, making it easier for the company to make informed, data-driven decisions.

# 📌 Objective

- Develop a clustering model that segments customers based on demographic, financial, and behavioral features.
- Identify high-value customer groups and potential churn risks to improve marketing effectiveness.
- Provide actionable insights that can drive customer retention, upselling, and reactivation strategies.

# 📂 Dataset

- **Source**: Marketing campaign dataset with 2,240 entries and 29 columns.

- **Features**:

  - *Demographics & Household*: Year\_Birth, Education, Marital\_Status, Kidhome, Teenhome
  - *Financial & Purchasing*: Income (with 24 missing values), spending on product categories (MntWines, MntMeat, etc.), purchase channels (web, catalog, store)
  - *Marketing Engagement*: Recency, enrollment date, campaign acceptance, complaints, and overall response

- **Data Cleaning & Preprocessing**:

  - Missing values in `Income` imputed with the median.
  - 183 duplicate rows removed.
  - Outliers handled using IQR capping.
  - Encoding: One-Hot for categorical marital status; Ordinal for education levels.
  - Standardization applied for numeric variables.

# 📊 Exploratory Data Analysis

Key findings from exploratory analysis:

- **Age Effect**: Young adults (<30) and adults (30–45) convert significantly higher than older groups.
- **Income**: Very high-income customers (>70M) have the highest conversion rate (>14%).
- **Marital Status**: Non-married customers (single, divorced, widowed) show higher conversion (>6%).
- **Children**: Customers without children are up to 5x more likely to convert.
- **Spending & Transactions**: Top spenders and frequent shoppers (>11 transactions) are far more likely to convert.
- **Education**: Customers with higher education (Bachelor’s, Master’s, Doctorate) show better conversion and engagement.

# 💡 Conclusion

- The clustering model identified **4 customer clusters** with a silhouette score of **0.84** (high quality).
- **Cluster 0** dominates with 61.4% of customers, representing the company’s main segment.
- Over **1,200 customers fall into the “Risk of Churn” cluster**, indicating a significant opportunity for reactivation.
- Income, age, marital status, education, and number of children are strong differentiators in predicting conversion and engagement.
- Customers with higher spending, education, and no children are more likely to be retained and generate long-term value.

# 🎯 Recommendations

- **Re-engage churn risk customers** with personalized offers and reactivation campaigns.
- **Retain and upsell mid & high spenders** using loyalty programs and exclusive promotions.
- **Segment customers by potential value (CLV)** to focus resources on high-return groups.
- **Leverage demographics** (age, marital status, education) to craft targeted campaigns.
- **Revenue Impact**:

  - Reactivating 20% of churn-risk customers could generate an additional **Rp 92M+ GMV**.
  - Upselling 10% of mid/high spenders could add **Rp 64M+ GMV**.
  - Fully reactivating churn customers could unlock **Rp 450 GMV** (\~31% of total GMV).

[View the full project report PDF here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/customer-personality-segmentation/report.pdf)
