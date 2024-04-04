def _legacy_mergeOrderings(orderings):
	from copy import copy
	# this is O(n^2), but it should be fine for a small number of orderings
	# and a small amount of objects in each ordering
	new_ordering = []
	objects = []
	for ordering in orderings:
		for obj in ordering:
			if obj not in objects:
				objects.append(obj)
				new_ordering.append(obj)
	return new_ordering


