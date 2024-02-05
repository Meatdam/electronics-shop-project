import pytest
from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test__init__(test_phone):
    """
    Проверка Инициализации атрибутов класса Phone
    """
    assert test_phone.name == "iPhone 14"
    assert test_phone.price == 120_000
    assert test_phone.quantity == 5
    assert test_phone.number_of_sim == 2


def test_repr(test_phone):
    """
     Проверка метода __repr__
    """
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(test_phone):
    """
    Проверка метода __str__
    """
    assert str(test_phone) == "iPhone 14"


def test_add_error(test_phone):
    """
    Отлавливает ошибку ValueError
    """
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0
        test_phone.number_of_sim = -1
