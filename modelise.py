import pyld
import json
from rdflib import Graph

#Load JSON document
with open('scrapped.json') as f:
    doc = json.load(f)

# Contexte JSON-LD
with open('ctx.json') as f:
    ctx = json.load(f)

res = pyld.jsonld.to_rdf(doc, {
    'expandContext': ctx,  # contexte à appliquer
    'format': 'application/n-quads', # format de sortie
})

with open('rdf_file.ttl', 'w', encoding="utf-8") as f:
    f.write(res)

