from typing import Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import MethodMeta, unit_registry, FormulationComponent

class ElectrolyteOutput(BaseModel):
    """
    Results returned from the following quantities:
    `electrolyte` - `flow`
    """
    formulation:list[FormulationComponent] = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    volume:float = Field(
        unit=str(unit_registry.mL),
        description=("The volume of electrolyte, which needs to be formulated. "
            f"Unit: {str(unit_registry.mL)}.")
    )
    location:str = Field(
        description=("The physical location, from where the prepared electrolyte "
                     "formulation may be picked up.")
    )
    meta:MethodMeta = Field(
        description=("This field provides information regarding the reliability of the "
                     "reported data. E.g. the success of the method for this quantity "
                     "and the rating of the data. This is for this specific quantity, "
                     "because a single method could fail individually for different "
                     "quantities. It is not included in the RunInfo as one run may "
                     "generate data for different quantities, for which the methods "
                     "may fail individually.")
    )