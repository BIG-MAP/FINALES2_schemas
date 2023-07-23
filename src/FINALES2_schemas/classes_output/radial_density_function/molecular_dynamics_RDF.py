from pydantic import BaseModel, Field
from typing import Optional

from .minimal_output import RDFOutput
from FINALES2_schemas.classes_common import RunInfo
from FINALES2_schemas.classes_output.density import DensityOutput
from FINALES2_schemas.classes_output.conductivity import ConductivityOutput

class MolecularDynamicsOutput(BaseModel):
    """
    Results returned from the following quantities:
    'radial_density_function' - 'molecular_dynamics_RDF'
    """

    run_info:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    RDF:RDFOutput = Field(
        description=("The ouptut of RDF calculations.")
    )
    conductivity:Optional[ConductivityOutput] = Field(
        description=("The output generated for the conductivity data, which were "
                     "generated as a side result.")
    )
    density:Optional[DensityOutput] = Field(
        description=("The ouptut of density calculations, which were generated "
                      "as a side result.")
    )