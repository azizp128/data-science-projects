# Project Description
The Nobel Prize is perhaps the world's most well known scientific award. Every year it is given to scientists and scholars in chemistry, literature, physics, medicine, economics, and peace. The first Nobel Prize was handed out in 1901, and at that time the prize was Eurocentric and male-focused, but nowadays it's not biased in any way. Surely, right?

Well, let's find out! What characteristics do the prize winners have? Which country gets it most often? And has anybody gotten it twice? It's up to you to figure this out.

The [**dataset**](https://www.kaggle.com/nobelfoundation/nobel-laureates) used in this project is from The Nobel Foundation on Kaggle.

> [!NOTE]  
> The project inspiration comes from DataCamp’s [Visualizing the History of Nobel Prize Winners](https://app.datacamp.com/learn/projects/441) project, which served as the foundation for this work.
> All code and insights in this project are my own.

# Dataset
### **nobel.csv**
| Column                  | Description                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| `year`                  | The year the Nobel Prize was awarded.                                                                     |
| `category`              | The Nobel Prize category, such as "Physics", "Chemistry", "Peace", "Literature", "Economics", etc.       |
| `prize`                 | The specific Nobel Prize name, e.g., "The Nobel Prize in Physics 1910", "The Nobel Prize in Chemistry 1920", etc.                 |
| `motivation`            | The reason or motivation for awarding the prize. This is a text field explaining why the prize was awarded.|
| `prize_share`           | The share of the Nobel Prize awarded to the laureate, which may be split if multiple laureates are honored.|
| `laureate_id`           | A unique identifier for each Nobel laureate.                                                             |
| `laureate_type`         | The type of laureate: individual or organization (e.g., "individual", "organization").                    |
| `full_name`             | The full name of the laureate or organization receiving the Nobel Prize.                                  |
| `birth_date`            | The birth date of the laureate. This field may contain null values for laureates with unknown birthdates.  |
| `birth_city`            | The city where the laureate was born (if available).                                                     |
| `birth_country`         | The country where the laureate was born.                                                                  |
| `sex`                   | The gender of the laureate (e.g., "Male", "Female").                                                     |
| `organization_name`     | The name of the organization that received the Nobel Prize (if applicable).                              |
| `organization_city`     | The city where the organization is located (if applicable).                                              |
| `organization_country`  | The country where the organization is located (if applicable).                                           |
| `death_date`            | The date of death of the laureate (if available).                                                        |
| `death_city`            | The city where the laureate died (if available).                                                         |
| `death_country`         | The country where the laureate died (if available).                                                      |

# Task
Analyze Nobel Prize winner data and identify patterns by answering the following questions:
- What is the most commonly awarded gender and birth country?
- Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
- Which decade and Nobel Prize category combination had the highest proportion of female laureates?
- Who was the first woman to receive a Nobel Prize, and in what category?
- Which individuals or organizations have won more than one Nobel Prize throughout the years?

# Solution
- [Jupyter Notebook](new-version/notebook.ipynb)