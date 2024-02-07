from src.keyboard import Keyboard
import pytest


@pytest.fixture
def test_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(test_keyboard):
    """
    Проверка вывода метода str
    """
    assert str(test_keyboard) == "Dark Project KD87A"


def test_language(test_keyboard):
    """
    Проверка языка по умолчанию
    """
    assert test_keyboard.language == 'EN'


def test_language_ru(test_keyboard):
    """
    Проеврка языка расскладки
    """
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'


def test_add_error(test_keyboard):
    """
    Отлавливает ошибку ValueError
    """
    with pytest.raises(AttributeError):
        test_keyboard.language = 'CH'
