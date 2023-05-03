from pydantic import BaseModel, Field

class MethodMeta(BaseModel):
    success:bool = Field(
        description=("This reports, if the method finished successfully.")
    )
    rating:int = Field(
        description=("This field serves to rate the quality of the result from the "
                     "tenant side. It shall serve as a support for the recieving party "
                     "upon evaluating the trustworthiness of the result. It shall range "
                     "from 0 (lowest) to 5 (highest).")
    )
