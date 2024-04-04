<insert generated code here>


def test_size_to_bytes():
    """
    Check the corretness of size_to_bytes
    """
    test_cases = dict()
    try:
        test_cases['test1'] = size_to_bytes("500") == 500
    except Exception as error:
        test_cases['test1']  = type(error).__name__
    try:
        test_cases['test2'] = size_to_bytes("1K") == 1000
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = size_to_bytes("1M") == 1000 ** 2
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = size_to_bytes("1G") == 1000 ** 3
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:
        test_cases['test5'] = size_to_bytes("1T") == 1000 ** 4
    except Exception as error:
        test_cases['test5'] = type(error).__name__
    try:
        test_cases['test6'] = size_to_bytes("1P") == 1000 ** 5
    except Exception as error:
        test_cases['test6'] = type(error).__name__
    print(test_cases)

if __name__ == "__main__":
    test_size_to_bytes()


