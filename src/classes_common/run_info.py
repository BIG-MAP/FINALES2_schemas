from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID
from .chemical_info import ChemicalInfo
from .formulation_info import FormulationInfo
from .formulation_component import FormulationComponent

class RunInfo(BaseModel):
    """Metadata for a run of a method. This information may apply to all samples
    processed in the respective run.
    """
    formulation:List[FormulationComponent] = Field(
        description=("This is a formulation defining the Chemicals contained in the"
                    "sample and their fraction in the total mixture.")
    )
    internal_reference:UUID = Field(
        description=("This field is an internal ID identifying this run of the method."
                    " In experimental setups, this may reference to an ID of the sample.")
    )
    formulation_info:Optional[FormulationInfo] = Field(
        description=("This is the metadata concerning the formulation relevant for "
                    "documentation.")
    )
    chemicals_info:Optional[Dict[str, ChemicalInfo]] = Field(
        description=("This is a dictionary of metadata of the chemicals relevant for "
                    "documentation. The keys are InChIKeys of the chemicals contained "
                    "in the formulation and the values are ChemicalInfo objects.")
    )
