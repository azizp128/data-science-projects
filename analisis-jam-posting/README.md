# Project Description
The Israel-Palestine conflict has been a highly discussed and sensitive topic in recent times. This project tries to analyze the most popular posting hours to determine the location of the authors.

# Dataset
### **pse_isr_reddit_comments.csv**
				
| Column     | Description              |
|------------|--------------------------|
| `'comment_id'` | Unique identifier for each comment. (type:str) |
| `'score'` | The score or upvotes received by the comment. (type:int) |
| `'self_text'` | The actual text content of the comment. (type:str) |
| `'subreddit'` | The subreddit where the comment was posted. (type:str) |
| `'created_time'` | The timestamp when the comment was created. (type:datetime) |

# Task
Analyze the most popular posting hours to determine the author's location based on the `subreddit` and `created_time` columns.

# Solution
- [Jupyter Notebook](https://github.com/azizp128/data-science-projects/blob/main/analisis-jam-posting/jam-posting.ipynb)
- [Jupyter Notebook on Kaggle](https://www.kaggle.com/code/azizp123/most-pop-posting-hours-to-determine-the-auths-loc)

# Findings
You can read the findings here: [Analisis Waktu Posting Paling Populer di Reddit terkait Konflik Israel-Palestina](https://blog.azizprabowo.com/data-science/analisis-waktu-posting-paling-populer-di-reddit-terkait-konflik-israel-palestina)
## Visualization using Matplotlib & Seaborn
![Matplotlib & Seaborn Visualizations](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analisis-jam-posting/viz/final_plot.png)

## Visualization using Tableau
![Tableau Visualization](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analisis-jam-posting/tableau/dashboard.png)

# Related Links
- [Dataset on Kaggle](https://www.kaggle.com/datasets/asaniczka/reddit-on-israel-palestine-daily-updated)
- [Visualization on Tableau Public](https://public.tableau.com/app/profile/aziz.prabowo3984/viz/AnalisisJamPostingPalingPopuleruntukMenentukanLokasiPenulisnya/Dashboard1)
- [Tableau File](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analisis-jam-posting/tableau/tableau.twbx)