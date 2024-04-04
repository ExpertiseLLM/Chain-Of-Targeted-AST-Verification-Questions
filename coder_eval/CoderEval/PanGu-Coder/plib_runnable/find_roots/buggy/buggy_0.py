def find_roots(
    graph: Graph,
    rdflib_subclass_of: RDFlib.NamespaceURIRef,
) -> Set[RDFlib.URIRef]:
    return find_triples(graph, rdflib_subclass_of, RDFlib.RDFS.subClassOf)
