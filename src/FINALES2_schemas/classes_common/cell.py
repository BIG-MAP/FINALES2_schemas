from pydantic import BaseModel, Field
from typing import Optional
from .unit_registry import unit_registry
from .battery_chemistry import BatteryChemistry
from .separator import Separator

class Cell(BaseModel):
    batteryChemistry:BatteryChemistry = Field(
        description = ("The definition of the chemistry used in the "
                     "cells, which includes the electrodes and electrolyte")
    )
    separator:Separator = Field(
        description=("The definition of the separator.")
    )
    electrolyte_volume:float = Field(
        unit=str(unit_registry.uL),
        description=("A designation of the volume of electrolyte.")
    )