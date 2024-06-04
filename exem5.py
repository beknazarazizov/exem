#1.	Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating  (id,name,price, color,image) .
"""
import requests
import psycopg2
from pprint import pprint
import time
import threading
"""

# 1- javob
import requests
import psycopg2
from pprint import pprint
import time
import threading


db_name = 'customer'
password = '5760'
host = 'localhost'
port = 5432
user = 'postgres'

#
# conn=psycopg2.connect(dbname = db_name,
#                         password = password,
#                         host = host,
#                         port = port,
#                         user = user)
#id,name,price, color,image
# cur=conn.cursor()

created_table_query = """ create table if not exists product(
     id serial primary key,
     name varchar(50) not null ,
     price float,
     collor varchar(30),
     image varchar(255)
);
"""

# cur.execute(created_table_query)
# conn.commit()
# print('Table successfully created')

#2.	Insert_product , select_all_products , update_product,delete_product nomli funksiyalar yarating.
 # 2- javob
# def insert_products_data(name_vch ,image_vch):
#     insert_query=""" INSERT INTO product(name,image)
#          VALUES(%s,%s);"""
#     data_params=name_vch,image_vch
#     cur.execute(insert_query,data_params)
#     conn.commit()
# insert_products_data('sofa','bjkdbsbkjdbsfbhhvkjbhugjhhjdghj')

# def update_data_of_products():
#     product_id=input("id>>  ")
#     product_price=input('price>>  ')
#     product_collor=input('collor>>  ')
#     update_query="""update product set collor=%s, price=%s where id=%s"""
#     cur.execute(update_query,(product_collor,product_price,product_id))
#     conn.commit()
#     print("Update product")
# update_data_of_products()

# def delete_data_of_product(id):
#     delete_query="""delete from product where id=%s"""
#     delete_params=id
#     cur.execute(delete_query,delete_params)
#     conn.commit()
# delete_data_of_product('1')

# from pprint import pprint
# def select_data_of_product ():
#     select_query="""select * from product"""
#     cur.execute(select_query)
#     row=cur.fetchall()
#     pprint(row)
# select_data_of_product()

# 3.	Alphabet nomli class yozing .class obyektlarini  iteratsiya qilish imkoni
# bo’lsin (iterator).  obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin
#  3-javob

# class Alphabit:
#     def __init__(self):
#         self.chractr= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         self.index=0
#
#     def __iter__(self):
#         self.index=0
#         return self
#
#     def __next__(self):
#         if self.index<len(self.chractr):
#             chractr=self.chractr[self.index]
#             self.index+=1
#             return chractr
#         else:
#             raise StopIteration
#
#
# alfa=Alphabit()
# for letter in alfa:
#     print(letter)
#
## 4-javob
# import threading
# import time
# def print_numbers():
#     for number in range(1,5+1):
#         print(number)
# alphabet = [chr(i) for i in range(97, 123)]
# def print_letters():
#     for i in range(1,5+1):
#         print(alphabet[i])
#
# thread_numbers = threading.Thread(target=print_numbers)
# thread_letters = threading.Thread(target=print_letters)
#
#
# thread_numbers.start()
# thread_letters.start()
#
# thread_numbers.join()
# thread_letters.join()

# 5.	Product nomli class yarating (1 – misoldagi Product ).Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin.
##5-javob

# class Product:
#     def __init__(self,name,collor,price,image):
#         self.name=name
#         self.collor=collor
#         self.price=price
#         self.image=image
#
#     def save(self):
#         # db_name = 'shoping'
#         # password = '5760'
#         # host = 'localhost'
#         # port = 5432
#         # user = 'postgres'
#         #
#         # conn = psycopg2.connect(dbname=db_name,
#         #                         password=password,
#         #                         host=host,
#         #                         port=port,
#         #                         user=user)
#
#         insert_user_query = """ insert into product(name,collor,price,image)
#                                  values (%s,%s,%s,%s);"""
#         data_param = self.name, self.collor, self.price, self.image
#         cur.execute(insert_user_query,data_param)
#
#
#         conn.commit()
#         conn.close()
# get_product=Product('iphon','bleack',345,'uhifdjhisljhsbjsl')
# get_product.save()



##6-javob

db_params={
'dbname' : 'customer',
'password' : '5760',
'host' : 'localhost',
'port' : 5432,
'user' : 'postgres'
}

class DbConnect:
    def __init__(self,db_params: dict):
        self.db_params=db_params
    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)

        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.conn is not None:
            self.conn.close()

    def commit(self):
        self.conn.commit()

    def rolbacke(self):
        self.conn.rollback()

with DbConnect(db_params) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM product;")
        rows=cur.fetchall()
        for rov in rows:
            print(rov)

## 7-javob

# import requests
# from pprint import pprint
# url='https://dummyjson.com/products/'
# respons=requests.get(url)
# pprint(respons.json())
# print(respons.json()['products'])
# for product in respons.json()['products']:
#     pprint(product)

# insert_into_query="""INSERT INTO product(name,)
#                     VALUES (%s);"""
# for product in respons.json()['products']:
#     cur.execute(insert_into_query,product['firstName'])
#     conn.commit()

# malumotlarini qidirishga vaqt yetmadfi faqat nemini insort qippoydim



