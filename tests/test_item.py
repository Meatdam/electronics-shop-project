"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item = Item('Смартфон', 10000, 2)
    assert item.calculate_total_price() == 20000.0
    assert item.price == 10000

    item.pay_rate = 0.8
    item.apply_discount()
    assert item.calculate_total_price() == 16000.0
    assert item.price == 8000
