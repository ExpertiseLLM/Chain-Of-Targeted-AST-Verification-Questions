# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0


def test_case_0():
    bytes_0 = b"L0&\x84\xc3=\xe6\x0e\xce\xdb\xcd\xcf\x99g\xa9Q\xae#\xb8\x06"
    var_0 = module_0.vertex3tuple(bytes_0)
    var_1 = module_0.vertex3tuple(var_0)
    var_2 = module_0.vertex3tuple(bytes_0)
    var_3 = module_0.vertex3tuple(bytes_0)
    var_4 = module_0.vertex3tuple(bytes_0)
    var_5 = module_0.vertex3tuple(var_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.vertex3tuple(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.vertex3tuple(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ";!_FWvSP\x0c5: M}"
    tuple_0 = (str_0,)
    var_0 = module_0.vertex3tuple(tuple_0)
    str_1 = "a_\x0cZh#:Y|@L"
    set_0 = {str_1}
    module_0.vertex3tuple(set_0)
