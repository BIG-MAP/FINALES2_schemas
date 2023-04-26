from pydantic import BaseModel, Field
from enum import Enum

class FractionType(str, Enum):
    """Fraction types used to specify formulations"""
    molPerMol = "molPerMol"