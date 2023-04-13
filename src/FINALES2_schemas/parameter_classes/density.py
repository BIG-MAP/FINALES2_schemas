from typing import List, Optional, Union, Tuple, Any
from pydantic import BaseModel, Field
from datetime import date
from enum import Enum
from uuid import UUID
import pint

# To get the units available
unitRegistry = pint.UnitRegistry()

class FractionType(str, Enum):
    """Fraction types used to specify formulations"""
    molPerMol = "molPerMol"
    volumePerVolume = "volumePerVolume"

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
                    "volume fractions, mass fractions,....")
    )

class DensityInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        unit=str(unitRegistry.kelvin),
        description="This is the temperature of measuring cell."
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

class DensityOutput(BaseModel):
    """
    Results returned from the following quantities:
    `density` - `vibratingTubeDensimetry`
    `density` - `molecularDynamicsSimulation`
    """
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the"
                    "sample and their fraction in the total mixture.")
    )
    values:list[float] = Field(
        unit=str(unitRegistry.g * unitRegistry.cm ** -3),
        description=("The values determined for the density.")
    )
    success:bool = Field(
        description=("This reports, if the method finished successfully.")
    )
    internalReference:str = Field(
        description=("This field is an internal ID identifying this run of the method."
                    " In experimental setups, this may reference to an ID of the sample.")
    )
    rating:int = Field(
        description=("This field serves to rate the quality of the result from the "
                     "tenant side. It shall range from 0 (lowest) to 5 (highest).")
    )
    formulationInfo:Optional[FormulationInfo] = Field(
        description=("This is the metadata concerning the formulation relevant for "
                    "documentation.")
    )
    chemicalsInfo:Optional[dict[str, ChemicalInfo]] = Field(
        description=("This is a dictionary of metadata of the chemicals relevant for "
                    "documentation. The keys are InChIKeys of the chemicals contained "
                    "in the formulation and the values are ChemicalInfo objects.")
    )
    temperature: Optional[float] = Field(
        unit=str(unitRegistry.kelvin),
        description="This is the temperature of measuring cell."
    )
