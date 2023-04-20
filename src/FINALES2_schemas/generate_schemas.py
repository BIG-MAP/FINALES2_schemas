import json
import pathlib

from parameter_classes.density.density import DensityInput
from parameter_classes.density.density_molecularDynamicsSimulation import DensityMolecularDynamicsSimulationOutput
from parameter_classes.density.density_vibratingTubeDensimetry import DensityVibratingTubeDensimetryOutput
from parameter_classes.conductivity.conductivity_twoElectrodeMeasuringCell import ConductivityTwoElectrodeMeasurementCellOutput
from parameter_classes.conductivity.conductivity import ConductivityInput

BASEPATH = pathlib.Path(__file__).parent.resolve()
BASEPATH_SCHEMAS = BASEPATH / 'parameter_schemas'
BASEPATH_QUANTITIES = BASEPATH / 'serialized_quantities'

def generate_schema(pydantic_class, filepath):
    """Generates the schema from a pydantic class and stores it in a file."""
    with open(filepath, 'w') as fileobj:
        fileobj.write(pydantic_class.schema_json(indent=2))

def generate_quantity(quantity_name, method_name, input_schema, output_schema, filepath):
    """Generates the schema from a pydantic class and stores it in a file."""
    dictobj = {
        'quantity': quantity_name,
        'method': method_name,
        'json_schema_specifications': input_schema.schema(),
        'json_schema_result_output': output_schema.schema(),        
        'is_active': True,
    }
    with open(filepath, 'w') as fileobj:
        json.dump(dictobj, fileobj, indent=2)

if __name__ == "__main__":
    generate_schema(DensityInput, BASEPATH_SCHEMAS / 'density/density_input.json')
    generate_schema(DensityVibratingTubeDensimetryOutput, BASEPATH_SCHEMAS / 'density/density_vibrating_tube_densimetry_output.json')
    generate_schema(ConductivityTwoElectrodeMeasurementCellOutput, BASEPATH_SCHEMAS / 'conductivity/conductivity_two_electrode_measuring_cell.json')

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'vibrating_tube_densimetry.json'
    generate_quantity('density', 'vibratingTubeDensimetry', DensityInput, DensityVibratingTubeDensimetryOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'molecular_dynamics_simulation.json'
    generate_quantity('density', 'molecularDynamicsSimulation', DensityInput, DensityMolecularDynamicsSimulationOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'conductivity' / 'two_electrode_measuring_cell.json'
    print(quantity_path)
    generate_quantity('conductivity', 'twoElectrodeMeasuringCell', ConductivityInput, ConductivityTwoElectrodeMeasurementCellOutput, quantity_path)
