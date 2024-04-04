def find_roots(
    graph: Graph,
    rdflib_sub_class: URIRef,
    rdflib_broader: URIRef,
) -> Set[URIRef]:
    return set(graph.objects(rdflib_sub_class, rdflib_broader))
