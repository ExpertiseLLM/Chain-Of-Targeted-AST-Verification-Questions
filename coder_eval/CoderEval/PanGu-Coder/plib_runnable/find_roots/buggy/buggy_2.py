def find_roots(
    graph: Graph,
    sub_class: str
) -> Set[URIRef]:
    rdf = rdflib.ConjunctiveGraph()
    rdf.parse(data=graph.serialize(format='turtle'))
    return set([rdf.prefixes[pref].namespaceURI for pref in graph.prefixes])
