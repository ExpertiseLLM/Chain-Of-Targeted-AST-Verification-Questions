# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -3061.213
    tuple_0 = (float_0,)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    str_0 = "Xn6x"
    bool_0 = False
    none_type_0 = None
    str_1 = module_0.int_to_string(none_type_0, str_0)
    assert str_1 == ""
    module_0.int_to_string(bool_0, list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    str_0 = ":Qe"
    list_0 = [str_0, str_0, str_0, str_0]
    none_type_0 = None
    str_1 = module_0.int_to_string(bool_0, list_0, none_type_0)
    assert str_1 == "eQ:"
    bool_1 = True
    module_0.int_to_string(bool_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa2\xe8s\xce).L\x02\xe7-"
    module_0.int_to_string(bytes_0, bytes_0)


def test_case_3():
    int_0 = 2019
    str_0 = "_k7"
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = module_0.int_to_string(int_0, list_0)
    assert str_1 == "7k_7k_7k_7k_7k_7k_"
    bool_0 = False
    str_2 = "z!n\r$zOs\n,g6&SZ(4#"
    str_3 = module_0.int_to_string(bool_0, str_2, bool_0)
    assert str_3 == ""
    str_4 = ""
    list_1 = [str_2, str_2, str_2, str_4]
    str_5 = module_0.int_to_string(str_4, list_1)
    assert str_5 == ""
    str_6 = module_0.int_to_string(bool_0, list_1)
    assert str_6 == ""


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    module_0.int_to_string(bool_0, bool_0)
