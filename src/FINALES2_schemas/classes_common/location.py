from pydantic import BaseModel, Field
from typing import Optional

class Location(BaseModel):
    """ The location providing information on where to find physical samples or
    equipment."""
    address:str = Field(
        description=("The physical address, where the objec can be found. Depending "
                     "on the usecase, this may be an official address or a name of an "
                     "instute or similar. The default should be an address.")
    )
    detail_1:str = Field(
        description=("A more detailed description of a location. This may be e.g. a "
                     "specific laboratory in a building, a desk in an office or a "
                     "device or a cabinet.")
    )
    detail_2:str = Field(
        description=("Another level of detail for a location. This may be e.g. a "
                     "bench in the laboratory, a shelf in a cabinet "
                     " or a specific port in a machine.")
    )