import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        result_price = self.price * self.quantity
        return result_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        """Отладка для разработчика
         return: <имя класа(товар, цена, количество)>
         """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """В случае если пользователь обращается к классу
        return: <Наименование товара>
        """
        return f"{self.__name}"

    @property
    def name(self):
        """getter приватного __name"""
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        """
        Проверка длины наименования, если длина больше 10 символов, выводится сообщение
        "Exception: Длина наименования товара превышает 10 символов". Обрезает наименование до 10 символов
         """

        self.__name = value
        if len(value) > 10:
            value = value[0:10]
            self.__name = value
            print(f"Exception: Длина наименования товара превышает 10 символов '{value}'")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """Добавление экземпляров класса с CSV файлов"""
        cls.all = []
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(str(row["name"]), float(row["price"]), int(row["quantity"]))

    @staticmethod
    def string_to_number(number):
        """Cтатический метод, возвращающий число из числа-строки"""
        numbers = float(number)
        numb = int(numbers)
        return numb
