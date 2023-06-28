from pydantic import BaseModel, Field
from FINALES2_schemas.src.classes_output.degradationEOL.minimal_output import DegradationEOLOutput
from FINALES2_schemas.src.classes_common import RunInfo

class DegradationModelOutput(BaseModel):
    run_info:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    degradationEOL:DegradationEOLOutput = Field(
        description=("The data corresponding to the end of life for the cell and the "
                     "degradation trajectory, each with the respective uncertainty.")
    )