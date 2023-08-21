from pydantic import BaseModel, Field
from .formulation_component import FormulationComponent
from .electrode import Electrode
from typing import Optional

class BatteryChemistry(BaseModel):
    """A description of the chemistry of a cell.
    """
    electrolyte:list[FormulationComponent] = Field(
        description = ("The definition of the composition of the electrolyte used in the "
                     "cells, for which the prediction shall be made")
    )
    anode:Optional[Electrode] = Field(
        default=None,
        description=("The definition of the anode.")
    )
    cathode:Optional[Electrode] = Field(
        default=None,
        description=("The definition of the cathode.")
    )
