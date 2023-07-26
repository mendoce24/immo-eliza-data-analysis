from fastapi import FastAPI, HTTPException
from src.immodataset import Immo
import pandas as pd

app = FastAPI()

@app.get('/')
def index():
    return 'Immo Eliza Data Analysis'

@app.get('/predict')
def read_item():
    im = Immo(
        transactionSubtype= '',
        price= 0,
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
    immo = item.model_dump()
    immo = pd.DataFrame.from_dict(immo)

    if (str(immo['price']).isdigit() & 
          str(item['constructionYear']).isdigit() &
          str(item['netHabitableSurface']).isdigit()) == False:
        raise HTTPException(status_code=404, detail='expected numbers, got strings.')

    # get the dummies and store it in a variable
    transactionSubtype_dummies = pd.get_dummies(immo.transactionSubtype,dtype=int)
    type_dummies = pd.get_dummies(immo.type,dtype=int)
    subtype_dummies = pd.get_dummies(immo.subtype,dtype=int)
    region_dummies = pd.get_dummies(immo.region,dtype=int)
    province_dummies = pd.get_dummies(immo.province,dtype=int)
    condition_dummies = pd.get_dummies(immo.condition,dtype=int)
    kitchen_dummies = pd.get_dummies(immo.kitchen,dtype=int)
    epcScore_dummies = pd.get_dummies(immo.epcScore,dtype=int)
    
    # Concatenate the dummies to original dataframe
    immo = pd.concat([immo, transactionSubtype_dummies, type_dummies, subtype_dummies, region_dummies, 
                    province_dummies, condition_dummies, kitchen_dummies, epcScore_dummies], axis='columns')
    
    # drop the values
    immo = immo.drop(['transactionSubtype', 'type', 'subtype', 'region', 'province', 'condition', 'kitchen', 'epcScore'], axis='columns')

    immo.hasLift = immo.hasLift.replace({True: 1, False: 0})
    immo.hasGarden = immo.hasGarden.replace({True: 1, False: 0})
    immo.hasTerrace = immo.hasTerrace.replace({True: 1, False: 0})
    immo.fireplaceExists = immo.fireplaceExists.replace({True: 1, False: 0})
    immo.hasSwimmingPool = immo.hasSwimmingPool.replace({True: 1, False: 0})
    immo.hasAirConditioning = immo.hasAirConditioning.replace({True: 1, False: 0})
    immo.hasDoubleGlazing = immo.hasDoubleGlazing.replace({True: 1, False: 0})

    

    return (immo['price']) # salary + bonus - taxes