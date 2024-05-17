#trello
from typing import Optional,List

class Tudu:
    def __init__(self,kitob:Optional[str]=None,sport:Optional[str]=None,zaruriyat:Optional[str]=None):
        self.kitob = kitob
        self.sport = sport
        self.zaruriyat =zaruriyat
    def __repr__(self):
        return f'{self.kitob},xudayberdi tuxtaboyev qalamiga mansub asar'
    def __repr__(self):
        return f'{self.sport},futbol bu shunchaki qiziqish eng yaxshi kurfgan mashgulotlarimdan biri'
    def __repr__(self):
        return f'{self.zaruriyat}'
class Aplication:
    def __init__(self,name,kitob:Optional[Tudu]=None,sport:Optional[Tudu]=None):
        self.name =name
        tod_list=[]
    def __str__(self):
        return f'{self.name}'
    def add_tod_list(self):
        pass
        pass
    def Update_tod_list(self):
        pass
    def Delete_tod_list(self):
       a= input(""" kitob uqib buldizmi
        1.ha
        2.yuq
        sport bajardizmi
        3.ha
        4,yuq
        >>>""")
       if a=="1":
           del self.kitob
       elif a=='2':
           print("churli")
       elif a=='3':
           del self.sport
       else:
           print("chunalr")
trello=Aplication("Trello",kitob="oqkema",sport="futbol")

print(trello.Delete_tod_list())



