from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import MethodMeta, unit_registry

class AssemblyOutput(BaseModel):
    """
    Results returned from the single cell assembly:
    """
    sealing_time:Optional[datetime] = Field(
        description="The datetime when the cell was sealed."
    )
    manufacturing_img:str= Field(
        description=("The path, where the cells' manufacturing images can be accessed. This is "
                     "relevant as the data files are large and cannot easily be sent "
                     "via FINALES.")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description=("This is the temperature of cell assembly. "
                     f"Unit: {str(unit_registry.kelvin)}")
    )
    meta:MethodMeta = Field(
        description=("This field provides information regarding the reliability of the "
                     "reported data. E.g. the success of the method for this quantity "
                     "and the rating of the data. This is for this specific quantity, "
                     "because a single method could fail individually for different "
                     "quantities. It is not included in the RunInfo as one run may "
                     "generate data for different quantities, for which the methods "
                     "may fail individually.")
    )