# Laptop-Price-Prediction

This project aims to predict the price of laptops based on various features like model, brand, specifications, and other attributes. The application is built using Streamlit for the frontend interface and leverages machine learning models built with scikit-learn and RandomForestRegressor for prediction. As an extra measure i have implemented Voting regressor and Stacking to commpare the model score with the ebase models.

# Project Structure

## The project contains the following files:

1. app.py: Streamlit web application for predicting laptop prices.

2. laptop_price_predictor.ipynb: Jupyter Notebook containing data analysis, preprocessing, and model training.

3. pipe_RF.pkl: Serialized machine learning model (Random Forest) used for prediction.

4. laptops_df.pkl: Pickle file containing the cleaned and preprocessed dataset.

Features

- Predicts laptop prices based on various specifications.

- User-friendly web interface using Streamlit.

- Supports dynamic input for different laptop configurations.

- Uses a trained Random Forest model for accurate predictions.

## Installation

To run the project locally, follow these steps:

### Clone the repository:

- git clone https://github.com/username/Laptop-Price-Prediction.git
- cd Laptop-Price-Prediction

### Create and activate a virtual environment:

- python -m venv myenv
- source myenv/bin/activate  # On Windows: myenv\Scripts\activate

### Install the required packages:

- pip install -r requirements.txt

### Running the Application
### Start the Streamlit application by running:

- streamlit run app.py

### Usage

- Open the application in your browser at http://localhost:8501.

### Fill in the required laptop specifications (refer to the Laptops specs for Testing.txt):

1. Model

2. Series

3. RAM

4. Weight

5. Touchscreen

6. IPS

7. Screen Size

8. Resolution

9. CPU

10. HDD

11. SSD

12. GPU

13. OS

- Click the Predict Price button to get the estimated price.

### Model and Training

The model used for prediction is a RandomForestRegressor trained on a dataset of laptop specifications and their corresponding prices. The model was trained using scikit-learn and fine-tuned to improve accuracy. 

Additionally i have implement Voting regressor and Stackingas a measure for comparison with the base models

### Model Features

Encodes categorical features using OneHotEncoder.

Uses Random Forest Regressor for robust predictions.

### Technologies Used

- Python: Core programming language

- Streamlit: Web application framework

- scikit-learn: Machine learning library

- NumPy: Numerical computations

- Pandas: Data manipulation and analysis

- Jupyter Notebook: Data analysis and model training

License

This project is licensed under the MIT License.
