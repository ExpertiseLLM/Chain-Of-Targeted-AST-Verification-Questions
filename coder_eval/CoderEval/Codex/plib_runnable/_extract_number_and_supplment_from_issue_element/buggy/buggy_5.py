def _extract_number_and_supplment_from_issue_element(issue):
	assert issue is not None

	issue_type = issue.attrib.get('publication_type', None)
	if issue_type is not None:
		issue_type = issue_type.lower()

	number = None
	suppl = None

	if issue_type == 'supplement':
		suppl = ''
	elif issue_type == 'retraction':
		suppl = 'ret'
	elif issue_type == 'correction':
		suppl = 'corr'

	if issue_type is None or issue_type == 'regular':
		number = issue.text

	if number is None:
		number = ''

	return (number, suppl)

