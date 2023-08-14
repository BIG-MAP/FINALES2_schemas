from pydantic import BaseModel, Field
from typing import Optional

class Location(BaseModel):
    """ The location providing information on where to find physical samples or
    equipment."""
    address:str = Field(
        description=("The physical address, where the object can be found. Depending "
                     "on the usecase, this may be an official address or a name of an "
                     "instute or similar. The default should be an address.")
    )
    detail_1:Optional[str] = Field(
        default=None,
        description=("A more detailed description of a location. This may be e.g. a "
                     "specific laboratory in a building, a desk in an office or a "
                     "device or a cabinet.")
    )
    detail_2:Optional[str] = Field(
        default=None,
        description=("Another level of detail for a location. This may be e.g. a "
                     "bench in the laboratory, a shelf in a cabinet "
                     " or a specific port in a machine.")
    )