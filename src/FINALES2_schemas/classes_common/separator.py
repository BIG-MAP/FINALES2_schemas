from pydantic import BaseModel, Field
from typing import Optional
from .unit_registry import unit_registry

class Separator(BaseModel):
    """The definition of a separator used in battery cells."""
    material:str = Field(
        description=("The product name of the separator reported by the manufacturer, "
                     "E.g. Celgard 2325.")
    )
    size:Optional[float] = Field(
        default=None,
        unit=str(unit_registry.cm**2),
        description=("The area of the separator, of which the shape is cut in cirular.")
    )