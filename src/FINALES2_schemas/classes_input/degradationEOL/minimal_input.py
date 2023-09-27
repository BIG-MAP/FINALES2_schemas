from pydantic import BaseModel, Field
from typing import Optional
from FINALES2_schemas.classes_common import BatteryChemistry, unit_registry, CellInfo

class DegradationEOLInput(BaseModel):
    """The parameters used by the following method
    'degradationEOL' - degradationModel
    """
    battery_chemistry:BatteryChemistry = Field(
        description=("The description of the chemicals involved in all the battery cell.")
    )
    input_cycles:Optional[list[float]] = Field(
        default=None,
        description=("A list of the capacity values associated with the cycles used "
                     "as the input for the model.")
    )
    average_charging_rate:Optional[float] = Field(
        default=None,
        unit=str(unit_registry.h **-1),
        description=("The average C-rate used for charging of the cell in the cycles "
                     "provided as an input. "
                     f"Unit: {str(unit_registry.h **-1)}")
    )
    maximum_charging_rate:Optional[float] = Field(
        default=None,
        unit=str(unit_registry.h **-1),
        description=("The maximum C-rate used for charging of the cell in the cycles "
                     "provided as an input. "
                     f"Unit: {str(unit_registry.h **-1)}")
    )
    minimum_charging_rate:Optional[float] = Field(
        default=None,
        unit=str(unit_registry.h **-1),
        description=("The minimum C-rate used for charging of the cell in the cycles "
                     "provided as an input. "
                     f"Unit: {str(unit_registry.h **-1)}")
    )
    delta_coulombic_efficiency:Optional[float] = Field(
        default=None,
        description=("The difference in coulombic efficiency between cycle x and 10.")
    )
    voltage_gap_charge_discharge:Optional[float] = Field(
        default=None,
        unit=str(unit_registry.V),
        description=("The difference of the voltage gap between charge and discharge "
                     "between cycle x and 10. "
                     f"Unit: {str(unit_registry.V)}")
    )
    capacity_vector_variance:Optional[float] = Field(
        default=None,
        description=("The variance of the difference between the Q(V) curves between "
                     "cycle x and 10.")
    )
    cell_info:CellInfo = Field(
        description="Information about the cell provided by AutoBass."
        )
