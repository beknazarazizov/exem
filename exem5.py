#1.	Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating  (id,name,price, color,image) .
# 1- javob

import psycopg2

db_name = 'customer'
password = '5760'
host = 'localhost'
port = 5432
user = 'postgres'


conn=psycopg2.connect(dbname = db_name,
                        password = password,
                        host = host,
                        port = port,
                        user = user)
#id,name,price, color,image
cur=conn.cursor()

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


##5-javob

##6-javob

# import psycopg2
#
# class DbConnect:
#     def init(self, con):
#         self.con = con
#
#     def enter(self):
#         self.conn = psycopg2.connect(**self.con)
#         self.cur = self.conn.cursor()
#         return self.cur
#
#     def exit(self, exc_type, exc_value, traceback):
#         self.conn.commit()
#         self.cur.close()
#         self.conn.close()

# with DbConnect(conn)as cur:
#     cur.execute("SELECT version();")
#     print(cur.fetchone()[0])

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



