from typing import List
from pydantic import BaseModel, Field

class Component(BaseModel):
    """Subclass"""
    name: str = Field(
        description="Description pending."
    )
    smiles: str = Field(
        description="Description pending."
    )
    reference: str = Field(
        description="Description pending."
    )
    ratio: float = Field(
        units="mol st / mol sc",
        description="This is the value of the molar fraction in the mixture for the component."
    )

class DensityCommon(BaseModel):
    """
    Parameters to be used with the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    formulation: List[Component] = Field(
        description="This is a list of dictionaries with the names of chemicals and their molar fraction in the mixture."
    )
    fraction: str = Field(
        description="This is the type of fraction used in the mixingRatio. Currently 'molPerMol' or 'direct' are supported for this."
    )
    measurement: str = Field(
        description="This is a string specifying, which measurement is requested. It can either be 'densiVisco' or 'nmr'."
    )
    temperature: float = Field(
        units="kelvin",
        description="This is the temperature of measuring cell."
    )
