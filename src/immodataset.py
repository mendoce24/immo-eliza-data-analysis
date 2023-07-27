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

'''
class ImmoTransform(BaseModel):
    transactionSubtype= None
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
    hasDoubleGlazing: Union[int, None] = None,
    BUY_REGULAR: Union[int, None] = None
    PUBLIC_SALE: Union[int, None] = None
    TYPE__APARTMENT: Union[int, None] = None
    TYPE__HOUSE: Union[int, None] = None
    APARTMENT: Union[int, None] = None
    APARTMENT_BLOCK: Union[int, None] = None
    BUNGALOW: Union[int, None] = None
    CASTLE: Union[int, None] = None
    CHALET: Union[int, None] = None
    COUNTRY_COTTAGE: Union[int, None] = None
    DUPLEX: Union[int, None] = None
    EXCEPTIONAL_PROPERTY: Union[int, None] = None
    FARMHOUSE: Union[int, None] = None
    FLAT_STUDIO: Union[int, None] = None
    GROUND_FLOOR: Union[int, None] = None
    HOUSE: Union[int, None] = None
    KOT: Union[int, None] = None
    LOFT: Union[int, None] = None
    MANOR_HOUSE: Union[int, None] = None
    MANSION: Union[int, None] = None
    MIXED_USE_BUILDING: Union[int, None] = None
    OTHER_PROPERTY: Union[int, None] = None
    PENTHOUSE: Union[int, None] = None
    SERVICE_FLAT: Union[int, None] = None
    TOWN_HOUSE: Union[int, None] = None
    TRIPLEX: Union[int, None] = None
    VILLA: Union[int, None] = None
    Brussels: Union[int, None] = None
    Flanders: Union[int, None] = None
    Wallonie: Union[int, None] = None
    Antwerp: Union[int, None] = None
    Brussels: Union[int, None] = None
    East: Union[int, None] = None
    Flanders: Union[int, None] = None
    Flemish: Union[int, None] = None
    Brabant: Union[int, None] = None
    Hainaut: Union[int, None] = None
    Limburg: Union[int, None] = None
    Liege: Union[int, None] = None
    Luxembourg: Union[int, None] = None
    Namur: Union[int, None] = None
    Walloon: Union[int, None] = None
    Brabant: Union[int, None] = None
    'West Flanders': Union[int, None] = None
    AS_NEW: Union[int, None] = None
    GOOD: Union[int, None] = None
    JUST_RENOVATED	NO_COND_INFORMATION	TO_BE_DONE_UP	TO_RENOVATE	TO_RESTORE	HYPER_EQUIPPED	INSTALLED	NOT_INSTALLED	NO_KITCH_INFORMATION	SEMI_EQUIPPED	USA_HYPER_EQUIPPED	USA_INSTALLED	USA_SEMI_EQUIPPED	USA_UNINSTALLED	A	A+	A++	B	C	D	E	F	G	NO_EPC_SCORE: Union[int, None] = None
'''    

