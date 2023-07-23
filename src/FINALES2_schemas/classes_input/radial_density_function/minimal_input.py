from pydantic import BaseModel, Field
from typing import Optional

from FINALES2_schemas.classes_common import FormulationComponent, unit_registry

class RDFInput(BaseModel):
    formulation:list[FormulationComponent] = Field(
        unit=f"{unit_registry.mol/unit_registry.mol}",
        description=("The formulation to be simulated. This is required to be provided "
                     "in units of mol per mol.")
    )
    temperature:float = Field(
        unit=f"{unit_registry.kelvin}",
        description=("The temperature, at which the simulation shall be performed.")
    )
    estimated_density:Optional[float] = Field(
        unit=f"{unit_registry.gram/unit_registry.cm**2}",
        description=("An inital guess for the density of the formulation, if available.")
    )