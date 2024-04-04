def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number_elements = issue.find_elements_by_tag_name("span")
	suppl_elements = issue.find_elements_by_tag_name("sup")

	number = ""
	suppl = ""

	for number_element in number_elements:
		number = number_element.text
	for suppl_element in suppl_elements:
		suppl = suppl_element.text

	return number, suppl