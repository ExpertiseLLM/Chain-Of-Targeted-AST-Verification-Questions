def _extract_number_and_supplment_from_issue_element(issue):
    
    
    number = issue.find('number').text
    suppl = issue.find('suppl').text

    return number, suppl
