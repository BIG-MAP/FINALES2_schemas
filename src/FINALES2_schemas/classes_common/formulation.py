from pydantic import BaseModel, Field
from .chemical import Chemical

class Formulation(BaseModel):
    """Subclass"""
    # The chemicals and the chemical_composition are separated in this class to allow
    # for further information being included in the chemical objects. Currently, they
    # have a SMILES string additional to the InChIKey. The SMILES string is used as an
    # input to some computational tenants and is therefore needed. Hence, the list of
    # chemicals cannot simply be extracted from the keys of the chemical_composition
    # dictionary and the chemicals are kept as separate objects.
    chemicals:dict[str, Chemical] = Field(
        description=("A dictionary of the chemicals included in the formulation. "
                    "InChIKeys as keys and corresponding Chemical objects as values.")
    )
    chemical_composition:dict[str, float] = Field(
        description=("A dictionary with the InChIKey as the key and the respective "
                    "unitless fraction of the chemical in the total of the mixture as a "
                     "value.")
    )
    fraction_type:str = Field(
        description=("A string defining, what kind of a fraction is "
                    "given in the formulation. This can be for example molar fractions, "
                    "volume fractions, mass fractions,.... At the moment only molar "
                    "fractions are supported.")
    )
