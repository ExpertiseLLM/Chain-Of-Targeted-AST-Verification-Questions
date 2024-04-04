<insert generated code here>


def test_paging():
    """
    Check the corretness of paging
    """
    test_cases = dict()
    try:

        test_cases['test1'] = list(paging([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = list(paging([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = list(paging([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = list(paging([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10]]
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:
        test_cases['test5'] = list(paging([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)) == [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10]]
    except Exception as error:
        test_cases['test5'] = type(error).__name__

    print(test_cases)

if __name__ == "__main__":
    test_paging()


