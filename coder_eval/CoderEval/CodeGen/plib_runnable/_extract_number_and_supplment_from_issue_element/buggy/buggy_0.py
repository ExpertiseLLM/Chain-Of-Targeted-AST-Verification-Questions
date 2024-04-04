def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number = None
	suppl = None
	if issue.has_extension_elements:
		extensions = issue.extension_elements
		for extension in extensions:
			ext_attr = extension.attrs.get('number', None)
			if ext_attr is not None:
				number = ext_attr.text
				break
		if number is not None:
			ext_attr = extension.attrs.get('suppl', None)
			if ext_attr is not None:
				suppl = ext_attr.text
				break
	return number, suppl

