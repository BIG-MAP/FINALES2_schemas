from typing import Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import CellInfo, Location

class CapacityCyclingInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `capacity` - `cycling`
    """

    cycling_protocol:str = Field(
        description="Name of a standardized test protocol (i.e. BIG-MAP-Cycling)."
        )
    number_cycles:int = Field(
        description="The number of cycles the test shoudl run through after formation."
        )
    cell_info:CellInfo = Field(
        description="Information about the cell provided by AutoBass."
        )
    location:Location = Field(
        description="Physical location where the cycler is."
        )
    reservation_number:str = Field(
        description=("The ID assigned to the reservation when requesting "
                     "free channels.")
    )
    I_max:Optional[float] = Field(
        description="Maximum current value in ampere."
        )
    V_max:Optional[float] = Field(
        description="Maximum Voltage value in Volt."
        )
    V_min:Optional[float] = Field(
        description="Minimum Voltage value in Volt."
        )
    capacity:Optional[float] = Field(
        description="theoretical/experimental capacity in Ah."
        )

    c_rate_charge_formation:Optional[float] = Field(
        description="C-rate of charging in formation process"
        )
    c_rate_discharge_formation:Optional[float] = Field(
        description="C-rate of discharging in formation process"
        )
    CV_I_cutoff_formation:Optional[float] = Field(
        description="current cutoff value in A for the constant voltage step in formation process"
        )
    repetions_formation_cycle:Optional[int] = Field(
        description="Number of formation cycles"
        )
    cycling_V_max:Optional[float] = Field(
        description="max. Voltage of battery during cycling in V"
        )
    cycling_V_min:Optional[float] = Field(
        description="min. Voltage of battery during cycling in V"
        )
    c_rate_charge:Optional[float] = Field(
        description="C-rate of charging"
        )
    c_rate_discharge:Optional[float] = Field(
        description="C-rate of discharging"
        )
    CV_I_cutoff:Optional[float] = Field(
        description="current cutoff value in A for the constant voltage step"
        )
