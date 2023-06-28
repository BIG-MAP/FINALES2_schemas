from pydantic import BaseModel, Field
from typing import Optional
from FINALES2_schemas.classes_common import unit_registry, Cell

class AssemblyInput(BaseModel):
    cell_info:Cell = Field(
        description=("This is a Cell class defining the information needed "
                    "to fabricate a single cell with the respective battery chemistry.")
    )
    batch_volume:Optional[int] = Field(
        description=("This is the numbers of the cells to be fabricated in one batch "
                    "with the same chemistry, It shall be given in the unit pieces. "
                    "And range from 1 (lowest) to 64 (highest). "
                    f"Unit: {str(unit_registry.pcs)}")
    )