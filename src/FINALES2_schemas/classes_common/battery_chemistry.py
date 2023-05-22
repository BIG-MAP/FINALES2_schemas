from pydantic import BaseModel, Field
from .formulation_info import FormulationInfo
from .electrode import Electrode
from .separator import Separator

class BatteryChemistry(BaseModel):
    """A description of the chemistry of a cell.
    """
    electrolyte:FormulationInfo = Field(
        description = ("The definition of the composition of the electrolyte used in the "
                     "cells, for which the prediction shall be made, this also includes the metadata.")
    )
    anode:Electrode = Field(
        description=("The definition of the anode.")
    )
    cathode:Electrode = Field(
        description=("The definition of the cathode.")
    )
    separator:Separator = Field(
        description=("The definition of the separator.")
    )
    