from fastapi import FastAPI, HTTPException
from src.immodataset import Immo
import pandas as pd
from src.preprocessing import Preprocessing
from src.predict import Predict

app = FastAPI()

@app.get('/')
def index():
    return 'Immo Eliza Data Analysis'

@app.get('/predict')
def read_item():
    immo = Immo.immo_ini()
    immo = vars(immo)
    immo_data = '{'

    for item in immo:
        immo_data += (item + ' : ' + str(type(immo[item])) + ',')
    
    immo_data += '}'
    return immo_data


@app.post('/predict')
def update_item(item: Immo):

    immo = Preprocessing().transform_data_api(item)

    validate_data(immo)

    value_to_return = Predict().get_price_api(immo)

    return (value_to_return)


def validate_data(immo):
    if ((pd.api.types.is_numeric_dtype(immo.constructionYear)) &
        pd.api.types.is_numeric_dtype(immo.netHabitableSurface)) == False:
        raise HTTPException(status_code=404, detail='expected numbers, got strings.')