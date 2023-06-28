from typing import List, Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common.cell_info import CellInfo


class CapacityCyclingInput(BaseModel):
    """
    Parameters to be used with the following quantities:
    `Capacities` 
    """
    cycling_protocoll: str = Field(description="Name of a standardized testprotocoll(i.e BIG-MAP-Cycling).")
    number_cycles: int = Field(description="The number of cycles the test shoudl run through after formation.")
    cell_info : CellInfo = Field(description="Information about the cell provided by AutoBass.")
    location : str = Field(description="Physical location where the cycler is.")

    Imax:Optional[float] = Field(description="Maximum current value in ampere.")
    Vmax:Optional[float] = Field(description="Maximum Voltage value in Volt.")
    Vmin:Optional[float] = Field(description="Minimum Voltage value in Volt.")
    Capacity: Optional[float] = Field(description="theoretical/experimental capacity in Ah.")

    crate_charge_formation : Optional[float] = Field(description="C-rate of charging in formation process")
    crate_discharge_formation: Optional[float] = Field(description="C-rate of discharging in formation process")
    CV_Icutoff_formation: Optional[float] = Field(description="current cutoff value in A for the constant voltage step in formation process")
    repetions_formationcycle: Optional[int] = Field(description="Number of formation cycles")

    cycling_Vmax: Optional[float] = Field(description="max. Voltage of battery during cycling in V")
    cycling_Vmin: Optional[float] = Field(description="min. Voltage of battery during cycling in V")
    crate_charge: Optional[float] = Field(description="C-rate of charging")
    crate_discharge: Optional[float] = Field(description="C-rate of discharging")
    CV_Icutoff: Optional[float] = Field(description="current cutoff value in A for the constant voltage step")
