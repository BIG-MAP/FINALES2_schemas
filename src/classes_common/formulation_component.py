from pydantic import BaseModel, Field
from .chemical import Chemical

class FormulationComponent(BaseModel):
    """This class shall be used when referring to chemicals as a component in a formulation.
    When assembling a formulation based on FormulationComponents, consider, that it
    might be required to use the same fraction type for all the chemicals.
    """
    chemical:Chemical = Field(
        description="The chemical, which shall be described as a component in a solution ."
    )
    fraction:float = Field(
        description="The unitless fraction of the chemical in the total of the mixture."
    )
    fraction_type:str = Field(
        description=("A string defining, what kind of a fraction is "
                "given in the formulation. This can be for example molar fractions, "
                "volume fractions, mass fractions,.... At the moment only molar "
                "fractions are supported.")
    )
