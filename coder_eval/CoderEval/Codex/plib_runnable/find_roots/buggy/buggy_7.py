def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
	roots = roots or set()
	for s, p, o in graph:
		if p == prop:
			roots.add(s)
			roots.add(o)
	return roots


