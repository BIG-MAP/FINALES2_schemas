from pydantic import BaseModel, Field

class Chemical(BaseModel):
    """Subclass"""
    name:str = Field(
        description="A human readable name of the chemical."
    )
    smiles:str = Field(
        description="A SMILES string representing the chemical."
    )
    InChIKey:str = Field(
        description=("The hashed standard International Chemical Identifier of "
                    "the chemical to ensure machine-readability.")
    )
