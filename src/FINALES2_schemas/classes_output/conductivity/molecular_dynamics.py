from pydantic import BaseModel, Field
from typing import Optional
from FINALES2_schemas.classes_common import RunInfo
from .minimal_output import ConductivityOutput
from FINALES2_schemas.classes_output.density import DensityOutput

class MolecularDynamicsOutput(BaseModel):
    run_info:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    conductivity:ConductivityOutput = Field(
        description=("The output generated for the conductivity data.")
    )
    density:Optional[DensityOutput] = Field(
        description=("The ouptut of density calculations, which were generated "
                      "as a side result.")
    )
    # TODO: Add this side result once the respective schema for RDFOutput is defined
    # RDF:Optional[RDFOutput] = Field(
    #     description=("The ouptut of RDF calculations, which were generated "
    #                  "as a side result.")
    # )