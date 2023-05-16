from pydantic import BaseModel, Field
from .chemical import Chemical
from .chemical_in_solution import ChemicalInSolution

class Formulation(BaseModel):
    """Subclass"""
    chemicals:list[ChemicalInSolution] = Field(
        description=("A list of the chemicals included in the formulation. The fraction "
                    "of the respective chemical in the solution is contained in each"
                    "of the elements in the list.")
    )
    # This defines the type of the fraction, which is given for each chemical in the
    # formulation. All the fractions in the chemicals must correspond to this type. 
    fraction_type:str = Field(
        description=("A string defining, what kind of a fraction is "
                    "given in the formulation. This can be for example molar fractions, "
                    "volume fractions, mass fractions,.... At the moment only molar "
                    "fractions are supported.")
    )
