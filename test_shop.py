import pytest
from shop import price_after_discount

def test_ten_percent():
    assert price_after_discount(100, 10) == 90

def test_invalid_percent():
    with pytest.raises(ValueError):
        price_after_discount(100, 150)
