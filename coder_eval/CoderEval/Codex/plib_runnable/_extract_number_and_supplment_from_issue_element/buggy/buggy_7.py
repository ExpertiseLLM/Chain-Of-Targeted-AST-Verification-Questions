def _extract_number_and_supplment_from_issue_element(issue):
	issue_elements = issue.get_children()
	issue_number = None
	suppl = None
	for element in issue_elements:
		if element.get_name() == "issue":
			issue_number = element.get_value()
		elif element.get_name() == "supplement":
			suppl = element.get_value()
	return issue_number, suppl

