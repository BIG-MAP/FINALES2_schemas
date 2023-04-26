from typing import List, Optional, Union, Tuple, Any
from pydantic import BaseModel, Field
from datetime import date
from ..common_subclasses.fraction_type import FractionType
from ..common_subclasses.chemical import Chemical
from ..common_subclasses.formulation import Formulation
from ..common_subclasses.chemical_info import ChemicalInfo
from ..common_subclasses.formulation_info import FormulationInfo
from ..common_subclasses.unit_registry import unit_registry

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
        unit=str(unit_registry.kelvin),
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
        unit=str(unit_registry.g * unit_registry.cm ** -3),
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
        unit=str(unit_registry.kelvin),
        description="This is the temperature of measuring cell."
    )