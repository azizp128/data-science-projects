# Car Purchase Prediction Streamlit App

This repository contains the source code for a Streamlit application that helps users make car purchasing decisions. The application uses a Decision Tree classification model to predict whether a person can afford a car based on certain variables such as age, gender, and annual income. Users can input the values of these features to predict whether they can afford a car or not.

## Project Structure

```
car-purchase-prediction
├── src
│   ├── app.py          # Main entry point for the Streamlit application
│   └── utils
│       └── model.py    # Functions for loading the model and making predictions
├── assets
│   ├── model
│   │   ├── car_data.csv # Dataset used for training the model
│   │   └── model.joblib  # Trained model
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/car-purchase-prediction.git
   cd car-purchase-prediction
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, use the following command:
```
streamlit run src/app.py
```

This will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Usage

- Input your age, gender (1 for female, 0 for male), and annual salary in the provided fields.
- Click the submit button to see the prediction on whether you can afford a car.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.