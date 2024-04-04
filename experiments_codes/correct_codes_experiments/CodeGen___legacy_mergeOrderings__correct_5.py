def _legacy_mergeOrderings(orderings):
	"""
	Merge multiple orderings so that within-ordering order is preserved

Orderings are constrained in such a way that if an object appears
in two or more orderings, then the suffix that begins with the
object must be in both orderings.

For example:

>>> _mergeOrderings([
... ['x', 'y', 'z'],
... ['q', 'z'],
... [1, 3, 5],
... ['z']
... ])
['x', 'y', 'q', 1, 3, 5, 'z']
	"""
	out = []
	for ordering in orderings:
		out.extend(ordering)
		if len(ordering) > 1:
			if any(ordering[0][0] == ordering[1][0]):
				out.remove(ordering[0])
	return out

