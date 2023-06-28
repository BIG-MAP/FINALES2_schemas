from pydantic import BaseModel, Field

class MethodMeta(BaseModel):
    """Additional information obtained from a method summarizing information, whether 
    the method was successfully run and what the rating for the returned data is.
    """
    success:bool = Field(
        description=("This reports, if the method finished successfully.")
    )
    rating:int = Field(
        description=("This field serves to rate the quality of the result from the "
                     "tenant side. It shall serve as a support for the recieving party "
                     "upon evaluating the trustworthiness of the result. It shall range "
                     "from 0 (lowest) to 5 (highest).")
    )
