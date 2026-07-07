from pydantic import BaseModel, Field

class SessionInput(BaseModel):
    Administrative: int = Field(..., ge=0, example=1)
    Administrative_Duration: float = Field(..., ge=0, example=14.65)
    Informational: int = Field(..., ge=0, example=0)
    Informational_Duration: float = Field(..., ge=0, example=0.0)
    ProductRelated: int = Field(..., ge=0, example=19)
    ProductRelated_Duration: float = Field(..., ge=0, example=283.88)
    BounceRates: float = Field(..., ge=0, le=1, example=0.008)
    ExitRates: float = Field(..., ge=0, le=1, example=0.042)
    PageValues: float = Field(..., ge=0, example=68.58)
    SpecialDay: float = Field(..., ge=0, le=1, example=0.0)
    Month: str = Field(..., example="June")
    OperatingSystems: int = Field(..., example=1)
    Browser: int = Field(..., example=2)
    Region: int = Field(..., example=1)
    TrafficType: int = Field(..., example=1)
    VisitorType: str = Field(..., example="Returning_Visitor")
    Weekend: bool = Field(..., example=False)

class PredictionOutput(BaseModel):
    prediction: int
    prediction_label: str
    purchase_probability: float