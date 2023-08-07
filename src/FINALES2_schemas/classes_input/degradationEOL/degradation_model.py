from pydantic import BaseModel, Field
from typing import Optional
from FINALES2_schemas.classes_common import BatteryChemistry, unit_registry

class DegradationModelInput(BaseModel):
    """The parameters used by the following method
    'degradationEOL' - degradationModel

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    chemistry:BatteryChemistry = Field(
        description=("The description of the chemicals involved in all the battery cell.")
    )
    input_cycles:Optional[list[float]] = Field(
        description=("The number of cycles provided as an input to the model.")
    )
    average_charging_rate:Optional[float] = Field(
        unit=str(unit_registry.h **-1),
        description=("The average C-rate used for charging of the cell in the cycles "
                     "provided as an input. "
                     f"Unit: {str(unit_registry.h **-1)}")
    )
    maximum_charging_rate:Optional[float] = Field(
        unit=str(unit_registry.h **-1),
        description=("The maximum C-rate used for charging of the cell in the cycles "
                     "provided as an input. "
                     f"Unit: {str(unit_registry.h **-1)}")
    )
    minimum_charging_rate:Optional[float] = Field(
        unit=str(unit_registry.h **-1),
        description=("The minimum C-rate used for charging of the cell in the cycles "
                     "provided as an input. "
                     f"Unit: {str(unit_registry.h **-1)}")
    )
    delta_coulombic_efficiency:Optional[float] = Field(
        description=("The difference in coulombic efficiency between cycle x and 10.")
    )
    voltage_gap_charge_discharge:Optional[float] = Field(
        unit=str(unit_registry.V),
        description=("The difference of the voltage gap between charge and discharge "
                     "between cycle x and 10. "
                     f"Unit: {str(unit_registry.V)}")
    )
    capacity_vector_variance:Optional[float] = Field(
        description=("The variance of the difference between the Q(V) curves between "
                     "cycle x and 10.")
    )