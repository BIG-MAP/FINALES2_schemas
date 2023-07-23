from pydantic import BaseModel, Field
from typing import Optional

from FINALES2_schemas.classes_common import MethodMeta, unit_registry

class ConductivityOutput(BaseModel):
    """
    Results returned from the following quantities:
    'conductivity' - 'two_electrode'
    'conductivity' - 'molecular_dynamics_conductivity'
    """
    values:list[float] = Field(
        unit=str(unit_registry.siemens * unit_registry.m ** -1),
        description=("The values determined for the conductivity. "
                     f"Unit: {str(unit_registry.siemens * unit_registry.m ** -1)}")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description=("This is the actual temperature of the measuring cell or used in a "
                    f"simulation. Unit: {str(unit_registry.kelvin)}")
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