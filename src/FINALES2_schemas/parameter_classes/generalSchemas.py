from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID
from typing import List, Optional, Union, Tuple, Any
from datetime import date
import pint

# To get the units available
unitRegistry = pint.UnitRegistry()

class FractionType(str, Enum):
    """Fraction types used to specify formulations"""
    molPerMol = "molPerMol"

class Chemical(BaseModel):
    """Subclass"""
    name:str = Field(
        description="A human readable name of the chemical."
    )
    smiles:str = Field(
        description="A SMILES string representing the chemical."
    )
    InChIKey:str = Field(
        description=("The hashed standard International Chemical Identifier of "
                    "the chemical to ensure machine-readability.")
    )

class Formulation(BaseModel):
    """Subclass"""
    name:str = Field(
        description="A human readable name of the formulation."
    )
    uuid:UUID = Field(
        description="A unique identifier assigned to this formulation in this run."
    )
    chemicals:dict[str, Chemical] = Field(
        description=("A dictionary of the chemicals included in the formulation. "
                    "InChIKeys as keys and corresponding Chemical objects as values.")
    )
    chemicalComposition:dict[str, float] = Field(
        description=("A dictionary with the InChIKey as the key and the respective "
                    "unitless fraction of the chemical in the total of the mixture as a "
                     "value.")
    )
    fractionType:FractionType = Field(
        description=("A value of an enumeration defining, what kind of a fraction is "
                    "given in the formulation. This can be for example molar fractions, "
                    "volume fractions, mass fractions,.... At the moment only molar f"
                    "ractions are supported.")
    )

class FormulationInfo(BaseModel):
    """Additional information about a formulation, which is relevant for documentation
    purposes"""
    preparationDate:Optional[date] = Field(
        description=("The date when the formulation was prepared. For commercial "
                    "formulations, the manufacturing date may be used.")
    )
    batch:Optional[str] = Field(
        description="A batch number for the formulation, if it is available."
    )

class ChemicalInfo(BaseModel):
    """Additional information about a chemical, which is relevant for documentation
    purposes"""
    molarMass:Optional[Tuple[float, float]] = Field(
        unit=str(unitRegistry.g / unitRegistry.mole),
        description=("The molar mass of the chemical and the correcponding uncertainty. "
                     "This may be a measured quantity or a literature "
                     "value. It is needed to convert between volumetric and molar "
                     "ratios and this field serves to report the used value.")
    )
    density:Optional[Tuple[float, float]] = Field(
        unit=str(unitRegistry.g * unitRegistry.cm ** 3),
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
