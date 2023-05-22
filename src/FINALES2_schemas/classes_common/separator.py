from pydantic import BaseModel, Field
from typing import Optional
from .formulation_component import FormulationComponent
from .unit_registry import unit_registry

class Separator(BaseModel):
    """The definition of an electrode.

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    material:list[FormulationComponent] = Field(
        description=("The description of the composition of the separator.")
    )
    Size:Optional[float] = Field(
        unit=str(unit_registry.cm**2),
        description=("The area of the separator, of which the shape is cut in cirular.")
    )
