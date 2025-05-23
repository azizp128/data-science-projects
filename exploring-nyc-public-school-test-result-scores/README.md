# Project Description
Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a **maximum score of 800 points**. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.

Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend. 

You have been provided with a dataset called `schools.csv`, which is previewed below.

You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.

> [!NOTE]  
> The project inspiration comes from DataCamp’s [Exploring NYC Public School Test Result Scores](https://app.datacamp.com/learn/projects/exploring_nyc_public_school_test_result_scores/) project, which served as the foundation for this work.
> All code and insights in this project are my own.

# Dataset
### **schools.csv**

| Column                   | Description                                                                      |
|------------------------- |--------------------------------------------------------------------------------- |
| `school_name`            |    The name of the school.                                                       |
| `borough`                | The borough of New York City where the school is located (e.g., Manhattan, Bronx, Brooklyn, Queens, Staten Island).  |
| `building_code`          | A unique identifier for the building or facility where the school is housed. |
| `average_math`           |    The average SAT math score for students at the school.             |
| `average_reading`        | The average SAT reading score for students at the school.                            |
| `average_writing`        |   The average SAT writing score for students at the school.                               |
| `percent_tested`         | The percentage of eligible students at the school who took the SAT.                                      |

# Task
- Which NYC schools have the best math results?
- What are the top 10 performing schools based on the combined SAT scores?
- Which single borough has the largest standard deviation in the combined SAT score?

# Solution
- [Jupyter Notebook](https://github.com/azizp128/data-science-projects/blob/main/exploring-nyc-public-school-test-result-scores/notebook.ipynb)
- [Microsoft Excel Workbook](https://raw.githubusercontent.com/azizp128/data-science-projects/main/exploring-nyc-public-school-test-result-scores/workbook.xlsx)

# Findings
- Which NYC schools have the best math results?
    - There are 10 schools that have the best math scores in New York City, with all scores exceeding the threshold of 640 (0.8 * 800). These schools represents some of the best performers in New York City's educational landscape, with exceptional math scores.

        ![Top Schools By AVG Maths Score](https://raw.githubusercontent.com/azizp128/data-science-projects/main/exploring-nyc-public-school-test-result-scores/charts/top_schools_by_avg_math_scores.png)
- What are the top 10 performing schools based on the combined SAT scores?
    - **Consistent Top Performers**: Three schools (Stuyvesant High School, Bronx High School of Science, and Staten Island Technical High School) consistently rank at the top in both math and combined SAT scores, demonstrating strong performance across both areas.
    - **New Entrant in SAT Scores**: Bard High School Early College stands out as a new addition to the top 10 based on combined SAT scores, despite not ranking highly in math scores. This suggests that Bard High School Early College excels in the reading and writing sections of the SAT.
    - **Reading/Writing Strength**: Some schools, such as High School of American Studies at Lehman College and Townsend Harris High School, perform well in combined SAT scores despite having lower math scores. This highlights that strong performance in the verbal and writing sections can help offset lower math results.

        ![Top 10 Schools By SAT Score](https://raw.githubusercontent.com/azizp128/data-science-projects/main/exploring-nyc-public-school-test-result-scores/charts/top_10_schools_by_sat_scores.png)
- Which single borough has the largest standard deviation in the combined SAT score?
    - **Manhattan** has the highest standard deviation in combined SAT scores of **230.29**, indicating a diverse performance range across its schools.

        ![Borough With Highest STD SAT Score](https://raw.githubusercontent.com/azizp128/data-science-projects/main/exploring-nyc-public-school-test-result-scores/charts/borough_highest_std_sat_score.png)
    - This high standard deviation suggests that the schools in Manhattan have a wide range of SAT scores. Some schools perform significantly better than others, leading to this variability.

        ![Manhattan's SAT ](https://raw.githubusercontent.com/azizp128/data-science-projects/main/exploring-nyc-public-school-test-result-scores/charts/sat_distribution_manhattan.png)
    - This indicate that some schools in Manhattan are top performers with very high SAT scores, while others are performing below average, creating a larger spread in scores. It suggests that the educational performance in Manhattan's schools is not uniform.        
