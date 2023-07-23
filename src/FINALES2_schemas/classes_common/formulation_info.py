from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID
from FINALES2_schemas.classes_common.location import Location


class FormulationInfo(BaseModel):
    """Additional information about a formulation, which is relevant for documentation
    purposes"""
    name:Optional[str] = Field(
        description="A human readable name of the formulation."
    )
    uuid:Optional[str] = Field(
        description="A unique identifier assigned to this formulation in this run."
    )
    preparation_date:Optional[str] = Field(
        description=("The date when the formulation was prepared. For commercial "
                    "formulations, the manufacturing date may be used.")
    )
    batch:Optional[str] = Field(
        description="A batch number for the formulation, if it is available."
    )
    location:Optional[Location] = Field(
        description=("The location, where the physical formulation can be found,"
                     " which corresponds to this specification.")
    )
