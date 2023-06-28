from pydantic import BaseModel, Field
from FINALES2_schemas.src.classes_common import RunInfo
from FINALES2_schemas.src.classes_output.conductivity.minimal_output import ConductivityOutput

class TwoElectrodeOutput(BaseModel):
    run_info:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    conductivity:ConductivityOutput = Field(
        description=("The output generated for the conductivity data.")
    )