from typing import Optional
from pydantic import BaseModel, Field

class CyclingChannelOutput(BaseModel):
    success:bool = Field(
        description=("Indicator for the success of the reservation. This is False, if "
                     "the number of available channels is not sufficient to satisfy "
                     "the request.")
    )
    reservation_id:Optional[str] = Field(
        description=("An ID associated with the reservation to identify the request "
                     "once the request for the cycling experiment is received. This ID "
                     "needs to be provided by the requester in the input for the "
                     "cycling experiment (associated with the quantity 'capacity')."
                     "This ID is only provided, if the requested number of channels "
                     "was reserved.")
    )
