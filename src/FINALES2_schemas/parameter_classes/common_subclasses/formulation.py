from pydantic import BaseModel, Field
from uuid import UUID
from parameter_classes.common_subclasses.chemical import Chemical
from parameter_classes.common_subclasses.fraction_type import FractionType

class Formulation(BaseModel):
    """Subclass"""
    name:str = Field(
        description="A human readable name of the formulation."
    )
    uuid:UUID = Field(
        description="A unique identifier assigned to this formulation in this run."
    )
    chemicals:dict[str, Chemical] = Field(
        description=("A dictionary of the chemicals included in the formulation. "
                    "InChIKeys as keys and corresponding Chemical objects as values.")
    )
    chemicalComposition:dict[str, float] = Field(
        description=("A dictionary with the InChIKey as the key and the respective "
                    "unitless fraction of the chemical in the total of the mixture as a "
                     "value.")
    )
    fractionType:FractionType = Field(
        description=("A value of an enumeration defining, what kind of a fraction is "
                    "given in the formulation. This can be for example molar fractions, "
                    "volume fractions, mass fractions,.... At the moment only molar f"
                    "ractions are supported.")
    )
