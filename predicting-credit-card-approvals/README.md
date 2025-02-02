# Project Description
Commercial banks receive a lot of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. In this workbook, you will build an automatic credit card approval predictor using machine learning techniques, just like real banks do.

> [!NOTE]  
> The project inspiration comes from DataCamp’s [Predicting Credit Card Approvals](https://app.datacamp.com/learn/projects/1908) project, which served as the foundation for this work.
> All code and insights in this project are my own.

# Dataset
The data is a small subset of the Credit Card Approval dataset from the UCI Machine Learning Repository showing the credit card applications a bank receives.
- [Credit Approval](https://archive.ics.uci.edu/dataset/27/credit+approval)

# Task
- Preproccess the data and apply supervised learning techniques to find the best model and parameters for the job.
- Aim for an accuracy score of at least 0.75.

# Solution
- [Jupyter Notebook](https://github.com/azizp128/data-science-projects/blob/main/predicting-credit-card-approvals/notebook.ipynb)
- [ydata-profiling Report](https://rawcdn.githack.com/azizp128/data-science-projects/refs/heads/main/predicting-credit-card-approvals/y_profiling_report.html)

# Findings
- Data Preprocessing & Exploration
    - Conducted **data profiling** using [ydata-profiling](https://github.com/ydataai/ydata-profiling) to understand dataset characteristics.
    - Cleaned the data by **removing missing values (`?`)**.
    - Performed **Exploratory Data Analysis (EDA)** to analyze numerical feature distributions.
        ![Distribution Before Log Transformation]()
    - Addressed **skewed features** in preprocessing to improve model performance.
        ![Distribution After Log Transformation]()
    - Transformed categorical variables into numerical form using **binary encoding and one-hot encoding**.
- Model Training & Evaluation
    - Split the dataset into **80% training and 20% testing**, and then using **Cross Validation** for performance evaluation.
    - Used [LazyClassifier](https://lazypredict.readthedocs.io/en/latest/usage.html#classification) for model selection, identifying **LGBMClassifier** as the best model with an **accuracy of 83%**.
    - Evaluated model predictions with a **confusion matrix**, highlighting misclassification patterns.
        ![Confusion Matrix]()
- Model Optimization
    - Performed **hyperparameter tuning** using `GridSearchCV`, optimizing key parameters.
    - Achieved a **2% accuracy improvement**, increasing performance from **83% to 85%**.

While an accuracy of **85%** is a promising improvement, we must still analyze the results critically. Given that the dataset has **imbalanced labels**, there is a risk that the model may still favor the majority class over the minority one, leading to suboptimal predictions. To further improve its performance, we can explore additional techniques such as **resampling methods**, where we either oversample the minority class or undersample the majority class to create a more balanced dataset. Another approach is **feature engineering**, where we refine or create new features that better capture the patterns in the data.

In conclusion, while our model has improved through careful tuning, there is always room for further enhancement. By addressing label imbalance and experimenting with advanced techniques, we can work towards building a model that is not only accurate but also more robust and reliable in real-world applications.