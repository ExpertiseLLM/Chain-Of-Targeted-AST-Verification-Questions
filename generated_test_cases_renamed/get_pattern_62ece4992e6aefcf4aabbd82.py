import re


<insert generated code here>


def test_get_pattern():
    """Check the correctness of get_pattern
    """

    test_cases = dict()
    try:
        test_cases['test1']= get_pattern('1.cpp', ) == re.compile('1.cpp')
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2']= get_pattern('4.cpp') == re.compile('4.cpp')
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3']= get_pattern('9.h') == re.compile('9.h')
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    print(test_cases)

if __name__ == "__main__":
    test_get_pattern()


