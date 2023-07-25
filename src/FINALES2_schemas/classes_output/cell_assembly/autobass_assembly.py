from pydantic import BaseModel, Field
from .minimal_output import AssemblyOutput

class AutoBASSOutput(BaseModel):
    """
    Results returned from the following quantities:
    `cell_assembly` - `autobass_assembly`
    """
    batch_output:list[AssemblyOutput] = Field(
        description="The list includes the AssemblyOutput class from each single cell."
    )
    batch_id:str = Field(
        description="A unique identifier assigned to this batch of cells in this run."
    )
