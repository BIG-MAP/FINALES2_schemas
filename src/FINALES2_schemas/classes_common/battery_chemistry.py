from pydantic import BaseModel, Field
from .formulation import Formulation
from .electrode import Electrode

class BatteryChemistry(BaseModel):
    electrolyte:Formulation = Field(
        description = ("The definition of the composition of the electrolyte used in the "
                     "cells, for which the prediction shall be made")
    )
    anode:Electrode = Field(
        description=("The definition of the anode.")
    )
    cathode:Electrode = Field(
        description=("The definition of the cathode.")
    )