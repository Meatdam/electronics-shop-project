"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from config import OPERATION_PATH


@pytest.fixture
def test_item():
    return Item('Смартфон', 10000, 2)


def test_calculator_total_price(test_item):
    assert test_item.calculate_total_price() == 20000.0
    assert test_item.price == 10000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.calculate_total_price() == 16000.0
    assert test_item.price == 8000


def test_name(test_item):
    test_item.name = "Смартфон"
    assert test_item.name == "Смартфон"


def test_string_to_number(test_item):
    assert test_item.string_to_number('5.5') == 5
    assert test_item.string_to_number('5') == 5


def test_instantiate_from_csv(test_item):
    test_item.instantiate_from_csv(OPERATION_PATH)
    assert len(test_item.all) == 5
