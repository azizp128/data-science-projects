# Project Description
Welcome to New York City, one of the most-visited cities in the world. There are many Airbnb listings in New York City to meet the high demand for temporary lodging for travelers, which can be anywhere between a few nights to many months. In this project, we will take a closer look at the New York Airbnb market by combining data from multiple file types like `.csv`, `.tsv`, and `.xlsx`.

> [!NOTE]  
> The project inspiration comes from DataCamp’s [Exploring Airbnb Market Trends](https://app.datacamp.com/learn/projects/1589) project, which served as the foundation for this work.
> All code and insights in this project are my own.

# Dataset
Recall that **CSV**, **TSV**, and **Excel** files are three common formats for storing data. 
Three files containing data on 2019 Airbnb listings are available to you:

### **data/airbnb_price.csv**
This is a CSV file containing data on Airbnb listing prices and locations.
- **`listing_id`**: unique identifier of listing
- **`price`**: nightly listing price in USD
- **`nbhood_full`**: name of borough and neighborhood where listing is located

### **data/airbnb_room_type.xlsx**
This is an Excel file containing data on Airbnb listing descriptions and room types.
- **`listing_id`**: unique identifier of listing
- **`description`**: listing description
- **`room_type`**: Airbnb has three types of rooms: shared rooms, private rooms, and entire homes/apartments

### **data/airbnb_last_review.tsv**
This is a TSV file containing data on Airbnb host names and review dates.
- **`listing_id`**: unique identifier of listing
- **`host_name`**: name of listing host
- **`last_review`**: date when the listing was last reviewed

# Task
As a consultant working for a real estate start-up, you have collected Airbnb listing data from various sources to investigate the short-term rental market in New York. You'll analyze this data to provide insights on private rooms to the real estate company.
- What are the dates of the earliest and most recent reviews? 
- How many of the listings are private rooms?
- What is the average listing price?
- Combine the new variables into one DataFrame

# Solution
- [Jupyter Notebook](https://github.com/azizp128/data-science-projects/blob/main/exploring-airbnb-market-trends/notebook.ipynb)

# Findings
- Earliest and Most Recent Reviews
    - The earliest review in the dataset was on **2019-01-01**, and the most recent review occurred on **2019-07-09**. These dates were visualized on a heatmap to highlight the review distribution.

        ![Earliest And Recent Dates](https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/exploring-airbnb-market-trends/charts/earliest_recent_dates.png)
- Private Room Listings
    - There are **11,356** listings for **private rooms**, with the majority of listings categorized as **entire home/apt** (**13,266**) and **shared rooms** (**587**).

        ![Room Type Frequencies](https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/exploring-airbnb-market-trends/charts/listing_freq.png)
- Average Listing Price
    - The price distribution is right-skewed, with most listings priced at the lower end. A few high-priced listings cause the average price to be **$141.78**, higher than the median price of **$105**. This suggests that while many listings are affordable, the presence of luxury or overpriced properties may distort the overall pricing trend.

        ![Historagm of Listing Price Distribution](https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/exploring-airbnb-market-trends/charts/listing_price_dist_hist.png)
    - Additionally, there are potential outliers in the data, including a **$0** minimum price and a **$7,500** maximum price, which should be further examined.
      
        ![Box Plot of Listing Price Distribution](https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/exploring-airbnb-market-trends/charts/listing_price_dist_box_plot.png)
