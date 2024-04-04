import platform


<insert generated code here>


def test_os_is_mac():
    """Check the correctness of os_is_mac
    """
    test_cases = dict()
    try:

        test_cases['test1']= os_is_mac() == (platform.system() == "Darwin")
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    print(test_cases)

if __name__ == "__main__":
    test_os_is_mac()


