# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.round_half_to_even(bool_0)
    assert var_0 == 0


def test_case_1():
    float_0 = 2154.1
    var_0 = module_0.round_half_to_even(float_0)
    assert var_0 == 2154
    float_1 = -186.1675
    var_1 = module_0.round_half_to_even(float_1)
    assert var_1 == -186
    var_2 = module_0.round_half_to_even(var_0)
    assert var_2 == 2154
    var_3 = module_0.round_half_to_even(var_1)
    assert var_3 == -186


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.round_half_to_even(none_type_0)


def test_case_3():
    float_0 = -709.5
    var_0 = module_0.round_half_to_even(float_0)
    assert var_0 == -710


def test_case_4():
    bool_0 = False
    var_0 = module_0.round_half_to_even(bool_0)
    assert var_0 == 0
    float_0 = 5586.421
    var_1 = module_0.round_half_to_even(float_0)
    assert var_1 == 5586
    var_2 = module_0.round_half_to_even(var_0)
    assert var_2 == 0
    float_1 = -3370.5
    var_3 = module_0.round_half_to_even(float_1)
    assert var_3 == -3370
    object_0 = module_1.object()
