import argparse


<insert generated code here>


def test_parser_flags():
    """
    Check the corretness of parser_flags
    """
    test_cases = dict()
    try :
        test_cases['test1'] = parser_flags(argparse.ArgumentParser()) == '-h --help'
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = parser_flags(argparse.ArgumentParser(add_help=False)) == ''
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = parser_flags(argparse.ArgumentParser(prog='test')) == '-h --help'
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = parser_flags(argparse.ArgumentParser(prog='test', add_help=False)) == ''
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:
        test_cases['test5'] = parser_flags(argparse.ArgumentParser(prog='test', description='test')) == '-h --help'
    except Exception as error:
        test_cases['test5'] = type(error).__name__
    try:
        test_cases['test6'] = parser_flags(argparse.ArgumentParser(prog='test', description='test', add_help=False)) == ''
    except Exception as error:
        test_cases['test6'] = type(error).__name__
    try:
        test_cases['test7'] = parser_flags(argparse.ArgumentParser(prog='test', description='test', epilog='test')) == '-h --help'
    except Exception as error:
        test_cases['test1'] = type(error).__name__

    print(test_cases)


if __name__ == "__main__":
    test_parser_flags()


