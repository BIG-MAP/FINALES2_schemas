from pydantic import BaseModel, Field
from typing import Optional
from FINALES2_schemas.classes_common import Location

class TransportOutput(BaseModel):
    success:bool = Field(
        description=("An information, whether the transport was successful.")
    )
    actual_new_location:Location = Field(
        description=("The new location ot the physical object.")
    )