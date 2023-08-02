from typing import List
from pydantic import BaseModel, Field

class CapacityCyclingOutput(BaseModel):
    """
    Results returned from the following quantities:
    `capacity` - `cycling`
    """
    capacity_list: List[float] = Field(
        units="Ah",
        description="A list with calculated capacities in Ah for charge and discharge alternately."
    )
    channel_list: List[int] = Field(
        description="A list with the channels used for cycling."
    )
