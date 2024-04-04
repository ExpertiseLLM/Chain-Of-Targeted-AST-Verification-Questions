def find_roots(
    graph: Graph, sub_class: str = SKOS.broader
) -> Iterable[Tuple[str, URIRef, URIRef]]:
    return _find_roots(graph, sub_class, set())
