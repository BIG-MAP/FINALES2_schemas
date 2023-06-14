from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID
from FINALES2_schemas.classes_common.cell import Cell
from FINALES2_schemas.classes_common.formulation_info import FormulationInfo


class CellInfo(BaseModel):
    """Additional information about a cell, which is relevant for documentation
    purposes"""
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
    anode_info:Optional[FormulationInfo] = Field(
        description=("The metadata related to the anode used in the cell.")
    )
    cathode_info:Optional[FormulationInfo] = Field(
        description=("The metadata related to the cathode used in the cell.")
    )