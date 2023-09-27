from typing import List, Optional
from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import unit_registry, CellInfo

class CapacityCyclingOutput(BaseModel):
    """
    Results returned from the following quantities:
    `capacity` - `cycling`
    """
    capacity_list: List[float] = Field(
        units=str(unit_registry.Ah),
        description="A list with calculated capacities in Ah for charge and discharge alternately."
    )
    channel_list: List[int] = Field(
        description="A list with the channels used for cycling."
    )
    cell_info:CellInfo = Field(
        description="Information about the cell provided by AutoBass."
        )
    delta_coulombic_efficiency:Optional[float] = Field(
        default=None,
        description=("The difference in coulombic efficiency between cycle x and 10. "
                     "As in the input schema of the degradation_model method.")
    )
    voltage_gap_charge_discharge:Optional[float] = Field(
        default=None,
        unit=str(unit_registry.V),
        description=("The difference of the voltage gap between charge and discharge "
                     "between cycle x and 10. As in the input schema of the "
                     "degradation_model method."
                     f"Unit: {str(unit_registry.V)}")
    )
    capacity_vector_variance:Optional[float] = Field(
        default=None,
        description=("The variance of the difference between the Q(V) curves between "
                     "cycle x and 10. As in the input schema of the "
                     "degradation_model method.")
    )