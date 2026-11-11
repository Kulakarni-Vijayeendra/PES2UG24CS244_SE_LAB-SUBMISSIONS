
from hypothesis import given, strategies as st
from self_storage import parse_rental, duration_average, payable_rent


# Test 1: Fuzz testing parse_rental()
@given(st.text() | st.none())
def test_parse_rental_no_crash(s):
    result = parse_rental(s)
    assert isinstance(result, tuple)
    assert len(result) == 2


# Test 2: Fuzz testing duration_average()
@given(st.text() | st.none())
def test_duration_average_no_crash(s):
    result = duration_average(s)
    assert isinstance(result, int)


# Test 3: Fuzz testing payable_rent()
@given(st.text() | st.none())
def test_payable_rent_no_crash(s):
    result = payable_rent(s)
    assert isinstance(result, float)


# Regression tests: Verify valid inputs still work

def test_parse_rental_valid():
    assert parse_rental("medium:6") == ("Medium", 6.0)


def test_duration_average_valid():
    assert duration_average("3,6,12") == 7


def test_payable_rent_valid():
    assert payable_rent("2400|200") == 2632.0


# Test invalid input handling

def test_invalid_inputs():
    assert parse_rental(":") == ("Unknown", 0.0)
    assert duration_average("") == 0
    assert payable_rent("|") == 0.0


# Test non-finite values

def test_non_finite_values():
    assert parse_rental("medium:nan") == ("Unknown", 0.0)
    assert payable_rent("inf|200") == 0.0
