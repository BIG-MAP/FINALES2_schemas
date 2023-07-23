from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import RunInfo, FormulationInfo
from .minimal_output import ConductivityOutput

class TwoElectrodeOutput(BaseModel):
    """
    Results returned from the following quantities:
    'conductivity' - 'two_electrode'
    """
    run_info:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    conductivity:ConductivityOutput = Field(
        description=("The output generated for the conductivity data.")
    )
