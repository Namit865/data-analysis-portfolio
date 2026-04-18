import pickle
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

with open("model/sales_model.pkl",'rb') as f:
    model = pickle.load(f)


@app.get("/")
def home():
    return {"message" : "sales Forecast API Running"}


@app.post("/predict")
def predict(data:dict):
    try:
        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]
    except Exception as e:
        print("Error:",e)
        return {'Error:':str(e)}

    return {
        'Predicted Sales' : round(float(prediction),2),
    }