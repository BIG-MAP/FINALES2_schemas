
from rdflib import Graph, Literal, BNode, RDF, URIRef



def get_json_object_uuid(json_object:dict, mapping:dict):
    #if key is uuid, use value as uuid of the subject node. Ex "uuid": "ce83md"
    for key, value in json_object.items():
        if key in mapping["uuids"]:
            return value
        else:
            return None



        
def replace_blank_node(g, blank_node, uriref):
    # Add new triples with the new IRI as the subject, while keeping the original triples
    for s, p, o in g.triples((blank_node, None, None)):
        g.add((uriref, p, o))

    # Remove the original triples with the blank node as the subject
    g.remove((blank_node, None, None))

    return g





def process_object(json_object:dict, 
                   g:Graph, 
                   mapping:dict, 
                   json_object_type=None, 
                   temp_subject = None):


    ##############      ASSIGN THE SUBJECT     ################
    uuid = get_json_object_uuid(json_object, mapping)
    if uuid:
        subject = URIRef(uuid)
        g = replace_blank_node(g, temp_subject, subject)
    else:
        subject = temp_subject


    ##############      ASSIGN THE TYPE     ################
    if json_object_type:
        g.add((subject, RDF.type, json_object_type))


    ##############      ADD ATTRIBUTES     ################

    for key, value in json_object.items():



        #### If key is mapped to an entity...
        if key in mapping["entities"].keys():

            ####... and the entity does not have a type, add it as a literal
            if isinstance(mapping["entities"][key], str):  

                predicate = URIRef(mapping["entities"][key])
                g.add((subject, predicate, Literal(value)))


            ####... otherwise if the entity has a type....
            elif isinstance(mapping["entities"][key], dict): 

                predicate = URIRef(mapping["entities"][key]["iri"])
                object_type = URIRef(mapping["entities"][key]["type"])

                ###... and the value is an object, send back recurvisely
                if isinstance(value, dict):
                    temp_object = BNode()
                    g.add((subject, predicate, temp_object))
                    process_object(value, g, mapping, object_type, temp_object)

                ####... otherwise if the value is a list...
                elif isinstance(value,list):
                    for element in value:

                        ### ...and the elements of the list are objects, then send back recursively.
                        if isinstance(element,dict):
                            temp_object = BNode()
                            g.add((subject, predicate, temp_object))
                            process_object(element, g, mapping, object_type, temp_object)

                        ### Otherwise if the value is a primitive, then add it as a literal.
                        elif isinstance(element,(float,int)):
                            g.add((subject, predicate, Literal(element)))



        ####...otherwise if key is mapped to an quantity...
        elif key in mapping["quantities"].keys():

            temp_object = BNode()
            predicate = URIRef(mapping["quantities"][key]["iri"]) #hasQuantitativeProperty
            object_type = URIRef(mapping["quantities"][key]["type"]) #Type, example "Temperature"
            object_value = URIRef(mapping["quantities"][key]["value"])#hasValue
                
            g.add((subject, predicate, temp_object))
            g.add((temp_object, RDF.type, object_type))

            for predicate_, object_ in mapping["quantities"][key]["pred_obj"]:
                g.add((temp_object, URIRef(predicate_), URIRef(object_))) #hasReferenceUnit: SomeUnit


            ####...and the value is a dict with a "values" key, and its value is itself a list, add each value as literal 
            if isinstance(value, dict):
                if ("values" in value.keys()) & isinstance(value["values"], list): 
                    print("and the value is a dict with a values key, and its value is itself a list, add each value as literal ")
                    print(f"Here goes a value of {key}: {value}")
                    for num_value in value["values"]:
                        g.add((temp_object, object_value, Literal(num_value)))

            ####...otherwise if the value is a primitive type, add it as literal, in addition to other quantity statements
            elif isinstance(value, (float,int)):
                g.add((temp_object, object_value, Literal(value)))


        ####...otherwise if key is not mapped to anything, but the value is an object, send it back recursively
        elif isinstance(value, dict):
            process_object(value, g, mapping, json_object_type=None, temp_subject=subject)

    return g



def get_label(uri:str, mapping:dict):
    for key, value in mapping["@context"].items():
        if value == uri:
            return key
    return uri




def replace_uris_with_labels(obj, mapping:dict):

    if isinstance(obj, list):

        iris_list = []

        for item in obj:

            if isinstance(item, dict):                
                iris_list.append(replace_uris_with_labels(item))

            elif isinstance(item, str):
                label = get_label(item) if item.startswith("http") and item in  mapping["@context"].values() else item
                iris_list.append(label)

        return iris_list
    
    elif isinstance(obj, dict):

        new_obj = {}

        for key, value in obj.items():

            # Replace URIs in keys (if they exist in the mapping)
            new_key = get_label(key) if key.startswith("http") and key in  mapping["@context"].values() else key

            # Replace URIs in values (if they exist in the mapping)
            new_value = get_label(value) if isinstance(value, str) and value.startswith("http") and value in  mapping["@context"].values() else value

            new_obj[new_key] = replace_uris_with_labels(new_value)

        return new_obj
    
    else:
        return obj