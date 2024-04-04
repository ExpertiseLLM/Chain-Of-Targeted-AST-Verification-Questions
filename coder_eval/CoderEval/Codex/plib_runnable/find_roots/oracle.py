import rdflib
def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    """
    Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    RDFS.subClassOf or SKOS.broader

    """

    non_roots: Set[Node] = set()
    if roots is None:
        roots = set()
    for x, y in graph.subject_objects(prop):
        non_roots.add(x)
        if x in roots:
            roots.remove(x)
        if y not in non_roots:
            roots.add(y)
    return roots
