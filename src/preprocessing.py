import pandas as pd
import numpy as np

class Preprocessing():

    def __init__(self) -> None:
        pass

    def format_data_get_dummies(self, immo):
        # get the dummies and store it in a variable
        transactionSubtype_dummies = pd.get_dummies(immo.transactionSubtype,dtype=int)
        type_dummies = pd.get_dummies(immo.type,dtype=int,prefix='TYPE_')
        subtype_dummies = pd.get_dummies(immo.subtype,dtype=int)
        region_dummies = pd.get_dummies(immo.region,dtype=int)
        province_dummies = pd.get_dummies(immo.province,dtype=int)
        condition_dummies = pd.get_dummies(immo.condition,dtype=int)
        kitchen_dummies = pd.get_dummies(immo.kitchen,dtype=int)
        epcScore_dummies = pd.get_dummies(immo.epcScore,dtype=int)
        print(type(immo), type(transactionSubtype_dummies))
        # Concatenate the dummies to original dataframe
        immo = pd.concat([immo, transactionSubtype_dummies, type_dummies, subtype_dummies, region_dummies, 
                        province_dummies, condition_dummies, kitchen_dummies, epcScore_dummies], axis='columns')

        # drop the values
        immo = immo.drop(['transactionSubtype', 'type', 'subtype', 'region', 'province', 'condition', 'kitchen', 'epcScore'], 
                         axis='columns')

        immo.hasLift = immo.hasLift.replace({True: 1, False: 0})
        immo.hasGarden = immo.hasGarden.replace({True: 1, False: 0})
        immo.hasTerrace = immo.hasTerrace.replace({True: 1, False: 0})
        immo.fireplaceExists = immo.fireplaceExists.replace({True: 1, False: 0})
        immo.hasSwimmingPool = immo.hasSwimmingPool.replace({True: 1, False: 0})
        immo.hasAirConditioning = immo.hasAirConditioning.replace({True: 1, False: 0})
        immo.hasDoubleGlazing = immo.hasDoubleGlazing.replace({True: 1, False: 0})

        immo.columns = immo.columns.str.replace(' ', '_')
        
        return immo
    
    
    def transform_data_api(self, data):
        df = pd.DataFrame(
            {
                'transactionSubtype': [data.transactionSubtype],
                'type': [data.type],
                "subtype": [data.subtype],
                "region": [data.region],
                "province": [data.province],
                "bedroomCount": [data.bedroomCount],
                "netHabitableSurface": data.netHabitableSurface,
                "constructionYear": data.constructionYear,
                "facadeCount": [data.facadeCount],
                "floorCount": [data.floorCount],
                "condition": [data.condition],
                "hasLift": [data.hasLift],
                "kitchen": [data.kitchen],
                "hasGarden": [data.hasGarden],
                "hasTerrace": [data.hasTerrace],
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
            }
            )
        
        return df