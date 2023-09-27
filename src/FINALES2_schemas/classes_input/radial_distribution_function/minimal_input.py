from pydantic import BaseModel, Field
from typing import Optional

from FINALES2_schemas.classes_common import FormulationComponent, unit_registry

class RDFInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `radial_density_function` - `molecular_dynamics_RDF`
    """
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
        default=None,
        unit=f"{unit_registry.g * unit_registry.cm ** -3}",
        description=("An inital guess for the density of the formulation, if available.")
    )