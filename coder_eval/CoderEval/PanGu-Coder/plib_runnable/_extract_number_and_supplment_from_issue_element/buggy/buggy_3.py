def _extract_number_and_supplment_from_issue_element(issue):
    return {
        "number": issue.find("number").text,
        "suppl": issue.find("suppl").text,
    }
