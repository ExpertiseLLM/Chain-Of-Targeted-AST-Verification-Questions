# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0


def test_case_0():
    bytes_0 = b"Lt\x12\xb0\x0f(pj{v4W"
    var_0 = module_0.was_processed(bytes_0, bytes_0, bytes_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1597
    bool_0 = True
    set_0 = {int_0, bool_0, int_0}
    none_type_0 = None
    var_0 = module_0.was_processed(set_0, none_type_0, none_type_0)
    assert var_0 is False
    module_0.was_processed(var_0, int_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1702.626871
    int_0 = 1753
    dict_0 = {float_0: float_0, float_0: int_0, float_0: float_0, int_0: int_0}
    list_0 = [dict_0]
    module_0.was_processed(list_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "^Mlhy"
    none_type_0 = None
    var_0 = module_0.was_processed(str_0, str_0, none_type_0)
    assert var_0 is True
    module_0.was_processed(var_0, var_0, var_0)
