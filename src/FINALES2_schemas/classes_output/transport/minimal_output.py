from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import Location

class TransportOutput(BaseModel):
    """
    Results returned from the following quantities:
    'transport' - 'service'
    """

    success:bool = Field(
        description=("An information, whether the transport was successful.")
    )
    actual_new_location:Location = Field(
        description=("The new location ot the physical object.")
    )