def minimalBases(classes):
	# Reduce the list to its unique items
	unique = []
	for c in classes:
		if c not in unique:
			unique.append(c)
	# Create a list of items that depend on other items
	rest = []
	for c in unique:
		if c._dependencies:
			rest.append(c)
	# Create a list of items that don't depend on other items
	head = []
	for c in unique:
		if c not in rest:
			head.append(c)
	# Add an item from rest to head if all its dependencies are in head
	while rest:
		rest2 = []
		for c in rest:
			if all(d in head for d in c._dependencies):
				head.append(c)
			else:
				rest2.append(c)
		rest = rest2
	# Add the remaining items from rest to head
	for c in rest:
		head.append(c)
	return head

