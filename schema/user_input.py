from typing import Literal
from pydantic import BaseModel, Field

class UserInput(BaseModel):
    LotArea: float = Field(..., json_schema_extra={"example": 8450})

    
    OverallQual: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] = Field(
        ..., json_schema_extra={"example": 7}
    )
    OverallCond: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] = Field(
        ..., json_schema_extra={"example": 5}
    )

    KitchenAbvGr: int = Field(..., json_schema_extra={"example": 1})
    GarageCars: int = Field(..., json_schema_extra={"example": 2})
    house_age: float = Field(..., json_schema_extra={"example": 20})
    total_sqft: float = Field(..., json_schema_extra={"example": 1710})
    total_bath: float = Field(..., json_schema_extra={"example": 2.5})

    MSZoning: Literal["RL", "RM", "FV", "RH", "C (all)"] = Field(
        ..., json_schema_extra={"example": "RL"}
    )

    Neighborhood: Literal[
        "Blueste",
        "BrDale",
        "BrkSide",
        "ClearCr",
        "CollgCr",
        "Crawfor",
        "Edwards",
        "Gilbert",
        "IDOTRR",
        "MeadowV",
        "Mitchel",
        "NAmes",
        "NPkVill",
        "NWAmes",
        "NoRidge",
        "NridgHt",
        "OldTown",
        "SWISU",
        "Sawyer",
        "SawyerW",
        "Somerst",
        "StoneBr",
        "Timber",
        "Veenker",
    ] = Field(..., json_schema_extra={"example": "CollgCr"})