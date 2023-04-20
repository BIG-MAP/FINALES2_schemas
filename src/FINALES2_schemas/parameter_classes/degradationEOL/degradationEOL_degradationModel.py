from pydantic import BaseModel, Field
from .degradationEOL import degradationEOLInput, degradationEOLOutput
from ..generalSchemas import RunInfo

class DegradationEOLDegradationModelOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    degradationEOL:degradationEOLOutput = Field(
        description=("The data corresponding to the end of life for the cell and the "
                     "degradation trajectory, each with the respective uncertainty.")
    )