from  typing import Optional
from datetime import datetime

class Dars:
    def __init__(self,
                 name:Optional[str] = None,
                 age: Optional[int] = None,
                 email:Optional[str] = None,):
        self.name = name
        self.age = age
        self.email = email
    @classmethod
    def from_dict(cls,
                  name:Optional[str] = None,age: Optional[int] = None):
    def user(self):
        return f' ismim {self.name},yoshim {self.age}, emailim {self.email}'

p1=Dars(name='jasur', age=20, email='<EMAIL>')
print(p1.user())