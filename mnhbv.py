
import psycopg2

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='jasur',
                        host='localhost',
                        port=5432)

cur = conn.cursor()

from typing import Optional
from datetime import datetime


# iphone = Product('Iphone', 'Image', True)
# iphone.save()
# (Product.get_all())
class User:
    def __init__(self,
                 name:Optional[str]=None,
                 age:Optional[int]=None,
                 email:Optional[str]=None,
                 create_at:Optional[datetime]=None
                 ):
        self.name=name
        self.age=age
        self.email=email
        self.create_at=create_at or datetime.now()
    @staticmethod

    def get_all():
        select_product_all = '''select * from user;'''
        cur.execute(select_product_all)
        rows = cur.fetchall()
        for i in rows:
            print(i,end=' ')

    def insert(self):
        insert_product_obj = '''insert into user (name,age,email,create_at) values (%s,%s,%s,%s);'''
        data = (self.name, self.age, self.email, self.create_at)
        cur.execute(insert_product_obj, data)
        conn.commit()
    def delete(self):

         name = input('name : ')
         delete_data_query = 'delete from categories where name= %s;'
         data = (name,)
         cur.execute(delete_data_query, data)
         conn.commit()
    def update(self):

        update_data_query = """update categories set email = %s,age = %s where name = %s"""
        name = input('Enter name: ')
        age = int(input('Enter age : '))
        email = input('email : ')
        cur.execute(update_data_query, (email, age, name))
        conn.commit()
p1=User(name='jasur',age=19,email='jasur@gmil.com')
p2=User(name='hikmat',age=20,email='hikmat@gmail.com')
p3=User(name='john',age=23,email='john@gmil.com')
print(p1.insert())
User.get_all()
User.update()
#shu tariqa delete uptade larni ishlatamiz
#class yaratishdan maqsad faqat bizga insert qilishda objekt orqali qushishimizda yordam beradi
#qolganlarini oddiy biz ishlatgan funksiya ichida stattik nethod orqali yaratib ketaveramiz



