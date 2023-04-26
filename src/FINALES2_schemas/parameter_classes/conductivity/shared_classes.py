from pydantic import BaseModel, Field
from typing import Optional

from parameter_classes.common_subclasses.formulation import Formulation
from parameter_classes.common_subclasses.mathod_meta import MethodMeta
from parameter_classes.common_subclasses.unit_registry import unit_registry

class ConductivityInput(BaseModel):
    """Parameters used by the quantities
    'conductivity' - 'twoElectrodeMeasuringCell'
    'conductivity' - 'molecularDynamicsSimulation'

    :param BaseModel: used to ensure, that the class can be checked for the types
    :type BaseModel: pydantic.BaseModel
    """
    formulation:Formulation = Field(
        description=("This is a formulation defining the Chemicals contained in the "
                    "sample and their fraction in the total mixture.")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description=("This is the temperature of the measuring cell or used in a "
                    "simulation. It shall be given in the unit kelvin.")
    )

class ConductivityOutput(BaseModel):
    """
    Results returned from the following quantities:
    'conductivity' - 'twoElectrodeMeasuringCell'
    'conductivity' - 'molecularDynamicsSimulation'
    """
    values:list[float] = Field(
        unit=str(unit_registry.siemens * unit_registry.m ** -1),
        description=("The values determined for the conductivity given in S/m.")
    )
    temperature: Optional[float] = Field(
        unit=str(unit_registry.kelvin),
        description=("This is the actual temperature of the measuring cell or used in a "
                    "simulation. It shall be given in the unit kelvin.")
    )
    meta:MethodMeta = Field(
        description=("This field provides information regarding the reliability of the "
                     "reported data. E.g. the success of the method for this quantity "
                     "and the rating of the data. This is for this specific quantity, "
                     "because a single method could fail individually for different "
                     "quantities.")
    )