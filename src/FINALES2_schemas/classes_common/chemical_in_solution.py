from pydantic import BaseModel, Field
from .chemical import Chemical

class ChemicalInSolution(BaseModel):
    chemical:Chemical = Field(
        description="The chemical, which shall be described as a component in a solution ."
    )
    # The type of the fraction, i.e. whether it is a volume, molar, mass or other fraction
    # is not recorded here, but in the formulation object, because formulations are
    # expected to be reported using the same type of fraction for all of the chemicals.
    # Please refer to the Chemicals class to refer to chemicals when they are not within
    # the context of a formulation.
    fraction:float = Field(
        description="The unitless fraction of the chemical in the total of the mixture."
    )