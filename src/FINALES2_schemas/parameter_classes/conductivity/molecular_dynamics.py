from pydantic import BaseModel, Field
from typing import Optional
from ..common_subclasses.run_info import RunInfo
from .shared_classes import ConductivityOutput
from density.shared_classes import DensityOutput

class ConductivityMolecularDynamicsOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    conductivity:ConductivityOutput = Field(
        description=("The output generated for the conductivity data.")
    )
    density:Optional(DensityOutput) = Field(
        description=("The ouptut of density calculations, which were generated "
                      "as a side result.")
    )
    # RDF:Optional(RDFOutput) = Field(
    #     description=("The ouptut of RDF calculations, which were generated "
    #                  "as a side result.")
    # )