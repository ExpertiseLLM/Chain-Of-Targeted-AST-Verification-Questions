def _extract_number_and_supplment_from_issue_element(issue):
	number_value = None
	suppl_value = None

	# Try to extract number value from the text contents of issue
	number_match = re.search(r'([0-9]+)', issue.text)
	if number_match:
		number_value = number_match.group(0)

	# Try to extract suppl value from the text contents of issue
	suppl_match = re.search(r'\((.+)\)', issue.text)
	if suppl_match:
		suppl_value = suppl_match.group(1)

	return (number_value, suppl_value)


