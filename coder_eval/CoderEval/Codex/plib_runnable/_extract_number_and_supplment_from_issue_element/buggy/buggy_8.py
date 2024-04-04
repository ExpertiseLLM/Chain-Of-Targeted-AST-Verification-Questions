def _extract_number_and_supplment_from_issue_element(issue):
	# print(issue)
	number, suppl = None, None
	if issue.tag == 'issue':
		number = issue.get('number')
		suppl = issue.get('supplement')
		if number is None:
			number = issue.get('volume')
	elif issue.tag == 'volume':
		number = issue.text
		suppl = issue.get('supplement')
	else:
		raise NotImplementedError('Unknown issue tag: %s' % issue.tag)
	return number, suppl


