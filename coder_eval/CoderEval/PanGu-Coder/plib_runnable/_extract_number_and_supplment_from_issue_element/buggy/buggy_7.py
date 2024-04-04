def _extract_number_and_supplment_from_issue_element(issue):
    number_and_suppl = issue.find('.//{' + NS + '}number').text
    number_and_suppl = number_and_suppl.strip()
    if number_and_suppl == '':
        number_and_suppl = issue.find('.//{' + NS + '}suppl').text
        number_and_suppl = number_and_suppl.strip()
    return number_and_suppl
