from pydantic import BaseModel
class UserInput(BaseModel):
    house_age: int
    GarageCars: int
    GarageArea: float
    OverallQual: int
    OverallCond: int
    Fireplaces: int
    total_bath: float
    KitchenQual: str
    ExterQual: str
    Neighborhood: str
    total_sqft: float