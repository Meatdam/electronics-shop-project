from src.item import Item


class KeyboardMixin:
    """
    Миксин Класса Keyboard
    Метод change_lang - меняет расскалдку на клавиатуре
    return: __language (Метод проперти)
    """

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, KeyboardMixin):
    """
    Дочерний класс Item
    return: name, price, quantity, __language
    """

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        KeyboardMixin.__init__(self)
