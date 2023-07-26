from typing import Union
from pydantic import BaseModel

class Immo(BaseModel):
    transactionSubtype: str
    price: int
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
