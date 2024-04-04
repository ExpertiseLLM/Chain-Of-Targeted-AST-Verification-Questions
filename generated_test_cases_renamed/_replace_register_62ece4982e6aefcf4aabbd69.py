<insert generated code here>


def test__replace_register():
    """
    Check the corretness of _replace_register
    """
    test_cases  = dict()
    try :
        test_cases['test1'] = _replace_register({'reg1': 1, 'reg2': 2, 'reg3': 3}, 1, 'reg1') == {'reg1': 1, 'reg2': 2, 'reg3': 3}
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = _replace_register({'reg1': 1, 'reg2': 2, 'reg3': 3}, 2, 'reg2') == {'reg1': 1, 'reg2': 2, 'reg3': 3}
    except Exception as error:
        test_cases ['test2'] = type(error).__name__
    try:
        test_cases['test3'] = _replace_register({'reg1': 1, 'reg2': 2, 'reg3': 3}, 3, 'reg3') == {'reg1': 1, 'reg2': 2, 'reg3': 3}
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = _replace_register({'reg1': 1, 'reg2': 2, 'reg3': 3}, 1, 'reg2') == {'reg1': 2, 'reg3': 3}
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:
        test_cases['test5'] = _replace_register({'reg1': 1, 'reg2': 2, 'reg3': 3}, 2, 'reg3') == {'reg1': 1, 'reg2': 3}
    except Exception as error:
        test_cases['test5'] = type(error).__name__
    try:
        test_cases['test6'] = _replace_register({'reg1': 1, 'reg2': 2, 'reg3': 3}, 3, 'reg1') == {'reg2': 2, 'reg3': 1}
    except Exception as error:
        test_cases['test6'] = type(error).__name__
    print(test_cases)
if __name__ == "__main__":
    test__replace_register()


