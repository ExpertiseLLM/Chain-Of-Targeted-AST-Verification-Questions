def find_roots(
    graph: Graph, rdflib_subclass_of: Union[RDFGraph, str]
) -> Set[Tuple[str, str, str]]:
    return find_subclass_roots(graph, rdflib_subclass_of)
