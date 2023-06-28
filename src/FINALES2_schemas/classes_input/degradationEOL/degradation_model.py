from pydantic import BaseModel, Field
from FINALES2_schemas.classes_common import BatteryChemistry, unit_registry

class DegradationModelInput(BaseModel):
    """The parameters used by the following method
    'degradationEOL' - degradationModel

    :param BaseModel: _description_
    :type BaseModel: _type_
    """

    input_cycles:list = Field(
        description=("The capacities for the input cycles provided as an input to the model.")
    )
    delta_coulombic_efficiency:float = Field(
        description=("The difference in coulombic efficiency between cycle x and 10.")
    )
    voltage_gap_charge_discharge:float = Field(
        unit=str(unit_registry.V),
        description=("The difference of the voltage gap between charge and discharge "
                     "between cycle x and 10. "
                     f"Unit: {str(unit_registry.V)}")
    )
    capacity_vector_variance:float = Field(
        description=("The variance of the difference between the Q(V) curves between "
                     "cycle x and 10.")
    )
