from pydantic import BaseModel, Field
from uuid import UUID
from .minimal_output import AssemblyOutput

class AutoBASSOutput(BaseModel):
    """
    Result returned from the cell assembly, which merges all the cells in on batch:
    """
    batch_output:list[AssemblyOutput] = Field(
        description="The list includes the AssemblyOutput class from each single cell."
    )
    batch_id: UUID = Field(
        description="A unique identifier assigned to this batch of cells in this run."
    )