def _extract_number_and_supplment_from_issue_element(issue):
	# number
	number = None
	number_value = None
	if 'number' in issue:
		number = issue['number']
		if number is not None:
			number_value = number.get_value()
			if number_value is None:
				number_value = number.get_text()

	# suppl
	suppl = None
	suppl_value = None
	if 'suppl' in issue:
		suppl = issue['suppl']
		if suppl is not None:
			suppl_value = suppl.get_value()
			if suppl_value is None:
				suppl_value = suppl.get_text()

	if number_value is not None and suppl_value is not None:
		if number_value.strip() == '':
			number_value = None
		if suppl_value.strip() == '':
			suppl_value = None

	if number_value is None and suppl_value is not None:
		number_value =
