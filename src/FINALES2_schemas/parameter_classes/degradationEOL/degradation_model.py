from pydantic import BaseModel, Field
from .shared_classes import DegradationEOLOutput
from ..common_subclasses.run_info import RunInfo

class DegradationModelOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    degradationEOL:DegradationEOLOutput = Field(
        description=("The data corresponding to the end of life for the cell and the "
                     "degradation trajectory, each with the respective uncertainty.")
    )