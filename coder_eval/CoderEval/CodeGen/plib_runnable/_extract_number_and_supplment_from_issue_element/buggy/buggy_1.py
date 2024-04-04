def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number = issue.find("number").text
	supp = issue.find("suppl").text
	return number, supp

