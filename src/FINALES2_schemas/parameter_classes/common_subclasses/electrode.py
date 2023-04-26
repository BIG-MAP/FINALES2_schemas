from pydantic import BaseModel, Field
from parameter_classes.common_subclasses.formulation import Formulation
from parameter_classes.common_subclasses.unit_registry import unit_registry

class Electrode(BaseModel):
    material:Formulation = Field(
        description=("The description of the composition of the electrode.")
    )
    massLoading:float = Field(
        unit=str(unit_registry.mAh * unit_registry.cm **-2),
        description=("The capacity per unit area of the electrode.")
    )
    currentCollector:str = Field(
        description=("A designation of the current collector material. E.g. 'copper' or 'aluminium'.")
    )
