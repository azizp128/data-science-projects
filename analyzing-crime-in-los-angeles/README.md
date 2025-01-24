# Project Description
Los Angeles, California, attracts people from all over the world, offering lots of opportunities, not always of the good kind!

Known for its warm weather, palm trees, sprawling coastline, and Hollywood, along with producing some of the most iconic films and songs. However, as with any highly populated city, it isn't always glamorous and there can be a large volume of crime. That's where you can help!

You have been asked to support the Los Angeles Police Department (LAPD) by analyzing crime data to identify patterns in criminal behavior. They plan to use your insights to allocate resources effectively to tackle various crimes in different areas.

They have provided you with a single dataset to use. It is a modified version of the original data, which is publicly available from Los Angeles Open Data.

In this project, you'll serve as a data detective, supporting the Los Angeles Police Department (LAPD) in analyzing crime data to guide how they should allocate resources to protect the people of their city!

> [!NOTE]  
> The project inspiration comes from DataCamp’s [Analyzing Crime in Los Angeles](https://app.datacamp.com/learn/projects/1876) project, which served as the foundation for this work.
> All code and insights in this project are my own.

# Dataset
They have provided you with a single dataset to use. A summary and preview are provided below.

It is a modified version of the original data, which is publicly available from Los Angeles Open Data.

### **crimes.csv**
| Column     | Description              |
|------------|--------------------------|
| `'DR_NO'` | Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits. |
| `'Date Rptd'` | Date reported - MM/DD/YYYY. |
| `'DATE OCC'` | Date of occurrence - MM/DD/YYYY. |
| `'TIME OCC'` | In 24-hour military time. |
| `'AREA NAME'` | The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles. |
| `'Crm Cd Desc'` | Indicates the crime committed. |
| `'Vict Age'` | Victim's age in years. |
| `'Vict Sex'` | Victim's sex: `F`: Female, `M`: Male, `X`: Unknown. |
| `'Vict Descent'` | Victim's descent:<ul><li>`A` - Other Asian</li><li>`B` - Black</li><li>`C` - Chinese</li><li>`D` - Cambodian</li><li>`F` - Filipino</li><li>`G` - Guamanian</li><li>`H` - Hispanic/Latin/Mexican</li><li>`I` - American Indian/Alaskan Native</li><li>`J` - Japanese</li><li>`K` - Korean</li><li>`L` - Laotian</li><li>`O` - Other</li><li>`P` - Pacific Islander</li><li>`S` - Samoan</li><li>`U` - Hawaiian</li><li>`V` - Vietnamese</li><li>`W` - White</li><li>`X` - Unknown</li><li>`Z` - Asian Indian</li> |
| `'Weapon Desc'` | Description of the weapon used (if applicable). |
| `'Status Desc'` | Crime status. |
| `'LOCATION'` | Street address of the crime. |

# Task
Explore the ***crimes.csv*** dataset and use your findings to answer the following questions:
- Which hour has the highest frequency of crimes? 
- Which area has the largest frequency of night crimes (crimes committed between 10:00 PM and 03:59 AM)?
- Identify the number of crimes committed against victims of different age groups.

# Solution
- [Jupyter Notebook](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analyzing-crime-in-los-angeles/notebook.ipynb)

# Findings
- Which hour has the highest frequency of crimes?
    - The analysis shows that **12 PM** has the highest frequency of crimes, with a total of **13,663** cases recorded. This suggests that crimes are most frequent during midday, indicating potential patterns or behaviors associated with this time.

        ![Crime Peak Hours](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analyzing-crime-in-los-angeles/charts/crime_peak_hours.png)
- Which area has the largest frequency of night crimes (crimes committed between 10:00 PM and 03:59 AM)?
    - The area **Central** experienced the largest frequency of night crimes, specifically those committed between **10:00 PM** and **3:59 AM**. A total of **3,312** crime cases were recorded in this time frame, highlighting **Central** as a hotspot for crimes during the night hours.
        
        ![Night Crime Frequency By Area](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analyzing-crime-in-los-angeles/charts/freq_night_crime_area.png)
- Identify the number of crimes committed against victims of different age groups.
    - The age group **26-34** has the highest number of crimes committed against victims, with a total of **47,470** recorded crime cases. This indicates that individuals within this age group are more likely to be involved as victims compared to others.

        ![Crime By Victim Age Group](https://raw.githubusercontent.com/azizp128/data-science-projects/main/analyzing-crime-in-los-angeles/charts/crimes_by_victim_age_group.png)
        
