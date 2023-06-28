from typing import Optional, List
from pydantic import BaseModel, Field
from FINALES2_schemas.src.classes_common import FormulationComponent, unit_registry

class DensityInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    formulation:List[FormulationComponent] = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description=("This is the temperature of measuring cell. "
                     f"Unit: {str(unit_registry.kelvin)}")

    )
