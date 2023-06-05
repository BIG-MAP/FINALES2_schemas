from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID
from FINALES2_schemas.classes_common.cell import Cell


class CellInfo(BaseModel):
    """Additional information about a cell, which is relevant for documentation
    purposes"""
    cell:Cell = Field(
        description=("This is a Cell class defining the information needed")
    )
    cell_name:Optional[str] = Field(
        description="A human readable name of the cell."
    )
    uuid:Optional[UUID] = Field(
        description="A unique identifier assigned to this cell in this run."
    )
    assembly_date:Optional[date] = Field(
        description=("The date when the cell was made.")
    )
    batch:Optional[str] = Field(
        description="A batch number for the cells, if it is available."
    )