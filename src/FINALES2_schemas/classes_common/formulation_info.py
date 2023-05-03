from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID


class FormulationInfo(BaseModel):
    """Additional information about a formulation, which is relevant for documentation
    purposes"""
    name:Optional[str] = Field(
        description="A human readable name of the formulation."
    )
    uuid:Optional[UUID] = Field(
        description="A unique identifier assigned to this formulation in this run."
    )
    preparation_date:Optional[date] = Field(
        description=("The date when the formulation was prepared. For commercial "
                    "formulations, the manufacturing date may be used.")
    )
    batch:Optional[str] = Field(
        description="A batch number for the formulation, if it is available."
    )
