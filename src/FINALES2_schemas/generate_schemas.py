import json
import pathlib

from parameter_classes.conductivity.shared_classes import ConductivityInput
from parameter_classes.conductivity.two_electrode import ConductivityTwoElectrodeOutput
from parameter_classes.conductivity.molecular_dynamics import ConductivityMolecularDynamicsOutput
from parameter_classes.degradationEOL.shared_classes import DegradationEOLInput
from parameter_classes.degradationEOL.degradation_model import DegradationEOLDegradationModelOutput
from parameter_classes.density.shared_classes import DensityInput
from parameter_classes.density.molecular_dynamics import DensityMolecularDynamicsOutput
from parameter_classes.density.vibrating_tube_densimetry import DensityVibratingTubeDensimetryOutput
from parameter_classes.viscosity.shared_classes import ViscosityInput, ViscosityOutput

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
    generate_schema(DensityVibratingTubeDensimetryOutput, BASEPATH_SCHEMAS / 'density/vibrating_tube_densimetry_output.json')
    generate_schema(DensityMolecularDynamicsOutput, BASEPATH_SCHEMAS / 'density/molecular_dynamics_output.json')
    generate_schema(ConductivityInput, BASEPATH_SCHEMAS / 'conductivity/conductivity_input.json')
    generate_schema(ConductivityTwoElectrodeOutput, BASEPATH_SCHEMAS / 'conductivity/two_electrode_output.json')
    generate_schema(DegradationEOLInput, BASEPATH_SCHEMAS / 'degradationEOL/degradationEOL_input.json')
    generate_schema(DegradationEOLDegradationModelOutput, BASEPATH_SCHEMAS / 'degradationEOL/degradation_model_output')

    quantity_path = BASEPATH_QUANTITIES / 'conductivity' / 'two_electrode.json'
    generate_quantity('conductivity', 'two_electrode', ConductivityInput, ConductivityTwoElectrodeOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'conductivity' / 'molecular_dynamics.json'
    generate_quantity('conductivity', 'molecular_dynamics', ConductivityInput, ConductivityMolecularDynamicsOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'vibrating_tube_densimetry.json'
    generate_quantity('density', 'vibrating_tube_densimetry', DensityInput, DensityVibratingTubeDensimetryOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'density' / 'molecular_dynamics_simulation.json'
    generate_quantity('density', 'molecular_dynamics', DensityInput, DensityMolecularDynamicsOutput, quantity_path)

    quantity_path = BASEPATH_QUANTITIES / 'degradationEOL' / 'degradation_model.json'
    generate_quantity('degradationEOL', 'degradation_model', DegradationEOLInput, DegradationEOLDegradationModelOutput, quantity_path)