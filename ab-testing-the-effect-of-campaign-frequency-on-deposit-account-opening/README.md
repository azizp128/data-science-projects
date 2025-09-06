# 🔍 Background

In the banking industry, customer acquisition and retention are closely tied to the effectiveness of marketing campaigns. This project analyzes data from an A/B test conducted by a bank to understand whether the **number of campaigns** influences customers’ willingness to open a deposit account. The analysis is based on the **UCI Bank Marketing Dataset** (`bank-full.csv`), which contains 45,211 customer records.

# 🎯 Objective

* Test whether the number of marketing campaigns significantly affects deposit account openings.
* Provide evidence-based recommendations for optimizing marketing campaign strategies.
* Translate statistical results into actionable business insights that balance cost efficiency and customer experience.

# 📂 Dataset

* **Source**: [UCI Machine Learning Repository – Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)
* **Size**: 45,211 rows × 17 columns.
* **Features used in this analysis**:

  * **Independent Variable (X)**: `campaign` – number of contacts performed during the campaign.
  * **Dependent Variable (Y)**: `y` – whether the customer subscribed to a term deposit (yes/no).
* **Other Attributes**: Age, job, marital status, education, balance, housing, loan, contact type, duration, previous outcome, etc.
* **Data Quality**: No missing values detected in the relevant columns.

# 📊 Insight

* **Group Sizes**: 5,289 customers opened a deposit account (`yes`), while 39,922 did not (`no`).
* **Mean Campaigns**:

  * `Yes` group: **2.14 contacts** (std ≈ 1.26).
  * `No` group: **2.85 contacts** (std ≈ 3.10).
* **Interpretation**: On average, customers who converted required fewer contacts compared to those who did not convert.

# 💡 Conclusion

* A **two-sample t-test** (Welch’s test, due to unequal variances) showed a highly significant result (t = –22.8, p < 0.000001).
* We **reject the null hypothesis (H₀)** and conclude that the number of campaigns **does significantly affect the likelihood of opening a deposit account**.
* Surprisingly, **fewer campaigns are associated with higher conversion**. Overly frequent or aggressive campaigns may have a negative effect, reducing customers’ willingness to open an account.

# 📌 Recommendations

* **Reduce campaign frequency**: Limit average contacts to \~2.1 per user, saving \~**\$28,500** in marketing costs without hurting conversions.
* **Prioritize high-potential customers early**: Focus resources on likely converters, reducing cost per acquisition by 10–15%.
* **Cap maximum contacts at 3**: Stop campaigns for non-responsive users to prevent wasted spend and customer fatigue.
* **Refine messaging and timing**: Optimize communication strategy to potentially lift conversions by 10%, adding \~\$79K in revenue.
* **Segment customers**: Use demographics and behavioral data for more targeted campaigns.
* **Adopt multivariate testing**: Explore additional factors such as channel, timing, and message type for continuous optimization.

[View the full project Jupyter Notebook here](https://github.com/azizp128/data-science-projects/blob/main/ab-testing-the-effect-of-campaign-frequency-on-deposit-account-opening/notebook.ipynb)