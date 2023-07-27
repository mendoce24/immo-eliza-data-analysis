from fastapi import FastAPI, HTTPException
from src.immodataset import Immo
import pandas as pd
import pickle
from src.regressor_models import RegressorModels
from src.preprocessing import Preprocessing
import json
import numpy as np

app = FastAPI()

@app.get('/')
def index():
    return 'Immo Eliza Data Analysis'

@app.get('/predict')
def read_item():
    im = Immo(
        transactionSubtype= '',
        type= '',
        subtype= '',
        region= '',
        province= '',
        floor= 0,
        bedroomCount= 0,
        netHabitableSurface= 0,
        constructionYear= 0,
        facadeCount= 0,
        floorCount= 0,
        condition= '',
        hasLift= 0,
        kitchen= '',
        hasGarden= 0,
        gardenSurface= 0,
        hasTerrace= 0,
        terraceSurface= 0,
        fireplaceExists= 0,      
        hasSwimmingPool= 0,
        hasAirConditioning= 0,
        bathroomCount= 0,
        showerRoomCount= 0,
        toiletCount= 0,
        parkingCountIndoor= 0,
        parkingCountOutdoor= 0,
        primaryEnergyConsumptionPerSqm= 0,
        epcScore= '',
        hasDoubleGlazing= 0
        )
    temp = vars(im)
    immo_data = '{'

    for item in temp:
        immo_data += (item + ' : ' + str(type(temp[item])) + ',')
    
    immo_data += '}'
    return immo_data

@app.post('/predict')
def update_item(item: Immo):
    #immo = item.dict()
    #dict= json.loads(item)
    #immo = pd.read_json(item)
    immo = transform_data(item)

    if (str(immo.constructionYear).isdigit() &
          str(immo.netHabitableSurface).isdigit()) == False:
        raise HTTPException(status_code=404, detail='expected numbers, got strings.' + str(immo.constructionYear)+', '+str(immo.netHabitableSurface))

    immo = Preprocessing().format_data(immo)


    filename = "../models/immo_model.pickle"

    # load model
    loaded_model = pickle.load(open(filename, "rb"))

    # predition with training data 
    pred_train= loaded_model.predict(immo)
    # calculating performance metric training
    score, mse, rmse, mae = RegressorModels.get_performance(immo, pred_train)

    value_to_return = ''
    for item in pred_train:
        value_to_return += '{ "prediction": '+ item +', "status_code": Optional[int]}'

    return (value_to_return)


def transform_data(data):
    '''immo = {
        'transactionSubtype': [data.transactionSubtype],
        "type": [data.type],
        "subtype": [data.subtype],
        "region": [data.region],
        "province": [data.province],
        "floor": [data.floor],
        "bedroomCount": [data.bedroomCount],
        "netHabitableSurface": [data.netHabitableSurface],
        "constructionYear": [data.constructionYear],
        "facadeCount": [data.facadeCount],
        "floorCount": [data.floorCount],
        "condition": [data.condition],
        "hasLift": [data.hasLift],
        "kitchen": [data.kitchen],
        "hasGarden": [data.hasGarden],
        "gardenSurface": [data.gardenSurface],
        "hasTerrace": [data.hasTerrace],
        "terraceSurface": [data.terraceSurface],
        "fireplaceExists": [data.fireplaceExists],
        "hasSwimmingPool": [data.hasSwimmingPool],
        "hasAirConditioning": [data.hasAirConditioning],
        "bathroomCount": [data.bathroomCount],
        "showerRoomCount": [data.showerRoomCount],
        "toiletCount": [data.toiletCount],
        "parkingCountIndoor": [data.parkingCountIndoor],
        "parkingCountOutdoor": [data.parkingCountOutdoor],
        "primaryEnergyConsumptionPerSqm": [data.primaryEnergyConsumptionPerSqm],
        "epcScore": [data.epcScore],
        "hasDoubleGlazing": [data.hasDoubleGlazing]
    }'''


    immo = pd.DataFrame(np.array(item.dict()),
                   columns=["transactionSubtype",
                            "type",
                            "subtype",
                            "region",
                            "province",
                            "floor",
                            "bedroomCount",
                            "netHabitableSurface",
                            "constructionYear",
                            "facadeCount",
                            "floorCount",
                            "condition",
                            "hasLift",
                            "kitchen",
                            "hasGarden",
                            "gardenSurface",
                            "hasTerrace",
                            "terraceSurface",
                            "fireplaceExists",
                            "hasSwimmingPool",
                            "hasAirConditioning",
                            "bathroomCount",
                            "showerRoomCount",
                            "toiletCount",
                            "parkingCountIndoor",
                            "parkingCountOutdoor",
                            "primaryEnergyConsumptionPerSqm",
                            "epcScore",
                            "hasDoubleGlazing"])

    #immo = pd.DataFrame(data=immo)

    return immo