from pydantic import BaseModel, Field
from .formulation import Formulation
from .unit_registry import unit_registry

class Electrode(BaseModel):
    material:Formulation = Field(
        description=("The description of the composition of the electrode.")
    )
    mass_loading:float = Field(
        unit=str(unit_registry.mAh * unit_registry.cm **-2),
        description=("The capacity per unit area of the electrode. "
                     f"Unit: {str(unit_registry.mAh * unit_registry.cm **-2)}")
    )
    current_collector:str = Field(
        description=("A designation of the current collector material. E.g. 'copper' or 'aluminium'.")
    )
