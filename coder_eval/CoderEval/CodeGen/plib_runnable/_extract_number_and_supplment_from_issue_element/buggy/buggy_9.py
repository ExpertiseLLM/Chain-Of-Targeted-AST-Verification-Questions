def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number = None
	supp = None
	try:
		number = int(issue.find('.//issue[@number]').text)
	except ValueError:
		number = None
	try:
		supp = issue.find('.//supplier[@name]').text
	except AttributeError:
		supp = None
	return number, supp

