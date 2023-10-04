# For app development
from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi import FastAPI, Form, Depends
import pandas as pd
import uvicorn
from pydantic import BaseModel
# For data frame
import pandas as pd
# For loading pipeline
import pickle
# For controlling warnings
import warnings
warnings.filterwarnings('ignore')
# For system functions
from io import BytesIO
import os

# Pieline loading
with open("..\\notebook\\pipeline.pkl", "rb") as f:
    pipe = pickle.load(f) 

cwd = os.getcwd()
relative_path = "notebook\\pipeline.pkl"

absolute_path = os.path.join(cwd, relative_path)

# instantiating fastAPI object
app = FastAPI(title = "Prediction From File - For \
              The classification API for predicting Sepsis positve / negative") 
  
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        content = await file.read() 
        df = pd.read_csv(BytesIO(content)) 

        # Selecting only usefull columns from users input file
        df = df[[ "PRG",   "PL",  "PR",  "SK",   "TS",   "M11",    "BD2",  "Age",  "Insurance"]].copy()

        # Predicting...
        output = pipe.predict_proba(df)
               
        df["predicted_label"] = output.argmax(axis = -1)
        mapping = {0: "Sepsis Negative", 1: "Sepsis Positive"}
        df["predicted_label"] = [mapping[x] for x in df["predicted_label"]]

        # Calculating confidence score
        confidence_score = output.max(axis= -1)
        df["confidence_score"] = f"{round( ( confidence_score[0] * 100 ) , 2) }%"
               
        return df.to_dict("records") 
    
    except Exception as e:
        return {"error": str(e)} # return an error message if something goes wrong

if __name__ == "__main__":
    uvicorn.run("main:app" , reload = True)