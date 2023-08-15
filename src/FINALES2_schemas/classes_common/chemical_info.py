from pydantic import BaseModel, Field
from typing import Optional, Tuple
from .unit_registry import unit_registry

class ChemicalInfo(BaseModel):
    """Additional information about a chemical, which is relevant for documentation
    purposes"""
    name:Optional[str] = Field(
        default=None,
        description=("A human readable name of the chemical, to which this information "
                    "is referring.")
    )
    molar_mass:Optional[Tuple[float, float]] = Field(
        default=None,
        unit=str(unit_registry.g / unit_registry.mole),
        description=("The molar mass of the chemical and the correcponding uncertainty. "
                     "This may be a measured quantity or a literature "
                     "value. It is needed to convert between volumetric and molar "
                     "ratios and this field serves to report the used value. "
                     f"Unit: {str(unit_registry.g / unit_registry.mole)}")
    )
    density:Optional[Tuple[float, float]] = Field(
        default=None,
        unit=str(unit_registry.g * unit_registry.cm ** 3),
        description=("The density of the chemical and the correcponding uncertainty. "
                     "This may be a measured quantity or a literature "
                     "value. It is needed to convert between volumetric and molar "
                     "ratios and this field serves to report the used value. "
                     f"Unit: {str(unit_registry.g * unit_registry.cm ** 3)}")
    )
    batch:Optional[str] = Field(
        default=None,
        description="A batch number for the chemical used, if it is available."
    )
    manufacturer:Optional[str] = Field(
        default=None,
        description="The manufacturer of the chemical, if it is available."
    )
    manufacturing_date:Optional[str] = Field(
        default=None,
        description="The date when the chemical was manufactured."
    )
