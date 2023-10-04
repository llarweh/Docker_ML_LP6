# For app development
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

# Pieline loading
with open("..\\notebook\\pipeline.pkl", "rb") as f:
    pipe = pickle.load(f) 

app = FastAPI( title = "The classification API for predicting Sepsis positve / negative") # instantiating fastAPI object

@app.get("/")
async def root():
    return {
        "Info" : "The classification API for predicting Sepsis positve / Negative"
    }

# Class inherits from BaseModel to be used as pydantic model
class Sepssis(BaseModel):
    # Input features
    plasma_glucose : float
    Blood_work_result_1 : float
    Blood_pressure : float
    Blood_work_result_2 : float
    Blood_work_result_3 : float
    Body_mass_index : float
    Blood_work_result_4 : float
    Age : int
    Insurance : int

    @classmethod
    def as_form(
        cls,
        plasma_glucose: float = Form(...), # "..." means the form is required
        Blood_work_result_1: float = Form(...),
        Blood_pressure: float = Form(...),
        Blood_work_result_2: float = Form(...),
        Blood_work_result_3: float = Form(...),
        Body_mass_index: float = Form(...),
        Blood_work_result_4: float = Form(...),
        Age: float = Form(...),
        Insurance: float = Form(...)
    ) -> "Sepssis":      # Forward reference
        return cls(
            plasma_glucose=plasma_glucose,
            Blood_work_result_1=Blood_work_result_1,
            Blood_pressure=Blood_pressure,
            Blood_work_result_2=Blood_work_result_2,
            Blood_work_result_3=Blood_work_result_3,
            Body_mass_index=Body_mass_index,
            Blood_work_result_4=Blood_work_result_4,
            Age=Age,
            Insurance=Insurance
        )

@app.post("/dataframe/") 
async def create_dataframe(form_data: Sepssis = Depends(Sepssis.as_form)):
    try:
        # Convert the form data to a data frame
        df = pd.DataFrame(form_data.dict(), index=[0])

        # Predicting...
        output = pipe.predict_proba(df)
               
        df["predicted_label"] = output.argmax(axis = -1)
        mapping = {0: "Sepsis Negative", 1: "Sepsis Positive"}
        df["predicted_label"] = [mapping[x] for x in df["predicted_label"]]

        # Calculating confidence score
        confidence_score = output.max(axis= -1)
        df["confidence_score"] = f"{round( ( confidence_score[0] * 100 ) , 2) }%"
        
        # Creating a display output
        msg = "execution went fine"
        code = 1
        pred = df.to_dict("records")

        result = { "Execution Message " : msg , "Execution Code " : code , "Prediction" : pred }

    except Exception as e:
        # If there is an error...
        msg = "execution went wrong"
        code = 0
        pred = None

        result = { "Error" : str(e) , "Execution Message " : msg , "Execution Code " : code , "Prediction" : pred }

    return result

# Running automaticaly when there is a change
if __name__ == "__main__":
    uvicorn.run("main:app" , reload = True)