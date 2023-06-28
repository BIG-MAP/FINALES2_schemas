from typing import List
from pydantic import BaseModel, Field

class CapacityCyclingOutput(BaseModel):
    """
    Result for the Capacities of each cycle.
    """
    capacity_list: List = Field(
        units="Ah",
        description="A list with calculated capacities in Ah for charge and discharge alternately."
    )
    channel_list: List = Field(
        description="A list with the channels used for cycling."
    )
