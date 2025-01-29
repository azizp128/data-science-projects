# Project Description
A DVD rental company needs your help! They want to figure out how many days a customer will rent a DVD for based on some features and has approached you for help. They want you to try out some regression models which will help predict the number of days a customer will rent a DVD for. The company wants a model which yeilds a MSE of **3** or less on a test set. The model you make will help the company become more efficient inventory planning.

> [!NOTE]  
> The project inspiration comes from DataCamp’s [Predicting Movie Rental Durations](https://app.datacamp.com/learn/projects/1796) project, which served as the foundation for this work.
> All code and insights in this project are my own.

# Dataset
### **rental_info.csv**
| Column | Description |
|--------|-------------|
| `rental_date` | The date (and time) the customer rents the DVD |
| `return_date` | The date (and time) the customer returns the DVD |
| `amount` | The amount paid by the customer for renting the DVD |
| `amount_2` | The square of `amount` |
| `rental_rate` | The rate at which the DVD is rented for |
| `rental_rate_2` | The square of `rental_rate` |
| `release_year` | The year the movie being rented was released |
| `length` | Lenght of the movie being rented, in minuites |
| `length_2` | The square of `length` |
| `replacement_cost` | The amount it will cost the company to replace the DVD |
| `special_features` | Any special features, for example trailers/deleted scenes that the DVD also has |
| `NC-17`, `PG`, `PG-13`, `R` | These columns are dummy variables of the rating of the movie. It takes the value 1 if the move is rated as the column name and 0 otherwise. For your convinience, the reference dummy has already been dropped |

# Task
- Preprocess the dataset for modeling.
- Create a regression model to predict the number of days a customer rents DVDs for with MSE less than 3.

# Solution
- [Jupyter Notebook](https://github.com/azizp128/data-science-projects/blob/main/predicting-movie-rental-durations/notebook.ipynb)

# Findings
- R-Squared: **0.732**
    - **73%** of the variation in movie rental durations is explained by the model. The remaining **27%** is unexplained and may be due to unaccounted factors or random variation.

    ![R-Squared Value]()
- Mean Squared Error: **1.91**
    - The model's predictions, on average, are off by **1.91 days**, which is about **73%** of the rental duration's standard deviation (**2.64**). This suggests reasonable predictions but leaves room for improvement.

    ![Mean Squared Error Value]()
- Residual Plot
    - The residuals show a structured pattern rather than random scatter, indicating potential model issues like missing features or non-linearity. The model may not fully capture the relationship in the data.

    ![Residual Plot]()
- Actual vs. Predicted Plot
    - The model captures the general trend but struggles with precise predictions, particularly for higher rental lengths. There is significant vertical dispersion, meaning some predictions are over or under-estimated.

    ![Actual vs. Predicted Plot]()
- Distribution of Residuals
    - The residuals are approximately normally distributed, with a slight right skew, suggesting underprediction. Some large residuals (outliers) indicate occasional large prediction errors.

    ![Distribution of Residuals]()
- Feature Importance
    - The features `amount` and `rental_rate` have the highest importance scores, contributing significantly to the model’s predictions. These features are key drivers in explaining rental duration.

    ![Feature Importance]()