def find_roots(
    graph: Graph, rdflib.RDFS.subClassOf: RDFLibClass
) -> Set[RDFLibClass]:
    if graph.sinks:
        return set()

    return set(graph.sinks) | set(graph.sources)
