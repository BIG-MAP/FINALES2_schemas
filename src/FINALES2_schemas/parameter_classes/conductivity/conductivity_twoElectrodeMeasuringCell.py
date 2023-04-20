from pydantic import BaseModel, Field
from ..generalSchemas import RunInfo
from conductivity.conductivity import ConductivityOutput

class ConductivityTwoElectrodeMeasurementCellOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    conductivity:ConductivityOutput = Field(
        description=("The output generated for the conductivity data.")
    )