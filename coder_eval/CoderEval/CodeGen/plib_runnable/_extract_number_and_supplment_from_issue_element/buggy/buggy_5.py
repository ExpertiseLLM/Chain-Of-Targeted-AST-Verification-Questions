def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number = ".".join(issue.find(".//number").text.split(".")[:-1])
	supp = ".".join(issue.find(".//supp").text.split(".")[:-1])
	return number, supp

