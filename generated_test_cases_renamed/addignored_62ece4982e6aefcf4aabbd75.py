import subprocess


<insert generated code here>


def test_addignored():
    """Check the correctness of addignored
    """
    # print(addignored("."))
    test_cases = dict()
    try :
        test_cases['test1']= addignored(".") == " ocfl/__pycache__/"
    except Exception as error :
        test_cases['test1'] = type(error).__name__
    print(test_cases)
if __name__ == "__main__":
    test_addignored()


