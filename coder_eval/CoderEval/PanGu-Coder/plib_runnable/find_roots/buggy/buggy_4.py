def find_roots(
    graph: Graph, rdflib_subclass: RDFSubClassOf, rdflib_broader: RDFSubClassOf
) -> Set[URIRef]:
    return set(rdflib_subclass.object) | set(rdflib_broader.object)
