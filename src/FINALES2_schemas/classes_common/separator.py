from pydantic import BaseModel, Field
from typing import Optional
from .formulation_component import FormulationComponent
from .unit_registry import unit_registry

class Separator(BaseModel):
    """The definition of an electrode.

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    material:str = Field(
        description=("The product name of the separator reported by the manufacturer, "
                     "E.g. Celgard 2325.")
    )
    size:Optional[float] = Field(
        unit=str(unit_registry.cm**2),
        description=("The area of the separator, of which the shape is cut in cirular.")
    )
