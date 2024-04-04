def _legacy_mergeOrderings(orderings):
	if orderings is None:
		return None
	if isinstance(orderings, dict):
		orderings = orderings.items()
	if isinstance(orderings, (list, tuple)):
		items = []
		for item in orderings:
			if isinstance(item, dict):
				items.extend(item.items())
			elif isinstance(item, (list, tuple)):
				items.extend(item)
			else:
				items.append(item)
		orderings = items
	ordering = []
	for item in orderings:
		if item not in ordering:
			ordering.append(item)
	return ordering


