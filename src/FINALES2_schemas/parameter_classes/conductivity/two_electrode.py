from pydantic import BaseModel, Field
from ..common_subclasses.run_info import RunInfo
from .shared_classes import ConductivityOutput

class ConductivityTwoElectrodeOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    conductivity:ConductivityOutput = Field(
        description=("The output generated for the conductivity data.")
    )