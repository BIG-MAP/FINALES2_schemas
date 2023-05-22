from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID
from .formulation_component import FormulationComponent


class FormulationInfo(BaseModel):
    """Additional information about a formulation, which is relevant for documentation
    purposes"""
    formulation:list[FormulationComponent] = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
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
