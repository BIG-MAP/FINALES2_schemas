from pydantic import BaseModel, Field
from .chemical import Chemical
from .fraction_type import FractionType

class Formulation(BaseModel):
    """Subclass"""
    chemicals:dict[str, Chemical] = Field(
        description=("A dictionary of the chemicals included in the formulation. "
                    "InChIKeys as keys and corresponding Chemical objects as values.")
    )
    chemical_composition:dict[str, float] = Field(
        description=("A dictionary with the InChIKey as the key and the respective "
                    "unitless fraction of the chemical in the total of the mixture as a "
                     "value.")
    )
    fractiontype:FractionType = Field(
        description=("A value of an enumeration defining, what kind of a fraction is "
                    "given in the formulation. This can be for example molar fractions, "
                    "volume fractions, mass fractions,.... At the moment only molar f"
                    "ractions are supported.")
    )
