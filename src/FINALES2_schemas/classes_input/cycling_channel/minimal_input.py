from typing import Optional
from pydantic import BaseModel, Field

class CyclingChannelInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `cycling_channel` - `service`
    """
    number_required_channels:int = Field(
        description=("The number of cycling channels required for the cycling "
                     "experiment.")
    )
    cycling_protocol:Optional[str] = Field(
        description=("The designation of the protocol to use for the cycling "
                     "experiment.")
    )
    number_cycles:Optional[int] = Field(
        description=("The number of cycles, which are planned for the cycling "
                     "experiment.")
    )
