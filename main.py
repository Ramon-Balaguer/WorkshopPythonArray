from py_linq import Enumerable


class Person:
    def __init__(self, name: str, age: int, birth_month: int):
        self._name = name
        self._age = age
        self._birth_month = birth_month

    def get_age(self) -> int:
        return self._age

    def month(self) -> int:
        return self._birth_month

    def name(self) -> str:
        return self._name

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
    MONTHS = Enumerable([Month(1, "Enero"), Month(2, "Febrero"), Month(8, "Agosto")])

    def __init__(self):
        ramon = Person("Ramon", 36, 2)
        victor = Person("Victor", 30, 8)
        laura = Person("Laura", 29, 2)
        paco = Person("Paco", 93, 1)
        carmen = Person("Carmen", 18, 2)
        self._persons = Enumerable([ramon, victor, laura, paco, carmen])

    def __str__(self) -> str:
        return ", ".join(self._persons.select(lambda friend: friend.__str__()).to_list())

    def order_by_age(self):
        self._persons = self._persons.order_by(lambda friend: friend.get_age())

    def oldest(self) -> Person:
        return self._persons.order_by_descending(lambda friend: friend.get_age()).first()

    def group_by_birth_month(self) -> Enumerable:
        return self._persons.group_by(["birth_month"], lambda friend: friend.month())

    def group_by_month(self):
        return self.MONTHS.group_join(self._persons,
                                      lambda month: month.month_numer_of_the_year,
                                      lambda friend: friend.month(),
                                      lambda friend_month: friend_month)

    def avg_age(self):
        return self._persons.avg(lambda friend: friend.get_age())

    def number_of_friends(self):
        return self._persons.count()

    def new_relationship(self, friend: Person):
        self._persons.add(friend)

    def born_in_february(self):
        return self._persons.where(lambda friend: friend.month() == 2)

    def born_in_month(self, month: str) -> Enumerable:
        mont_object: Month = self.MONTHS.where(lambda month_item: month_item.name == month).single()
        return self._persons.where(lambda friend: friend.month() == mont_object.month_numer_of_the_year)

    def bring_friends_together(self, other_friends: Enumerable):
        self._persons = self._persons.concat(other_friends)

    def mutual_friends_with_the_same_age(self, other_friends: Enumerable) -> Enumerable:
        return self._persons.join(other_friends,
                                  lambda friend: friend.get_age(),
                                  lambda friend: friend.get_age(),
                                  lambda result: result)


if __name__ == '__main__':
    friends = Friends()
    print(friends)
    friends.order_by_age()
    print(friends)
    print(friends.oldest())
    print(friends.group_by_birth_month())
    print(friends.group_by_month())
    print(friends.avg_age())
    print(friends.number_of_friends())

    carlos = Person("Carlos", 45, 8)
    friends.new_relationship(carlos)
    print(friends.number_of_friends())
    print(friends)
    print(friends.avg_age())

    print(friends.born_in_february())
    print(friends.born_in_month("Febrero"))
    print(friends.born_in_month("Enero"))

    pepe = Person("pepe", 36, 2)
    manuela = Person("manuela", 30, 8)
    cristina = Person("cristina", 29, 2)
    extra_friends = Enumerable([pepe, manuela, cristina])
    print(friends.mutual_friends_with_the_same_age(extra_friends))

    friends.bring_friends_together(extra_friends)
    print(friends)
