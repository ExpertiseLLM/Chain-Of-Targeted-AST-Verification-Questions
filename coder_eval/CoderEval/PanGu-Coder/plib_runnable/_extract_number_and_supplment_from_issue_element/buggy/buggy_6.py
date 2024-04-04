def _extract_number_and_supplment_from_issue_element(issue):
    number = issue.find('.//{http://purl.org/dc/elements/1.1/}number')
    number = number.text
    suppl = issue.find('.//{http://purl.org/dc/elements/1.1/}suppl')
    suppl = suppl.text
    return number, suppl
