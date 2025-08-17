# Description

This is a Machine Learning model that utilizes Logistic Regression to predict the survival of passengers aboard the Titanic. The model is trained on a dataset consisting of various passenger attributes such as age, gender, ticket class, and more. By analyzing these features, the model can make predictions on whether a passenger would have survived or not. 

In addition, this project includes a web application deployed on the Heroku platform, serving as the focal point for experimenting with deploying an ML model using Django. The web application enables users to interact with the trained model and receive predictions on the survival probability of a passenger based on the information provided.

# How to Run
Follow these steps to run the Django project locally:

1. Install **Python 3.10.7**
   
    Make sure Python is added to your system PATH.

3. Navigate to the project directory
    ```bash
    cd \path\to\this_project

4. Create a virtual environment
    ```bash
    python -m venv venv

5. Activate the virtual environment
    - Windows:
        ```bash
        venv\Scripts\activate
    - macOS/Linux:
        ```bash
        source venv/bin/activate

6. Install project dependencies
    ```bash
    python -m pip install -r requirements.txt

7. Apply database migrations
    ```bash
    python manage.py migrate

8. Run the development server
    ```bash
    python manage.py runserver

9. Open the app in your browser
    Go to http://127.0.0.1:8000/ to see the running application.

# Screenshot
![Page Screenshot](https://raw.githubusercontent.com/azizp128/titanic-survival-prediction-django/refs/heads/main/assets/screenshot.png)
