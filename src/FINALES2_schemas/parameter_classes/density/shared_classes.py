from typing import Optional
from pydantic import BaseModel, Field
from datetime import date
from ..common_subclasses.formulation import Formulation
from ..common_subclasses.mathod_meta import MethodMeta
from ..common_subclasses.unit_registry import unit_registry

class DensityInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description="This is the temperature of measuring cell."
    )

class DensityOutput(BaseModel):
    """
    Results returned from the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    values:list[float] = Field(
        unit=str(unit_registry.g * unit_registry.cm ** -3),
        description=("The values determined for the density.")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description="This is the actual temperature of measuring cell."
    )
    meta:MethodMeta = Field(
        description=("This field provides information regarding the reliability of the "
                     "reported data. E.g. the success of the method for this quantity "
                     "and the rating of the data. This is for this specific quantity, "
                     "because a single method could fail individually for different "
                     "quantities.")
    )