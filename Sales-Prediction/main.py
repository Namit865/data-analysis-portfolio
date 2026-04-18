import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

with open("../model/sales_model.pkl","rb") as f:
    model = pickle.load(f)


class SalesData(BaseModel):
    Store: int
    Dept: int
    IsHoliday: int
    Temperature: float
    Fuel_Price: float
    MarkDown1: float
    MarkDown2: float
    MarkDown3: float
    MarkDown4: float
    MarkDown5: float
    CPI: float
    Unemployment:float
    Type : str
    Size : int
    Year: int
    Month: int
    WeekOfYear : int

@app.get("/")
def home():
    return {'message':'Retail Sales Forecast API is Live!'}

@app.post("/predict")
def predict(data:SalesData):
    try:
        df = pd.DataFrame([data.dict()])

        prediction = model.predict(df)[0]

    except Exception as e:
        print("Error:",e)
        return {
            'Error' : str(e)
        }
    
    return {
        'Predicted Weekly Sales' : round(float(prediction),2)
    }