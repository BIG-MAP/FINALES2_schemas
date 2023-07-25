from pydantic import BaseModel, Field

from FINALES2_schemas.classes_common import unit_registry

class RDFOutput(BaseModel):
    """
    Results returned from the following quantities:
    'radial_density_function' - 'molecular_dynamics_RDF'
    """

    radius:list[float] = Field(
        unit=f"{unit_registry.m}",
        description=("The radius at which atoms of the respecive species appear.")
    )
    pair_title:list[str] = Field(
        description=("The names of the pairs of atoms considered.")
    )
    RDF:list[list[float]] = Field(
        description=("A collection of the RDF for each pair of atoms.")
    )
    cell_volume:float = Field(
        unit=f"{unit_registry.nm}",
        description=(f"The volume of the cell under concideration. Unit: {unit_registry.nm}")
    )
    cell_formula:str = Field(
        description=("The composition of the considered cell reporting the "
                     "number of atoms per type contained in the cell, "
                     "e.g. Li16 O600 P16 F96 C600 H600")
    )