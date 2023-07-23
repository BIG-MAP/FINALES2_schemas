from pydantic import BaseModel, Field

from FINALES2_schemas.classes_common import FormulationComponent

class ElectrolyteInput(BaseModel):
    """Parameters used by the quantities
    'electrolyte' - 'flow'

    :param BaseModel: used to ensure, that the class can be checked for the types
    :type BaseModel: pydantic.BaseModel
    """
    formulation:list[FormulationComponent] = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
