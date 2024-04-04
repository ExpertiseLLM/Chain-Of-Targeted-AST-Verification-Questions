def find_roots(
    graph: Graph,
    rdflib_subclass: RDFS.Class,
    rdflib_broader: RDFS.Class,
) -> Set[URIRef]:
    return set(
        rdflib_subclass
        if rdflib_broader in graph
        else graph
        if rdflib_subclass in graph
        else rdflib_broader
        if rdflib_broader in graph
        else rdflib_subclass
    )
