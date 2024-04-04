import re


<insert generated code here>


def test_make_find_paths():
    """Check the correctness of make_find_paths
    """
    test_cases = dict()
    try :

        test_cases['test1'] = make_find_paths(('foo.txt', 'pp:root/somedir')) == ('sh:**/*foo.txt*/**', 'pp:root/somedir')
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = make_find_paths(('foo.txt', 'pp:root/somedir', '-R')) == (
        'sh:**/*foo.txt*/**', 'pp:root/somedir', 'sh:**/*-R*/**')
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        test_cases['test3'] = make_find_paths(('foo.txt', 'pp:root/somedir', '-R', '-r')) == (
        'sh:**/*foo.txt*/**', 'pp:root/somedir', 'sh:**/*-R*/**', 'sh:**/*-r*/**')
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = make_find_paths(('foo.txt', 'pp:root/somedir', '-R', '-r', '-P')) == (
        'sh:**/*foo.txt*/**', 'pp:root/somedir', 'sh:**/*-R*/**', 'sh:**/*-r*/**', 'sh:**/*-P*/**')
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:
        test_cases['test5'] = make_find_paths(('foo.txt', 'pp:root/somedir', '-R', '-r', '-P', '-p')) == (
        'sh:**/*foo.txt*/**', 'pp:root/somedir', 'sh:**/*-R*/**', 'sh:**/*-r*/**', 'sh:**/*-P*/**', 'sh:**/*-p*/**')
    except Exception as error:
        test_cases['test5'] = type(error).__name__

    print(test_cases)


if __name__ == "__main__":
    test_make_find_paths()


