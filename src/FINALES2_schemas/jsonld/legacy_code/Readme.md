# Ontology Mappings and JSON-LD
The purpose is to map keys and values in the results.json files output from FINALES, to concepts in EMMO-based ontologies.

## Main methodology
The main methodology can be summarized as follows:  
1. Develop a mapping file, contianing the keys in the JSON file, and the URI of the corresponding concept in the ontology. For example look at `./mapping.json`
2. Re-build the results.json file into a human-friendly hierarchy of json-ld objects. 
    * JSON-LD objects differ from traditional JSON objects, as each object has a `@type` mapped to an ontology URI, and an `@id`, which could be itself an UUID or extend the UUID of the parent node (the UUID of the whole results.json)
    * For instance, the file `./conductivity_two_electrode.json` is a JSON-LD file with a manually crafted hierarchy of JSON-LD objects. Copy the contents of the json file and paste them into the [JSON-LD playground](https://json-ld.org/playground/), and go to the tab "Visualized". It will show the hierarchy of JSON-LD objects.
    * However, this hierarchy is hard to reproduce programatically from the results.json. Other hierarchies are possible, as long as they reflect the right nesting among JSON-LD objects.

> NOTE: the mapping file mapping.json depends on the hierarchy, because the script should be able to read from the mapping file not only the ontology URIs but also how to assemble the JSON-LD objects into the desired hierarchy.

3. Develop a script that uses results.json to populate the human-friendly hierarchy of JSON-LD objects.


## To do

* Develop a script to read the results.json and mappings.json and build the JSON-LD file. Current efforts at prototyping the script can be found at `./prototyping.ipynb`.
   