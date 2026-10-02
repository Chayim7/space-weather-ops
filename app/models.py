from datetime import datetime
from pydantic import BaseModel, Field

class SolarWindObservation(BaseModel):
    timestamp: datetime
    speed: float = Field(..., ge=0) #speed must be greater than or equal to 0, and it must be a float