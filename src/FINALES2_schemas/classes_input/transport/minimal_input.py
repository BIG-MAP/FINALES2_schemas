from pydantic import BaseModel, Field
from typing import Optional
from FINALES2_schemas.classes_common import Location

class TransportInput(BaseModel):
    """ The input requrired for a request to transport physical objects from A to B."""
    origin:Location = Field(
        description=("The location, from where the physical object shall be picked up.")
    )
    destination:Location = Field(
        description=("The destination, where the physical object is needed.")
    )