<insert generated code here>


def test_subclasses():
    """
    Check the corretness of subclasses
    """
    test_cases = dict()
    try:
        test_cases['test1']=subclasses(set) == set()
    except Exception as exeption :
        test_cases['test1'] = type(exeption).__name__
    print(test_cases)
if __name__ == "__main__":
    test_subclasses()


