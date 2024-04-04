import os


<insert generated code here>


def test_write_configuration():
    """Check the correctness of write_configuration
    """
    test_cases = dict()
    try:
        test_cases['test1'] = write_configuration('test.yaml', 'test', overwrite=True) == 'test'
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = write_configuration('test.yaml', 'test', overwrite=False) == FileExistsError
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = write_configuration('test.yaml', 'hhhhh', overwrite=True) == 'hhhhh'
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = write_configuration('test.yaml', 'hhhhh', overwrite=False) == FileExistsError
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    print(test_cases)

if __name__ == "__main__":
    test_write_configuration()


