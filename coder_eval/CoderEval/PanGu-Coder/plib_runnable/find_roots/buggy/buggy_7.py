def find_roots(
    graph: Graph, subclass_of: str = SKOS.broader, cache: bool = True
) -> Set[URIRef]:
    return find_roots_via_cache(graph, subclass_of, cache)
