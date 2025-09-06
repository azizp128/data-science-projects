# 🔍 Background

YouTube is one of the largest video-sharing platforms, with millions of videos uploaded and consumed daily. The number of views is a key indicator of video popularity and success. Various factors such as title, description, tags, category, publishing time, and engagement metrics (likes, dislikes, comments) may affect view counts.
By leveraging historical trending video data, this project aims to develop a predictive model that can estimate the number of views a video may achieve before trending. Such insights are valuable for content creators and analysts to optimize publishing strategies.

# 🎯 Objective

* Perform data cleaning and exploratory data analysis (EDA) on the YouTube trending video dataset.
* Engineer features such as tag count, description length, title length, and engagement ratios.
* Apply and evaluate different regression models (Linear Regression, Random Forest, Gradient Boosting, XGBoost, etc.) using metrics such as RMSE, MAE, and R².
* Identify the most influential features contributing to view prediction.
* Provide actionable insights for improving video performance.

# 📂 Dataset

The dataset consists of **36,791 rows** and **18 columns**, later enriched with engineered features. Key variables include:

* `trending_date` – Date when the video appeared in trending.
* `title`, `channel_title`, `tags`, `description`.
* `views`, `likes`, `dislikes`, `comment_count`.
* `category_id` – Encoded video category.
* `comments_disabled`, `ratings_disabled`, `video_error_or_removed`.
* Engineered features: `days_to_trend`, `publish_hour`, `publish_dayofweek`, `engagement_ratio`, `like_dislike_ratio`, `title_words_count`, `tag_density`, etc.


# 📊 Exploratory Data Analysis

* **Data Cleaning**: Removed 4,229 duplicate rows and filled 45 missing descriptions with `"no description"`.
* **Distributions**: Views, likes, dislikes, and comment counts are highly right-skewed, with a small number of viral outliers.
* **Correlations**:

  * Likes have the strongest correlation with views (r = 0.85).
  * Comment count shows a strong positive correlation (r = 0.67).
  * Dislikes moderately correlate with views (r = 0.54).
  * Title length and number of tags show very weak correlation with views.
* **Categorical Analysis**:

  * Category 30 videos achieved the highest median views (\~2.9M).
  * Videos with ratings enabled performed significantly better than those with ratings disabled.
  * Videos uploaded on Wednesdays and in the morning (5–11 AM) gained more views.


# 💡 Conclusion

* **Best Model**: XGBoost Regressor achieved the highest performance with hyperparameter tuning:

  * R² = 0.9915 ± 0.0049
  * RMSE ≈ 281,735
  * MAE ≈ 61,628
* **Feature Importance**: Likes, dislikes, engagement ratio, comment count, title length, and publishing day/time are the most influential predictors.
* **Insights**:

  * Viewer engagement (likes, comments, dislikes) is the strongest driver of views.
  * Publishing strategy (time and day) significantly impacts initial traction.
  * Content category influences median views, with some categories far outperforming others.

# 📌 Recommendation

1. **Boost Viewer Engagement**: Encourage likes/dislikes interactions to improve visibility; a 10% increase in likes could raise views by \~8–10%.
2. **Optimize Titles**: Keep titles between 6–12 words for higher CTR, potentially increasing views by 15–20%.
3. **Strategic Publishing**: Upload videos on high-engagement days (e.g., Wednesdays) and morning hours for 20–30% more initial views.
4. **Improve Metadata Quality**: Use keyword-rich descriptions and optimized tags to enhance search visibility and engagement.
5. **Focus on High-Performing Categories**: Prioritize categories with higher median views (e.g., Category 30, 15, 20) to increase total channel views.
6. **Leverage Predictive Modeling**: Use models to identify videos with high potential for promotion, improving ROI by 10–15%.
7. **Study Viral Patterns**: Analyze outlier videos to replicate characteristics of virality, potentially driving exponential growth.

[View the full project Jupyter Notebook here](https://github.com/azizp128/data-science-projects/blob/main/youtube-views-prediction/notebook.ipynb)