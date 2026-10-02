from datetime import datetime
from pydantic import BaseModel

class SolarWindObservation(BaseModel):
    timestamp: datetime
    speed: float