from pydantic import BaseModel, Field

from FINALES2_schemas.classes_common import unit_registry
from .minimal_input import ElectrolyteInput

class FlowInput(BaseModel):
    """Input taken by the quantity and method
    'electrolyte' - 'flow'

    :param BaseModel: used to ensure, that the class can be checked for the types
    :type BaseModel: pydantic.BaseModel
    """
    electrolyte:ElectrolyteInput = Field(
        description="The definition of the electrolyte formulation to be prepared."
    )
    volume:float = Field(
        unit=str(unit_registry.mL),
        description=("The volume of electrolyte, which needs to be formulated. "
            f"Unit: {str(unit_registry.mL)}.")
    )
