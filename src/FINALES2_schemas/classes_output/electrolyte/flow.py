from typing import Optional
from pydantic import BaseModel, Field

from FINALES2_schemas.classes_common import RunInfo, FormulationInfo
from .minimal_output import ElectrolyteOutput

class FlowOutput(BaseModel):
    """
    Results returned from the following quantities:
    'electrolyte' - 'flow'
    """

    run_info:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    electrolyte:ElectrolyteOutput = Field(
        description="The output generated for the formulation of the electrolyte."
    )
