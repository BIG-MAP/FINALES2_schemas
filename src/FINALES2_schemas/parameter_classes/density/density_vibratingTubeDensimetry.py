from pydantic import BaseModel, Field
from typing import Optional
from .density import DensityOutput
from ..generalSchemas import RunInfo

class  DensityVibratingTubeDensimetryOutput(BaseModel):
    runInfo:RunInfo = Field(
        description=("The information regarding the formulation and the internal "
                     "reference, which is common for all data generated in this run of "
                     "the method.")
    )
    density:DensityOutput = Field(
        description=("The output generated for the density data.")
    )
    # viscosity:Optional(ViscosityOutput) = Field(
    #     description=("The ouptut of viscosity measurements, which were run in parallel "
    #                  "to the density measurement.")
    # )