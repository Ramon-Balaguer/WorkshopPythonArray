from py_linq import Enumerable


class Person:
    def __init__(self, name: str, age: int, birth_month: int):
        self._name = name
        self._age = age
        self._birth_month = birth_month

    def get_age(self) -> int:
        return self._age

    def birth_month(self) -> int:
        return self._birth_month

    def __str__(self) -> str:
        return f"{self._name} {self._age}"

    def __repr__(self) -> str:
        return f"{self._name} {self._age}"


class Month:
    def __init__(self, month_numer_of_the_year: int, name: str):
        self.month_numer_of_the_year = month_numer_of_the_year
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Friends:
    MONTHS = Enumerable([Month(2, "Febrero"), Month(8, "Agosto")])

    def __init__(self):
        ramon = Person("Ramon", 36, 2)
        victor = Person("Victor", 29, 8)
        laura = Person("Laura", 29, 2)
        self._persons = Enumerable([ramon, victor, laura])

    def oldest(self) -> Person:
        return self._persons.order_by_descending(lambda friend: friend.get_age()).first()

    def group_by(self):
        return self._persons.group_by(["birth_month"], lambda friend: friend.birth_month())

    def add_months_name(self):
        return self.MONTHS.group_join(self._persons,
                                      lambda month: month.month_numer_of_the_year,
                                      lambda friend: friend.birth_month(),
                                      lambda friend_month: friend_month)

    def __str__(self) -> str:
        return "\n".join(self._persons.select(lambda friend: friend.__str__()).to_list())


if __name__ == '__main__':
    friends = Friends()
    print(friends)
    print(friends.oldest())
    print(friends.group_by())
    print(friends.add_months_name())
