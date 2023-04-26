from pydantic import BaseModel, Field
from typing import Optional
from ..common_subclasses.run_info import RunInfo
from .shared_classes import DensityOutput
from ..conductivity.shared_classes import ConductivityOutput

class  DensityMolecularDynamicsSimulationOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    density:DensityOutput = Field(
        description=("The output generated for the density data.")
    )
    conductivity:Optional(ConductivityOutput) = Field(
        description=("The ouptut of conductivity measurements, which were run in parallel "
                     "to the density measurement.")
    )  
    # RDF:Optional(RDFOutput) = Field(
    #     description=("The ouptut of RDF calculations, which were generated "
    #                  "as a side result.")
    # )