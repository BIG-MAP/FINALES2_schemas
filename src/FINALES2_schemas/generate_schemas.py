import json
import pathlib

from classes_input import (conductivity as conductivity_input,
                           degradationEOL as degradationEOL_input,
                           density as density_input,
                           viscosity as viscostiy_input, 
                           cell_assembly as assembly_input)
from classes_output import (conductivity as conductivity_output,
                           degradationEOL as degradationEOL_output,
                           density as density_output,
                           viscosity as viscostiy_output,
                           cell_assembly as assembly_output)

BASEPATH = pathlib.Path(__file__).parent.resolve()
BASEPATH_QUANTITIES = BASEPATH / 'serialized_quantities'

# This function is not used at the moment, but it is kept here for easy reactivation in the future
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
    quantity_path = BASEPATH_QUANTITIES / 'conductivity' / 'two_electrode.json'
    generate_quantity('conductivity', 'two_electrode', conductivity_input.ConductivityInput, conductivity_output.TwoElectrodeOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'conductivity' / 'molecular_dynamics.json'
    generate_quantity('conductivity', 'molecular_dynamics', conductivity_input.ConductivityInput, conductivity_output.MolecularDynamicsOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'vibrating_tube_densimetry.json'
    generate_quantity('density', 'vibrating_tube_densimetry', density_input.DensityInput, density_output.VibratingTubeDensimetryOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'molecular_dynamics_simulation.json'
    generate_quantity('density', 'molecular_dynamics', density_input.DensityInput, density_output.MolecularDynamicsOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'degradationEOL' / 'degradation_model.json'
    generate_quantity('degradationEOL', 'degradation_model', degradationEOL_input.DegradationModelInput, degradationEOL_output.DegradationModelOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'cell_assembly' / 'cell_assembly.json'
    generate_quantity('cell_assembly', 'autobass_assembly', assembly_input.AssemblyInput, assembly_output.AutoBASSOutput, quantity_path)