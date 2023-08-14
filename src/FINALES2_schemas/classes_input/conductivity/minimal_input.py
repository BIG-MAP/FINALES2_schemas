from pydantic import BaseModel, Field
from typing import Optional

from FINALES2_schemas.classes_common import FormulationComponent, unit_registry

class ConductivityInput(BaseModel):
    """Parameters used by the quantities
    'conductivity' - 'twoElectrodeMeasuringCell'
    'conductivity' - 'molecularDynamicsSimulation'

    :param BaseModel: used to ensure, that the class can be checked for the types
    :type BaseModel: pydantic.BaseModel
    """
    formulation:list[FormulationComponent] = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        default=None,
        unit=str(unit_registry.kelvin),
        description=("This is the temperature of the measuring cell or used in a "
                    "simulation. It shall be given in the unit kelvin. "
                    f"Unit: {str(unit_registry.kelvin)}")
    )
