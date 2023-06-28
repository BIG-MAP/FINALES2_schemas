from pydantic import BaseModel, Field
from FINALES2_schemas.src.classes_common import MethodMeta, unit_registry
from typing import List

class DegradationEOLOutput(BaseModel):
    """Results returned from the following quantities:
    'degradationEOL' - degradationModel

    :param BaseModel: _description_
    :type BaseModel: _type_
    """
    end_of_life:int = Field(
        description=("The predicted end of life for the cell.")
    )
    end_of_life_uncertainty:float = Field(
        description=("The uncertainty of the predicted end of life for the cell.")
    )
    capacity_trajectory:List[float] = Field(
        unit=str(unit_registry.mAh),
        description=("The predicted capacity evolution for future cycles. "
                     f"Unit: {str(unit_registry.mAh)}")
    )
    capacity_trajectory_uncertainty:List[float] = Field(
        unit=str(unit_registry.mAh),
        description=("The uncertainty associated with each datapoint in the predicted "
                     "capacity evolution. "
                     f"Unit: {str(unit_registry.mAh)}")
    )
    meta:MethodMeta = Field(
        description=("This field provides information regarding the reliability of the "
                     "reported data. E.g. the success of the method for this quantity "
                     "and the rating of the data. This is for this specific quantity, "
                     "because a single method could fail individually for different "
                     "quantities. It is not included in the RunInfo as one run may "
                     "generate data for different quantities, for which the methods "
                     "may fail individually.")
    )