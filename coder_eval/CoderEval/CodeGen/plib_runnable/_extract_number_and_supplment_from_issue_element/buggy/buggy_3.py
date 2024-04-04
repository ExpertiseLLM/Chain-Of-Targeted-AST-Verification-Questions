def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number = ''
	suppl = ''
	contents = issue.find_all('p')
	for content in contents:
		if content.text == 'Number':
			number = content.text
		elif content.text == 'Suppl':
			suppl = content.text
	return number, suppl

