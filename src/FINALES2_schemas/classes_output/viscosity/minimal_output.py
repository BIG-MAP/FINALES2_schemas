from typing import Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import MethodMeta, unit_registry

class ViscosityOutput(BaseModel):
    """
    Results returned from the following quantities:
    `viscosity` - `rolling_ball_viscometry`
    """
    values:list[float] = Field(
        unit=str(unit_registry.g * unit_registry.cm ** -3),
        description=("The values determined for the density. "
                     f"Unit: {str(unit_registry.g * unit_registry.cm ** -3)}")
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
    temperature: Optional[float] = Field(
        default=None,
        unit=str(unit_registry.kelvin),
        description=("This is the temperature of measuring cell. "
                     f"Unit: {str(unit_registry.kelvin)}")
    )