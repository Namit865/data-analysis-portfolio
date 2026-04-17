import pickle
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

with open('churn_model.pkl','rb') as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message":"Customer Churn API Running"}

@app.post("/predict")
def predict(data:dict):
    try:
        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]
        proba = model.predict_proba(df)[0][1]

        result = "Churn" if prediction == 1 else "No Churn"
    except Exception as e:
        print("Error:",e)
        return {'Error:':str(e)}

    return {
        "prediction" : result,
        'probability' : round(proba,3)
    }