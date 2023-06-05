from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import unit_registry, CellInfo

class AssemblyInput(BaseModel):
    cell_info:CellInfo = Field(
        description=("This is a CellInfo class defining the information needed"
                    "to fabricate a single cell with the same battery chemistry, which includes the metadata.")
    )
    batch_volume:int = Field(
        description=("This is the numbers of the cells to be fabricated in one batch"
                    "with the same chemistry, It shall be given in the unit pieces. "
                    "And range from 1 (lowest) to 64 (highest). "
                    f"Unit: {str(unit_registry.pcs)}")
    )