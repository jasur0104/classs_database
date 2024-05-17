# name , age , id , passport,voice
from typing import Optional
from uuid import uuid4, UUID


class Animal:
    specials = 'Similar families'

    def __init__(self,
                 id: Optional[UUID] = None,
                 name: Optional[str] = None,
                 voice: Optional[str] = None,
                 age: Optional[int] = None,
                 passport: Optional[str] = None) -> None:
        self.id = id or uuid4()
        self.name = name
        self.voice = voice
        self.age = age
        self.passport = passport

    @classmethod
    def get_specials(cls):
        return f'This is class method => {cls.specials}'

    @classmethod
    def set_specials(cls, new_variable):
        if isinstance(new_variable, str):
            cls.specials = new_variable
        else:
            print('Typeerror')

    def get_info(self):
        return f'{self.id} - {self.name} - {self.voice} - {self.age}'

    def set_age(self, new_age):
        if isinstance(new_age, int):
            self.age = self.age + new_age
        else:
            print('TypeError. Age must be integer type')

    @staticmethod
    def is_adult(animal_age):
        if animal_age < 6:
            print('This is not adult')
        else:
            print('This animal adult')


#
# dog = Animal(name='Beethoven', voice='Woof Woof', age=5)
#
# dog.set_age(4)
#
# print(dog.age)

# cat = Animal(name='Tom', voice='Meow', age=2)
# print(dog.get_info())
# print('-----------------------------------------')
# print(cat.get_info())
# print(isinstance(dog, Animal))

# print(Animal.specials)
duck = Animal()

# print(duck.specials)
# print(Animal.specials)

# print(Animal.get_specials())
# (Animal.set_specials('Mammals'))
# print(Animal.get_specials())

x = int(input('Enter a number: '))
Animal.is_adult(x)
