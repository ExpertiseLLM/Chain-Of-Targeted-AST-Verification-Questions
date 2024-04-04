def _extract_number_and_supplment_from_issue_element(issue):
	# number
	number = _extract_number_from_issue_element(issue)
	if number:
		number = number[0]

	# suppl
	suppl = _extract_suppl_from_issue_element(issue)
	if suppl:
		suppl = suppl[0]

	return number, suppl


