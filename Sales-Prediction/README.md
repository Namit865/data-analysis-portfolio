# 📊 Retail Sales Prediction using Machine Learning

## 🔹 Overview

This project focuses on predicting weekly retail sales using real-world business features such as store characteristics, economic indicators, promotional markdowns, and seasonal patterns.

The goal is to simulate how companies forecast demand and make data-driven business decisions.

---

## 🔹 Features Used

### 🏪 Store & Department

* Store
* Dept
* Type
* Size

### 📅 Time-Based Features

* Year
* Month
* WeekOfYear
* IsHoliday

### 📈 Economic Indicators

* CPI
* Unemployment
* Fuel_Price
* Temperature

### 💸 Promotional Features

* MarkDown1 – MarkDown5

---

## 🔹 Model Details

* Algorithm: **RandomForestRegressor**
* Pipeline: **Scikit-learn Pipeline**
* Data Split: **Time-based split (no data leakage)**

---

## 🔹 Results

* 📉 Mean Absolute Error (MAE): ~1330
* 📊 R² Score: ~0.98

The model performs well on seasonal trends and store-level patterns.

---

## 🔹 Limitations

* Model relies heavily on calendar-based patterns
* Promotional impact (MarkDown features) can be improved
* Does not include lag-based temporal dependencies

---

## 🔹 Future Improvements

* Add lag-based features for better forecasting
* Improve promotion modeling
* Hyperparameter tuning
* Deploy scalable model system

---

## 🔹 Project Structure

```
retail-sales-prediction-ml/
│
├── data/
├── notebook/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Setup & Run

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/retail-sales-prediction-ml.git
cd retail-sales-prediction-ml
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

### 3️⃣ Activate Environment

#### Windows:

```
venv\Scripts\activate
```

#### Mac/Linux:

```
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Run API

```
uvicorn main:app --reload
```

---

## 🔹 API Usage

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 Note

The trained model file (`.pkl`) is not included due to size limitations.
You can generate it by running the training notebook.

---

## 🔹 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* FastAPI
* Uvicorn

---

## 🔹 Author

**Namit Senjaliya**
