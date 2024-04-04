def find_roots(
    graph: Graph,
    rdflib_subclass: Union[URIRef, Literal],
    return_type: Optional[Type] = None,
) -> Set[URIRef]:
    if return_type is None:
        return_type = set()
    return set(graph.objects(subject=rdflib_subclass, predicate=RDFS.hasRoot))
