from pydantic import BaseModel, Field
from ..common_subclasses.battery_chemistry import BatteryChemistry
from ..common_subclasses.unit_registry import unit_registry

class DegradationEOLInput(BaseModel):
    """The parameters used by the following method
    'degradationEOL' - degradationModel

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    chemistry:BatteryChemistry = Field(
        description=("The description of the chemicals involved in all the battery cell.")
    )
    inputCycles:int = Field(
        description=("The number of cycles provided as an input to the model.")
    )
    averageChargingRate:float = Field(
        unit=unit_registry.h **-1,
        description=("The average C-rate used for charging of the cell in the cycles "
                     "provided as an input.")
    )
    maximumChargingRate:float = Field(
        unit=unit_registry.h **-1,
        description=("The maximum C-rate used for charging of the cell in the cycles "
                     "provided as an input.")
    )
    minimumChargingRate:float = Field(
        unit=unit_registry.h **-1,
        description=("The minimum C-rate used for charging of the cell in the cycles "
                     "provided as an input.")
    )
    deltaCoulombicEfficiency:float = Field(
        description=("The difference in coulombic efficiency between cycle x and 10.")
    )
    voltageGapChargeDischarge:float = Field(
        unit=unit_registry.v,
        description=("The difference of the voltage gap between charge and discharge "
                     "between cycle x and 10.")
    )
    capacityVectorVariance:float = Field(
        description=("The variance of the difference between the Q(V) curves between "
                     "cycle x and 10.")
    )

class DegradationEOLOutput(BaseModel):
    """Results returned from the following quantities:
    'degradationEOL' - degradationModel

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    endOfLife:int = Field(
        description=("The predicted end of life for the cell.")
    )
    endOfLifeUncertainty:float = Field(
        description=("The uncertainty of the predicted end of life for the cell.")
    )
    capacityTrajectory:list[float] = Field(
        unit=unit_registry.mAh,
        description=("The predicted capacity evolution for future cycles.")
    )
    capacityTrajectoryUncertainty:list[float] = Field(
        unit=unit_registry.mAh,
        description=("The uncertainty associated with each datapoint in the predicted "
                     "capacity evolution.")
    )