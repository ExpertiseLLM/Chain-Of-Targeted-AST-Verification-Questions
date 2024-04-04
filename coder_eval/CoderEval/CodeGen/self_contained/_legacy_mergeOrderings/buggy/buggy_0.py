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
	for ordering in orderings:
		if len(ordering) > 0:
			for i in range(len(ordering)):
				if ordering[i]!= '.':
					del ordering[i]
					break
	return orderings

class _Base(object):
	"""
	Base class for all objects that are not necessarily instances of
	_Base, but are used in a common way.
	"""
	def __getstate__(self):
		return self.__dict__

	def __setstate__(self, state):
		self.__dict__.update(state)