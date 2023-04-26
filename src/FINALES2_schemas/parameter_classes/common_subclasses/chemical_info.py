from pydantic import BaseModel, Field
from typing import List, Optional, Tuple
from datetime import date
from unit_registry import unit_registry

class ChemicalInfo(BaseModel):
    """Additional information about a chemical, which is relevant for documentation
    purposes"""
    molarMass:Optional[Tuple[float, float]] = Field(
        unit=str(unit_registry.g / unit_registry.mole),
        description=("The molar mass of the chemical and the correcponding uncertainty. "
                     "This may be a measured quantity or a literature "
                     "value. It is needed to convert between volumetric and molar "
                     "ratios and this field serves to report the used value.")
    )
    density:Optional[Tuple[float, float]] = Field(
        unit=str(unit_registry.g * unit_registry.cm ** 3),
        description=("The density of the chemical and the correcponding uncertainty. "
                     "This may be a measured quantity or a literature "
                     "value. It is needed to convert between volumetric and molar "
                     "ratios and this field serves to report the used value.")
    )
    batch:Optional[str] = Field(
        description="A batch number for the chemical used, if it is available."
    )
    manufacturer:Optional[str] = Field(
        description="The manufacturer of the chemical, if it is available."
    )
    manufacturingDate:Optional[date] = Field(
        description="The date when the chemical was manufactured."
    )
