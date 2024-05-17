# class Person:
#     def __init__(self, first_name: str, last_name: str, age: int) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def get_age(self):
#         return f'I am {self.age} years old'
#
#     def __str__(self) -> str:
#         return f'{self.first_name} - {self.last_name} - {self.age}'
#
#
# john = Person("John", "Doe", 35)
# mike = Person("Mike", "Tyson", 64)
#
# # print(john.age)
# # print(john.get_age())
# # print(mike.get_age)
# # from sys import getsizeof
#
# # print(getsizeof(mike))
#
# # print()
# # def func():
# #     print('I am a function')
# #
# #
# # print(func)
# population = []
# while True:
#     choice = input("Dou you wanna quit mode --> (exit) ")
#     citizen = dict()
#     # citizen = {}
#     if choice == "exit":
#         print("Come back again 😊")
#         break
#
#     fullname = input("Fullname : ")
#     address = input("Address : ")
#     age = input("Age : ")
#
#     citizen["fullname"] = fullname
#     citizen["address"] = address
#     citizen["age"] = age
#
#     passport = dict()
#
#     serial = input("Serial : ")
#     number = input("Number : ")
#
#     passport["serial"] = serial
#     passport["number"] = number
#
#     citizen["passport"] = passport
from typing import Optional, List


class Passport:
    def __init__(self, serial: str, number: str) -> None:
        self.serial = serial
        self.number = number

    def __repr__(self):
        return f'{self.serial} => {self.number}'


class Citizen:
    def __init__(self, full_name: str, passport: Optional[Passport] = None, address: Optional[str] = None,
                 age: Optional[int] = None):
        self.full_name = full_name
        self.address = address
        self.age = age
        self.passport = passport

    # def __str__(self):
    #     return f'{self.full_name} => {self.age}'

    def __repr__(self):
        return f'{self.full_name} => {self.passport}'


class Population:
    def __init__(self, name: str):
        self.name = name
        self.citizens = []

    def __repr__(self):
        return f'{self.name} => included in population {len(self.citizens)}'


john_passport = Passport('AA', '111')
mike_passport = Passport('BB', '222')

john = Citizen(full_name='John', passport=john_passport)
mike = Citizen(full_name='Mike', passport=mike_passport)

england = Population(name='England')
russian = Population(name='Russian')

england.citizens.append(john)
england.citizens.append(mike)
print(england.citizens)
