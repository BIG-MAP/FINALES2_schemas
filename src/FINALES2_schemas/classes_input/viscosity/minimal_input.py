from typing import Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import FormulationComponent, unit_registry

class ViscosityInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `viscosity` - `rollingBallViscosimetry`
    """
    formulation:FormulationComponent = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature:Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description=("This is the temperature of measuring cell. "
                     f"Unit: {str(unit_registry.kelvin)}")
    )
