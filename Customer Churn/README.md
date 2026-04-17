# 🚀 Customer Churn Prediction API

## 📌 Overview

This project is an end-to-end Machine Learning system that predicts whether a customer is likely to churn or not.

The model is deployed using FastAPI, allowing real-time predictions through an API.

---

## 🧠 Problem Statement

Customer churn is a critical issue for businesses. Identifying customers who are likely to leave helps companies take preventive actions.

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* Pandas
* FastAPI
* Uvicorn

---

## 🔍 Features

* Full preprocessing pipeline (imputation + encoding)
* Machine learning model (Random Forest)
* REST API for real-time predictions
* Returns prediction along with probability

---

## 📂 Project Structure

```
Customer-Churn/
│
├── main.py
├── model/
│   └── churn_model.pkl
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── notebook/
│   └── customer_churn.ipynb
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/Namit865/data-analysis-portfolio/tree/37fab32e3accff0f9c592e15a3b88bc5d72e375e/Customer%20Churn
cd Customer-Churn
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the API

```
uvicorn main:app --reload
```

### 4. Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 📊 Example Input

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "No",
  "DeviceProtection": "Yes",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "Yes",
  "Contract": "One year",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 65.5,
  "TotalCharges": 780.0
}
```

---

## 📈 Example Output

```json
{
  "prediction": "No Churn",
  "probability": 0.17
}
```

---

## 🎯 Future Improvements

* Improve model performance (handle class imbalance)
* Add input validation using Pydantic
* Deploy API to cloud (Render / Railway)

---

## 📊 Key Insights

- Customers with month-to-month contracts are more likely to churn
- Higher monthly charges increase churn risk
- Customers with longer tenure are less likely to churn
- Lack of tech support and online security increases churn probability

## 💡 Author

Built by Namit

---
