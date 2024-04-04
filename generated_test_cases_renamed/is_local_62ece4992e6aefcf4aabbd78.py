import socket,platform


<insert generated code here>


def test_is_local():
    """Check the correctness of is_local
    """
    test_cases = dict()
    try:
        test_cases['test1'] = is_local(' ') == False
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = is_local('   ') == False
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = is_local('127.0.0.1') == True
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = is_local('localhost') == True
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:
        test_cases['test5'] = is_local(' localhost ') == False
    except Exception as error:
        test_cases['test5'] = type(error).__name__
    try:
        test_cases['test6'] = is_local(platform.node()) == True
    except Exception as error:
        test_cases['test6'] = type(error).__name__
    try:
        test_cases['test7'] = is_local(socket.gethostbyaddr(socket.gethostname())[0]) == True
    except Exception as error:
        test_cases['test7'] = type(error).__name__
    try:
        test_cases['test8'] = is_local(socket.gethostname()) == True
    except Exception as error:
        test_cases['test8'] = type(error).__name__


    print(test_cases)
if __name__ == "__main__":
    test_is_local()


