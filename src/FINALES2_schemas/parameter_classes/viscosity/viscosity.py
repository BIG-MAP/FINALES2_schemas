from typing import List, Optional, Union, Tuple, Any
from pydantic import BaseModel, Field
from datetime import date
from ..generalSchemas import FractionType, Chemical, Formulation, ChemicalInfo, FormulationInfo
from enum import Enum
from uuid import UUID
import pint

# To get the units available
unitRegistry = pint.UnitRegistry()

# class FractionType(str, Enum):
#     """Fraction types used to specify formulations"""
#     molPerMol = "molPerMol"
#     volumePerVolume = "volumePerVolume"

# class Chemical(BaseModel):
#     """Subclass"""
#     name:str = Field(
#         description="A human readable name of the chemical."
#     )
#     smiles:str = Field(
#         description="A SMILES string representing the chemical."
#     )
#     InChIKey:str = Field(
#         description=("The hashed standard International Chemical Identifier of "
#                     "the chemical to ensure machine-readability.")
#     )

# class Formulation(BaseModel):
#     """Subclass"""
#     name:str = Field(
#         description="A human readable name of the formulation."
#     )
#     uuid:UUID = Field(
#         description="A unique identifier assigned to this formulation in this run."
#     )
#     chemicals:dict[str, Chemical] = Field(
#         description=("A dictionary of the chemicals included in the formulation. "
#                     "InChIKeys as keys and corresponding Chemical objects as values.")
#     )
#     chemicalComposition:dict[str, float] = Field(
#         description=("A dictionary with the InChIKey as the key and the respective "
#                     "unitless fraction of the chemical in the total of the mixture as a "
#                      "value.")
#     )
#     fractionType:FractionType = Field(
#         description=("A value of an enumeration defining, what kind of a fraction is "
#                     "given in the formulation. This can be for example molar fractions, "
#                     "volume fractions, mass fractions,....")
#     )

class ViscosityInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `viscosity` - `rollingBallViscosimetry`
    """
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        unit=str(unitRegistry.kelvin),
        description="This is the temperature of measuring cell."
    )

class RunInfo(BaseModel):
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the"
                    "sample and their fraction in the total mixture.")
    )
    internalReference:str = Field(
        description=("This field is an internal ID identifying this run of the method."
                    " In experimental setups, this may reference to an ID of the sample.")
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

class ViscosityOutput(BaseModel):
    """
    Results returned from the following quantities:
    `viscosity` - `rollingBallViscosimetry`
    """
    values:list[float] = Field(
        unit=str(unitRegistry.g * unitRegistry.cm ** -3),
        description=("The values determined for the density.")
    )
    success:bool = Field(
        description=("This reports, if the method finished successfully.")
    )
    rating:int = Field(
        description=("This field serves to rate the quality of the result from the "
                     "tenant side. It shall range from 0 (lowest) to 5 (highest).")
    )
    temperature: Optional[float] = Field(
        unit=str(unitRegistry.kelvin),
        description="This is the temperature of measuring cell."
    )