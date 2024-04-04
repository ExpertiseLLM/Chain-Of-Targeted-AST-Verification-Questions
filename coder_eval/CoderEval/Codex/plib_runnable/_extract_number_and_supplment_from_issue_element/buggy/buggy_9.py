def _extract_number_and_supplment_from_issue_element(issue):
	issue_text = issue.text
	for match in re.finditer(r'\(?(no\.?\s*|n\.?\s*|num\.?\s*|núm\.?\s*)?(\d+)\)?', issue_text, re.I):
		return (match.group(2), None)
	for match in re.finditer(r'\(?(no\.?\s*|n\.?\s*|num\.?\s*|núm\.?\s*)?(\d+)(?:[^\d]*(?:sup\.?\s*|suppl\.?\s*|supplement\.?\s*|supplément\.?\s*|s\.?\s*|sppl\.?\s*))?(\d*)\)?', issue_text, re.I):
		return (match.group(2), match.group(3))
	return (None, None)

