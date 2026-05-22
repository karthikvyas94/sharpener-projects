# Car Insurance Claim Prediction

A machine learning project that predicts whether a customer is likely to file a car insurance claim based on policy, vehicle, and customer-related features.

## Project Overview

This project uses Python and machine learning techniques to:

* Perform Exploratory Data Analysis (EDA)
* Clean and preprocess insurance data
* Handle categorical features using encoding
* Balance imbalanced datasets using SMOTE
* Train classification models
* Evaluate model performance using metrics such as accuracy score and confusion matrix

The goal is to build a predictive model that helps insurance companies identify potential claim cases in advance.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Jupyter Notebook

---

## Machine Learning Workflow

### 1. Data Collection

* Loaded dataset using Pandas
* Read CSV insurance dataset

### 2. Exploratory Data Analysis (EDA)

* Checked dataset shape
* Viewed top rows and column information
* Analyzed missing values
* Generated descriptive statistics
* Visualized data distributions and relationships

### 3. Data Preprocessing

* Removed unnecessary columns
* Encoded categorical variables using Label Encoding
* Handled imbalanced data using SMOTE
* Split data into training and testing sets

### 4. Model Building

The project includes training classification models such as:

* Decision Tree Classifier
* Other Scikit-learn models (if added)

### 5. Model Evaluation

Evaluated the model using:

* Accuracy Score
* Confusion Matrix
* Classification Report
* Cross Validation

---

## Project Structure

```bash
car-insurance-claim-prediction/
│
├── car insurance claim prediction.ipynb
├── data.csv
├── README.md
└── requirements.txt
```

## Sample Features Used

Some example features used in prediction:

* Vehicle age
* Policy tenure
* Engine type
* Fuel type
* Area cluster
* Driver information
* Vehicle specifications
* Safety features

---

## Future Improvements

* Hyperparameter tuning
* Feature engineering
* Deploying the model using Flask or FastAPI
* Creating a web application interface
* Trying advanced models like XGBoost and Random Forest

---

## Learning Outcomes

Through this project, you can learn:

* Data preprocessing techniques
* Handling imbalanced datasets
* Classification algorithms
* Model evaluation metrics
* End-to-end machine learning workflow

---

## Author

Created by Karthik Bandamidi

---

## License

This project is open-source and available under the MIT License.
