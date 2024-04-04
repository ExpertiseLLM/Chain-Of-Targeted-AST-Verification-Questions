def _extract_number_and_supplment_from_issue_element(issue):
	number = None
	suppl = None
	for child in issue.children:
		if isinstance(child, lxml.etree._Element):
			if child.tag == 'volume':
				number = child.text
			elif child.tag == 'supplement':
				suppl = child.text
			else:
				raise ValueError('Unexpected child %s of issue' % child.tag)
	return number, suppl


