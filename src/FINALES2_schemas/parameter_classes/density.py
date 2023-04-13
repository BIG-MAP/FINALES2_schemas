from typing import List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

class FractionType(Enum):
    """Fraction types used to specify formulations"""
    molPerMol = "molPerMol"
    volumePerVolume = "volumePerVolume"
    # massPerMass = "massPerMass"   <-- this is not yet supported by ASAB, but might be
    #                                   useful for future use or other tenants

class Chemical(BaseModel):
    """Subclass"""
    name:str = Field(
        description="A human readable name of the chemical."
    )
    smiles:str = Field(
        description="A SMILES string representing the chemical."
    )
    InChIKey:str = Field(
        description=("The hashed standard International Chemical Identifier of"
                    "the chemical to ensure machine-readability.")
    )
    # molarMass:Optional[Tuple[float, float, SIunit]] = Field(
    #     description=("The molar mass of the chemical, the correcponding uncertainty"
    #                  "and the unit.")
    # )
    # density:Optional[Tuple[float, float, SIunit]] = Field(
    #     description=("The density of the chemical, the correcponding uncertainty"
    #                  "and the unit.")
    # )
    # batch:Optional[str] = Field(
    #     description="A batch number for the chemical used, if it is available."
    # )
    # manufacturer:Optional[str] = Field(
    #     description="The manufacturer of the chemical, if it is available."
    # )
    # manufacturingDate:Optional[date] = Field(
    #     description="The date when the chemical was manufactured."
    # )

class Formulation(BaseModel):
    """Subclass"""
    name:str = Field(
        description="A human readable name of the chemical."
    )
    # preparationDate:Optional[date] = Field(
    #     description=("The date when the formulation was prepared. For commercial"
    #                 "formulations, the manufacturing date may be used.")
    # )
    chemicals:dict[str, Chemical] = Field(
        description=("A dictionary of the chemicals included in the formulation."
                    "InChIKeys as keys and corresponding Chemical objects as values.")
    )
    chemicalComposition:dict[str, float] = Field(
        description=("A dictionary with the InChIKey as the key and the respective"
                    "unitless fraction of the chemical in the total of the mixture as a"
                     "value.")
    )
    fractionType:FractionType = Field(
        description=("A value of an enumeration defining, what kind of a fraction is"
                    "given in the formulation. This can be for example molar fractions,"
                    "volume fractions, mass fractions,....")
    )

class DensityCommon(BaseModel):
    """
    Parameters to be used with the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the"
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        unit="kelvin",
        description="This is the temperature of measuring cell."
    )


class DensityOutput(BaseModel):
    """
    Result for the density.
    """
    density_value: float = Field(
        units="g/L",
        description="The value of the density."
    )
