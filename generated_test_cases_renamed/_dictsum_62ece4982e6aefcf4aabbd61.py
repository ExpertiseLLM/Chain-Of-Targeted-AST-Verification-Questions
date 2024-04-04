<insert generated code here>


def test__dictsum():
    """
    Check the corretness of _dictsum
    """
    test_cases = dict()
    try :
        test_cases['test1']= (_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}]) == {'a': 6, 'b': 2})
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2']= (_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}]) == {'a': 7, 'b': 4})
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test3']= (_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]) == {'a': 8, 'b': 6})
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test4']= (_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]) == {
        'a': 9, 'b': 8})
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test']= (_dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2},
                     {'a': 1, 'b': 2}]) == {'a': 10, 'b': 10})
        print(test_cases)
    except Exception as error :
        print(type(error).__name__)


if __name__ == "__main__":
    test__dictsum()


