from pydantic import BaseModel, Field
from typing import Optional
from parameter_classes.common_subclasses.run_info import RunInfo
from parameter_classes.density.shared_classes import DensityOutput
from parameter_classes.conductivity.shared_classes import ConductivityOutput

class  DensityMolecularDynamicsOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    density:DensityOutput = Field(
        description=("The output generated for the density data.")
    )
    conductivity:Optional[ConductivityOutput] = Field(
        description=("The ouptut of conductivity measurements, which were run in parallel "
                     "to the density measurement.")
    )  
    # RDF:Optional[RDFOutput] = Field(
    #     description=("The ouptut of RDF calculations, which were generated "
    #                  "as a side result.")
    # )