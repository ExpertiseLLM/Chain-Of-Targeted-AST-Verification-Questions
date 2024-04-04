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
	return [x for x in orderings if x[0][-1]!= x[0][-2]]
