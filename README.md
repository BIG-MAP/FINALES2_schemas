# FINALES2 schemas

The FINALES server is able to dynamically incorporate new measurements as they become available.
They are stored in a database in which each entry corresponds to a given quantity, method for obtaining the quantity, and a json specifying the expected schema of the parameters for obtaining this quantity.
Since generating and handling these schemas is non-trivial, this package allows users to write them first as Pydantic classes (that they can then use in their tenants) and export them in the format that the finales server understands and uses to validate their submissions.

If you want to add a new quantity, you should define the parameters that are expected as a Pydantic class in the `/parameter_classes` and expose it in the `__init__.py` there (import it and add it to `__all__`).
Then you should go to the `/generate_schemas.py` script, import it there and use it to generate the corresponding parameter schema and serialized quantities.
Finally, run the script to generate the files: you can then commit your changes to this repository, but most importantly you must send the serialized quantities to the admin of the finales server so that they can add it to the quantity table.