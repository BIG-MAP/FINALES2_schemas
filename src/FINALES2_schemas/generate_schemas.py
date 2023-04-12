import json
import pathlib

from parameter_classes import DensityCommon

BASEPATH = pathlib.Path(__file__).parent.resolve()
BASEPATH_SCHEMAS = BASEPATH / 'parameter_schemas'
BASEPATH_QUANTITIES = BASEPATH / 'serialized_quantities'

def generate_schema(pydantic_class, filepath):
    """Generates the schema from a pydantic class and stores it in a file."""
    with open(filepath, 'w') as fileobj:
        fileobj.write(pydantic_class.schema_json(indent=2))

def generate_quantity(quantity_name, method_name, pydantic_class, filepath):
    """Generates the schema from a pydantic class and stores it in a file."""
    dictobj = {
        'quantity': quantity_name,
        'method': method_name,
        'specifications': pydantic_class.schema(),
        'is_active': True,
    }
    with open(filepath, 'w') as fileobj:
        json.dump(dictobj, fileobj, indent=2)

if __name__ == "__main__":
    generate_schema(DensityCommon, BASEPATH_SCHEMAS / 'density_common.json')

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'vibrating_tube_densimetry.json'
    generate_quantity('density', 'vibratingTubeDensimetry', DensityCommon, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'molecular_dynamics_simulation.json'
    generate_quantity('density', 'molecularDynamicsSimulation', DensityCommon, quantity_path)
