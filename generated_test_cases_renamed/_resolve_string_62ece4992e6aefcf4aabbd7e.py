import os, re


<insert generated code here>


def test__resolve_string():

    test_cases = dict()
    """Check the correctness of _resolve_string
    """
    # print(_resolve_string(re.compile(r"\&\{(?P<name>[a-zA-Z0-9_]+)(?P<default>\:.+)?\}").match("&{name}")))
    os.environ["AAA"] = "huawei"
    # assert _resolve_string(re.compile(r"\&\{(?P<name>[a-zA-Z0-9_]+)(?P<default>\:.+)?\}").match("&{name}")) == "huawei"
    try:
        test_cases['test1']= _resolve_string(re.compile(r"\&\{(?P<name>[a-zA-Z0-9_]+)(?P<default>\:.+)?\}").match("&{AAA:huawei}")) == "huawei"
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    print(test_cases)

if __name__ == "__main__":
    test__resolve_string()

