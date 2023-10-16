from pyshacl import validate


#Read the data_graph:
with open('rdf_file.ttl', 'r', encoding="utf-8") as f:
    data_graph = f.read()

#Read the shacl_graph
with open('trace_model.shacl.ttl', 'r', encoding="utf-8") as f:
    sg = f.read()

r = validate(data_graph,
      shacl_graph=sg)
conforms, results_graph, results_text = r
print(f"Conforms : {conforms}")
print(f"{results_text}")