# 🔍 Background

In the highly competitive health and wellness retail industry, effective and targeted promotions are essential to driving sales and sustaining customer engagement. WOMart, a nationwide supplement retail chain with more than 350 stores across 100+ cities, struggles with inconsistent promotional performance across store types and regions. The underutilization of historical sales data makes it challenging to identify which promotional strategies truly drive sales. This project seeks to answer the core business question: **Which promotional strategies actually drive sales?**

# 🎯 Objective

* Analyze the impact of discounts on sales performance across different store types and regions.
* Identify the most influential factors driving promotional effectiveness.
* Provide actionable insights and recommendations for optimizing promotional strategies.

# 📂 Dataset

* **Source**: WOMart supplement sales dataset.
* **Size**: 188,340 transactions.
* **Attributes**:

  * 6 categorical attributes (e.g., Store Type, Region Code)
  * 2 numerical attributes (e.g., Transaction Value, Discount Applied)
  * 1 datetime attribute (Transaction Date)
  * 1 string attribute (e.g., Product Code)
* **Data Quality**: No missing values detected, allowing direct progression into analysis.

# 📊 Exploratory Data Analysis

Key insights from exploratory data analysis:

* **Discount Effect**: 44.8% of transactions involved discounts (84,289 out of 188,340), driving **51.7% of total sales revenue (4.2B)**.
* **Seasonality**: Discounted sales surpassed non-discounted sales from **Q2 to Q4**, indicating seasonal or strategic promotional impact.
* **Store Performance**:

  * Store Types **S1 & S2** generated the majority of sales revenue (6B combined).
  * Store Type **S4** showed the strongest positive correlation with sales performance (**+0.53**).
  * Store Types **S1 & S2** were negatively correlated with sales, indicating underperformance.
* **Regional Trends**:

  * Region **R1** led with **2.9B revenue**, while Region **R4** trailed with only **1.2B**.
* **Transaction Value**: High-value purchases (>40,000) were more likely to involve discounts, contributing disproportionately to revenue.

# 💡 Conclusion

* Discounts are a major driver of revenue, contributing more than half of total sales despite fewer transactions.
* Store Type S4 and discount strategies emerge as the strongest drivers of sales performance.
* Seasonal trends show that discounts are most effective from mid-Q2 onwards, suggesting timing is crucial.
* Regional disparities indicate differences in customer behavior, engagement, or localized strategies.
* Some store types (S1 & S2) generate high revenue volume but show signs of underperformance relative to their size and potential.

# 📌 Recommendations

1. **Prioritize Store Type S4** during high-demand seasons (Q3–Q4) to maximize sales performance.
2. **Enhance discount strategies** in high-performing stores (especially S4) to drive revenue from high-value purchases.
3. **Re-evaluate underperforming store types (S1 & S2)** by adjusting product mix, store layout, or targeted promotions.
4. **Launch seasonal campaigns** with threshold-based discounts during Q3–Q4 to increase transaction values.
5. **Limit discounting in Q1–early Q2** to protect profit margins when discount effectiveness is lower.
6. **Segment promotions by store type and region**, using correlation insights to optimize targeting and efficiency.
7. **Adopt tailored pricing strategies** based on discount effectiveness and store profitability for long-term growth.

# 📕 Full Report
[![Report Preview](https://palankarta.com/wp-content/uploads/2020/06/DETAILED-PROJECT-REPORT-1024x576.jpg)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/supplement-sales-analysis/report.pdf)

[Click the image above or click here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/supplement-sales-analysis/report.pdf)