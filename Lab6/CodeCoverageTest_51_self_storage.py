import pytest
from self_storage import rent_due, access_allowed, payment_status


def test_rent_due():
    assert rent_due("small", 1, False, False) == 0
    assert rent_due("small", 3, True, False) == 240
    assert rent_due("medium", 4, False, True) == 80
    assert rent_due("large", 5, False, True) == 160
    assert rent_due("small", 8, True, False) == 735
    assert rent_due("small", 8, False, False) == 490


def test_rent_due_errors():
    with pytest.raises(ValueError):
        rent_due("extra-large", 2, False, False)
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_access_allowed():
    assert access_allowed(23, 4, True) is True
    assert access_allowed(12, 5, True) is False
    assert access_allowed(5, 1, False) is False
    assert access_allowed(23, 1, False) is False
    assert access_allowed(12, 2, False) is True
    assert access_allowed(12, 3, False) is False


def test_payment_status():
    assert payment_status(0, True, False) == "current"
    assert payment_status(0, False, False) == "grace"
    assert payment_status(-11, False, True) == "lien"
    assert payment_status(15, False, True) == "current"