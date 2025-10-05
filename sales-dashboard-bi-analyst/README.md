# 🔍 Background

PT Sejahtera Bersama is a retail company specializing in robotics, drones, and related products across multiple U.S. cities. With a growing product portfolio and customer base, the company faces challenges in tracking sales performance and identifying which regions and product categories contribute most to revenue. Sales performance varies significantly by city and product type, making it crucial to analyze trends and uncover insights that can help optimize marketing, inventory, and operational strategies.

# 🎯 Objective

* Develop an **interactive dashboard** to visualize sales and order performance across cities and product categories.
* Identify **top-performing cities and product categories** that contribute the most to total revenue and sales volume.
* Detect **underperforming markets or products** to guide future marketing and inventory decisions.
* Enable the management team to make **data-driven strategic decisions** to improve efficiency, maximize sales, and enhance customer satisfaction.

# 📂 Dataset

The project uses a relational database consisting of **four tables**:

1. **Customers** (`CustomerID`) – Contains customer details including email and city.
2. **Products** (`ProdNumber`) – Contains product information such as product name, price, and category.
3. **Orders** (`OrderID`) – Stores transactional data including order date, product quantity, and customer reference.
4. **ProductCategory** (`CategoryID`) – Contains category names for products.

These tables are connected through primary and foreign keys:

* `Customers.CustomerID = Orders.CustomerID`
* `Products.ProdNumber = Orders.ProdNumber`
* `ProductCategory.CategoryID = Products.Category`

Data was retrieved using SQL queries with **LEFT JOINs** to ensure inclusion of all order data even if customer or product information was missing.

# 📊 Exploratory Data Analysis

* **Top-Performing Cities**: Washington, Houston, and Sacramento generated the highest revenue and order volume, highlighting them as the company’s key sales hubs.
* **Category Insights**:

  * *Robots* contributed the highest total revenue (≈743.5K).
  * *eBooks* recorded the highest order quantity (≈3.1K orders), showing strong customer engagement despite lower price per unit.
* These results indicate a clear difference between **high-value** and **high-volume** categories, suggesting the need for balanced strategies that target both revenue growth and customer demand.

# 💡 Conclusion

The analysis revealed that sales are concentrated in a few key cities and dominated by specific product categories. While robots drive the majority of revenue, eBooks attract the most transactions. This duality highlights opportunities to optimize both premium and mass-market strategies. The insights gained through this analysis were visualized using an **interactive Looker Studio dashboard**, allowing stakeholders to monitor performance trends in real time and make data-driven business decisions.

**Dashboard Link:** [Sales Performance Dashboard – Looker Studio](https://lookerstudio.google.com/reporting/acacfcfa-a42a-4548-938a-c4a619b9fa48)

# 📌 Recommendations

1. **Customer Segmentation & Retention**

    * Perform **RFM analysis** (Recency, Frequency, Monetary) to identify loyal and at-risk customers.
    * Send **personalized email campaigns**:

    * **Loyal customers** → Exclusive discounts or VIP programs.
    * **Passive customers** → Free shipping or discount vouchers to re-engage them.

2. **Category & Product Optimization**

    * Analyze **best- and worst-selling products** within each category.
    * Implement **cross-sell and up-sell** strategies:

        * Example: "Buy a Drone Kit → get Training Videos at a discount."
        * "Buy a Robot → get an eBook or blueprint bundle."

3. **City-Based Marketing**

    * Focus digital marketing efforts on **low-performing but high-potential cities**.
    * Conduct **local workshops or community events** (e.g., drone demos or robotics training) to boost regional awareness and sales.

[View the full project report PDF here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/sales-dashboard-bi-analyst/report.pdf)