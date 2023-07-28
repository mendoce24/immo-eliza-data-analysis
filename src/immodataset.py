from typing import Union
from pydantic import BaseModel

class Immo(BaseModel):
    transactionSubtype: str
    type: str
    subtype: str
    region: str
    province: str
    floor: int
    bedroomCount: int
    netHabitableSurface: int
    constructionYear: int
    facadeCount: Union[int, None] = None
    floorCount: int
    condition: str
    hasLift: Union[int, None] = None
    kitchen: str
    hasGarden: Union[int, None] = None
    gardenSurface: Union[int, None] = None
    hasTerrace: Union[int, None] = None
    terraceSurface: Union[int, None] = None
    fireplaceExists: Union[int, None] = None
    hasSwimmingPool: Union[int, None] = None
    hasAirConditioning: Union[int, None] = None
    bathroomCount: int
    showerRoomCount: int
    toiletCount: int
    parkingCountIndoor: Union[int, None] = None
    parkingCountOutdoor: Union[int, None] = None
    primaryEnergyConsumptionPerSqm: Union[int, None] = None
    epcScore: str
    hasDoubleGlazing: Union[int, None] = None


    def immo_ini():
        immo = Immo(
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
        return immo