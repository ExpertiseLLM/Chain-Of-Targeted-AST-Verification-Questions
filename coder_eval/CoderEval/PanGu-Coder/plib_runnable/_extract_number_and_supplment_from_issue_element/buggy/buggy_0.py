def _extract_number_and_supplment_from_issue_element(issue):
    
    
    number_element = issue.find('number')
    if number_element is None:
        raise ValueError("issue not found: %s" % issue)
    number = number_element.text
    suppl = number_element.getnext()
    if suppl is None:
        raise ValueError("issue not found: %s" % issue)
    return number, suppl
