from pydantic import BaseModel, Field
from typing import Optional
from .formulation_component import FormulationComponent
from .unit_registry import unit_registry

class Electrode(BaseModel):
    """The definition of an electrode.

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    material:list[FormulationComponent] = Field(
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
    Size:Optional[float] = Field(
        unit=str(unit_registry.cm**2),
        description=("The area of the electrode, of which the shape is cut in cirular.")
    )
