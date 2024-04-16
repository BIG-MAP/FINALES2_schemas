# FINALES2 schemas

The FINALES server is able to dynamically incorporate new measurements as they become available. They are stored in a database in which each entry corresponds to a given quantity, a method for obtaining the quantity, and a JSON file specifying the expected schema of the parameters for obtaining this quantity. Since generating and handling these schemas is non-trivial, this package allows users to write them first as Pydantic classes (that they can then use in their tenants) and export them in the format that the FINALES can process and uses to validate submissions.

## The structure of this repository
The structure of this repository reflects different levels of generality. This comprises classes and schemas, which can be used in the whole MAP, such, which can be shared among different methods providing the same quantity and classes and schemas, which are specific to one method. It should be taken care, that the classes and schemas are reused, wherever this is reasonably possible to avoid many different schemas emerging conveying the same information.

### classes_common
Classes, which can be shared among a large fraction of the tenants, are collected in the ``classes_common`` directory. These classes shall be used, wherever the respective input, e.g. a formulation of an electrolyte is needed.

### classes_input
This directory collects all the classes used as inputs for methods related to quantities. Each quantity has its own subdirectory. The ``__init__.py`` files in each subdirectory collect all the classes defined in the respective directory for this quantity to facilitate imports and make them more independent of the internal structure of the directory. If a folder for a quantity contains a file called ``minimal_input.py``, this file defines an input, which should be shared among different methods providing this quantity to the furthest extend possible. If a method needs additional inputs, it can create its own input file using the class defined in ``minimal_input.py`` and add further information. Creating a completely independent input class should be the last resort when defining input classes. Method-specific input classes are collected in files labelled as ``<method name>.py`` in the directory of the respective quantity.

### classes_output
The structure of the ``classes_output`` directory is analogous to the ``classes_input`` directory. For the generation of method-specific output classes the same rules as for the input classes apply.

### serialized_quantities
This directory contains a subdirectory for every quantity. These subdirectories contain files with labels according to ``<method name>.json``. These files provide a JSON-schema describing the input and output of the method to which they belong. These files are auto-generated by the ``generate_schemas.py`` script, which will be described further below. The schemas contained in this directory are saved in the ``Quantities`` table in the FINALES database and serve as a means to validate the correct format of inputs and outputs for the communication with the FINALES.

### generate_schemas.py
This file generates the JSON-schemas in the ``serialized_quantities`` directory. The way of importing the classes can be seen at the top of this file. After the line ``if __name__ == "__main__":``, one set of two lines generates the file for one capability. The input parameters for the ``generate_quantity`` method are the name of the quantity, the name of the method, the input schema and the output schema to use and the path to save the file.

# Usage of the classes and schemas
This section describes how the classes and schemas contained in this repository can be used.

## Use of the classes
The classes defined in this repository may be used by importing them from the ``classes_common``, ``classes_input`` and ``classes_output``, respectively. This may be useful in the implementation of tenants.

## Use of the schemas
The schemas can be used for understanding the data structures as a human or for validating the data structures sent to and received from FINALES. Both options will briefly be explained in the following.
The schemas for the inputs can be found in the JSON files in the key ``json_schema_specifications``. The schemas for the output can be found in the key ``json_schema_result_output```.

### Validation
For programmatically validating a data structure, the schemas may be used as follows:
If you would like to validate, that an input ``specific_params = {...}`` for a certain method matches the required input schema for this method, get the capability from FINALES using the endpoint ``/capabilities/`` to retrieve all capabilities registered with FINALES and search for the one corresponding to the quantity and method of interest. From the capability, the schema for the input can be obtained from ``schema_specs = capability_object['json_schema_specifications']``. The data structure can be validated using the ``validate`` method from the ``jsonschema`` package by executing ``validate(instance=specific_params, schema=schema_specs)``.

### Understanding the data structures
To understand the data structures as a human, you can request all capabilities from FINALES using the endpoint ``/capabilities/``, filtering for the desired quantity and method and check the schema in the ``json_schema_specifications`` key for the input and ``json_schema_result_output`` key for the output, respectively. Alternatively, the schemas can also be obtained from this repository as they are loaded to FINALES dynamically. These schemas may be inspected as they are or using a visualization tool like e.g. [this](https://json-schema-visualizer.netlify.app/).

## How to add new schemas for my quantity and method
The procedure of how to add new schema classes is given in the [Wiki](https://github.com/BIG-MAP/FINALES2_schemas/wiki/Adding-new-schemas).

## Acknowledgements

This project has received funding from the European Union’s [Horizon 2020 research and innovation programme](https://ec.europa.eu/programmes/horizon2020/en) under grant agreement [No 957189](https://cordis.europa.eu/project/id/957189).
