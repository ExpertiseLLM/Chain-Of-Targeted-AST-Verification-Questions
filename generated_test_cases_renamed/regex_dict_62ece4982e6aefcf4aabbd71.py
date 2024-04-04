import re, fnmatch


<insert generated code here>


def test_regex_dict():
    """Check the correctness of regex_dict
    """
    test_cases = dict()
    try:
        test_cases['test1'] = regex_dict({'*.cpp': {'a': 'arf', 'b': 'bark', 'c': 'coo'}}) == {
            re.compile(fnmatch.translate('*.cpp')).match: {'a': 'arf', 'b': 'bark', 'c': 'coo'}}
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = regex_dict({'*.h': {'h': 'help'}}) == {re.compile(fnmatch.translate('*.h')).match: {'h': 'help'}}
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = regex_dict({'*.cpp': {'a': 'arf', 'b': 'bark', 'c': 'coo'}, '*.h': {'h': 'help'}}) == {
            re.compile(fnmatch.translate('*.cpp')).match: {'a': 'arf', 'b': 'bark', 'c': 'coo'},
            re.compile(fnmatch.translate('*.h')).match: {'h': 'help'}}
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    print(test_cases)

if __name__ == "__main__":
    test_regex_dict()


