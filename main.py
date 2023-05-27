# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telegram
import telebot
# Импорт модуля Psycopg2 в программу
import psycopg2
import os
# С помощью класса Error можно обрабатывать любые ошибки и исключения базы данных
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# Подключаем модуль для работы с датой/веременем
from datetime import datetime
# Функция для преобразования объектов datetime с использованием часовых поясов.
#import pytz
#local_tz = pytz.timezone('Asia/Almaty')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Для определения имени пользователя
import getpass
# QR Code
#from pyzbar.pyzbar import decode
#from PIL import Image
#import cv2 
#import numpy 

# Указываем токен
API_TOKEN = '5281292321:AAHcrX098QqGom13KF7-_trKIeXEV6ZSOgQ'
bot = telebot.TeleBot(API_TOKEN)
# Текст приглашения
#welcome_message = "Тестовая версия\nДобро пожаловать!\nБот предназначен для поиска вакансий на рынке труда"
welcome_message = "Сынақ нұсқасы\nқош келдіңіз!\nбот еңбек нарығында бос жұмыс орындарын табуға арналған"
# Справочная информация
#help_message = "Помощь"

# Строка соединения (Connecion string)
#database_name="deju147jiuqj51"
database_name="vacancy"

# Подключаем модуль для SQLite
import sqlite3


# Глобальные переменные
DOSSIER_FLAG = False

def get_connection_string():
    # Подключение к SQLite 
    # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
    # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                             
    #cs = sqlite3.connect('db.sqlite3')
    #print("База данных SQLite подключена")
    #cs = psycopg2.connect("postgres://dzlzpndnpafmkm:083eec1d9a8962b5dc40e071d8e8c25655351820dbc979d516d0a0b8194a1bdc@ec2-3-215-83-124.compute-1.amazonaws.com:5432/d333vksqb1unsv", sslmode="require")
    cs = psycopg2.connect("postgres://vacancy77_user:WOD4lJZzVKPteet62VxF9eqlMW0wtyam@dpg-chnn5j9mbg5577n9esdg-a.frankfurt-postgres.render.com/vacancy77", sslmode="require")
    print("База данных PostgreSQL подключена")
    return cs

def get_connection_string2():
    # Подключение к SQLite 
    # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
    # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                             
    #cs = sqlite3.connect('db.sqlite3')
    #print("База данных SQLite подключена")
    #cs = psycopg2.connect("postgres://dzlzpndnpafmkm:083eec1d9a8962b5dc40e071d8e8c25655351820dbc979d516d0a0b8194a1bdc@ec2-3-215-83-124.compute-1.amazonaws.com:5432/d333vksqb1unsv", sslmode="require")
    cs = psycopg2.connect("postgres://vacancy77_user:WOD4lJZzVKPteet62VxF9eqlMW0wtyam@dpg-chnn5j9mbg5577n9esdg-a.frankfurt-postgres.render.com/vacancy77", sslmode="require")
    print("База данных PostgreSQL подключена")
    return cs
"""

def get_connection_string():
    #print("get_connection_string")
    cs = psycopg2.connect(user="postgres",
                            password="3552998",
                            host="127.0.0.1",
                            port="5432",
                            database="vacancy")
    return cs

def get_connection_string2():
    #print("get_connection_string2")
    cs = psycopg2.connect(user="postgres",
                            password="3552998",
                            host="127.0.0.1",
                            port="5432")
    return cs
"""

# Метод, который получает сообщения и обрабатывает их
#@bot.message_handler(content_types=['text'])
# Пользователь клиент
class Customer:
    def __init__(self, id, telegram_id, phone_number, first_name, last_name, fio, birthday, education, experience):
        self.id = id
        self.telegram_id = telegram_id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.fio = fio
        self.birthday = birthday
        self.education = education
        self.experience = experience

# Город
class City:
    def __init__(self, title):
        self.title = title

# Организация
class Organization:
    def __init__(self, title, details, price, phone):
        self.title = title
        self.details = details
        self.address = address
        self.phone = phone

# Категория (вид деятельности)
class Category:
    def __init__(self, title):
        self.title = title

# Вакансия
class Vacancy:
    def __init__(self, datev, city, organization, category, position, details, salary, date_close):
        self.datev = datev
        self.city = city
        self.organization = organization
        self.category = category        
        self.position = position
        self.details = details
        self.salary = salary        
        self.date_close = date_close

# Отклик на вакансию
class Respond:
    def __init__(self, dater, vacancy, customer):
        self.dater = dater
        self.vacancy = vacancy
        self.customer = customer

# Создание базы данных 
"""
try:
    # Подключение к PostgreSQL 
    conn = get_connection_string2()
    # Транзакция в режиме «autocommit» (автофиксация), то есть каждый оператор выполняется в своей отдельной транзакции, которая неявно фиксируется в конце оператора
    # (если оператор был выполнен успешно; в противном случае транзакция откатывается).
    #conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)    
    # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
    # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
    cursor = conn.cursor()
    # Проверка наличия базы данных
    cursor.execute("SELECT * FROM pg_database WHERE datname = '" + database_name + "'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("База данных уже существует")        
    else:
        cursor.execute("CREATE DATABASE " + database_name)
        print("База данных создана")        
    # Закрыть объект cursor после завершения работы.
    cursor.close()
    # Закрыть соединение после завершения работы.
    conn.close()
    # Подключение к PostgreSQL 
    conn = get_connection_string()
    # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
    # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
    cursor = conn.cursor()
    # Проверка наличия таблицы клиентов
    cursor.execute("SELECT 1 FROM pg_tables WHERE tablename = 'customer'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("Таблица клиентов уже существует")        
    else:
        create_table_query = '''CREATE TABLE "customer" (
            "id"	integer NOT NULL,
            "telegram_id"	integer NOT NULL,
            "phone_number"	varchar(20) NOT NULL,
            "first_name"	varchar(64) NOT NULL,
            "last_name"	varchar(64),
            PRIMARY KEY("id" AUTOINCREMENT) );'''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица клиентов создана")        
    # Проверка наличия таблицы city
    cursor.execute("SELECT 1 FROM pg_tables WHERE tablename = 'city'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("Таблица city уже существует")        
    else:
        create_table_query = '''CREATE TABLE city (
            id bigint NOT NULL DEFAULT nextval('city_id_seq'::regclass),
            title character varying(196) COLLATE pg_catalog."default" NOT NULL,
            CONSTRAINT city_pkey PRIMARY KEY (id),
            CONSTRAINT city_title_key UNIQUE (title)
            );'''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица city создана")
    # Проверка наличия таблицы category
    cursor.execute("SELECT 1 FROM pg_tables WHERE tablename = 'category'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("Таблица category уже существует")        
    else:
        create_table_query = '''CREATE TABLE category (
            id bigint NOT NULL DEFAULT nextval('category_id_seq'::regclass),
            title character varying(196) COLLATE pg_catalog."default" NOT NULL,
            CONSTRAINT category_pkey PRIMARY KEY (id),
            CONSTRAINT category_title_key UNIQUE (title)
            );'''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица category создана")         
    # Проверка наличия таблицы organization
    cursor.execute("SELECT 1 FROM pg_tables WHERE tablename = 'organization'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("Таблица organization уже существует")        
    else:
        create_table_query = '''CREATE TABLE organization
            (id bigint NOT NULL DEFAULT nextval('organization_id_seq'::regclass),
            title character varying(196) COLLATE pg_catalog."default" NOT NULL,
            details text COLLATE pg_catalog."default",
            address character varying(128) COLLATE pg_catalog."default" NOT NULL,
            phone character varying(128) COLLATE pg_catalog."default" NOT NULL,
            CONSTRAINT organization_pkey PRIMARY KEY (id));'''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица organization создана")        
    # Проверка наличия таблицы vacancy
    cursor.execute("SELECT 1 FROM pg_tables WHERE tablename = 'vacancy'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("Таблица vacancy уже существует")        
    else:
        create_table_query = '''CREATE TABLE vacancy (
            id bigint NOT NULL DEFAULT nextval('vacancy_id_seq'::regclass),
            datev timestamp with time zone NOT NULL,
            "position" character varying(196) COLLATE pg_catalog."default" NOT NULL,
            details text COLLATE pg_catalog."default" NOT NULL,
            salary character varying(196) COLLATE pg_catalog."default" NOT NULL,
            date_close timestamp with time zone,
            category_id bigint NOT NULL,
            city_id bigint NOT NULL,
            organization_id bigint NOT NULL,
            CONSTRAINT vacancy_pkey PRIMARY KEY (id),
            CONSTRAINT vacancy_category_id_ae4396de_fk_category_id FOREIGN KEY (category_id)
                REFERENCES public.category (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                DEFERRABLE INITIALLY DEFERRED,
            CONSTRAINT vacancy_city_id_6bff3a25_fk_city_id FOREIGN KEY (city_id)
                REFERENCES public.city (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                DEFERRABLE INITIALLY DEFERRED,
            CONSTRAINT vacancy_organization_id_baad833f_fk_organization_id FOREIGN KEY (organization_id)
                REFERENCES public.organization (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                DEFERRABLE INITIALLY DEFERRED);'''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица vacancy создана")
        # Проверка наличия таблицы respond
    cursor.execute("SELECT 1 FROM pg_tables WHERE tablename = 'respond'")
    result = cursor.fetchall()
    if len(result) > 0:
        print("Таблица respond уже существует")        
    else:
        create_table_query = '''CREATE TABLE public.respond (
            id bigint NOT NULL DEFAULT nextval('respond_id_seq'::regclass),
            dater timestamp with time zone NOT NULL,
            customer_id bigint NOT NULL,
            vacancy_id bigint NOT NULL,
            CONSTRAINT respond_pkey PRIMARY KEY (id),
            CONSTRAINT respond_customer_id_c89f12e9_fk_customer_id FOREIGN KEY (customer_id)
                REFERENCES public.customer (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                DEFERRABLE INITIALLY DEFERRED,
            CONSTRAINT respond_vacancy_id_4756d036_fk_vacancy_id FOREIGN KEY (vacancy_id)
                REFERENCES public.vacancy (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                DEFERRABLE INITIALLY DEFERRED);'''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица respond создана") 
except (Exception, Error) as error:
    print(error)    
"""
# Проверка наличия пользовтаеля Telegram (telegram_id) в базе данных пользователей
def check_telegram_id(telegram_id):
    print("check_telegram_id")        
    try:
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        # SQL-запрос
        sql = "SELECT id, telegram_id, phone_number, first_name, last_name, fio, birthday, education, experience FROM customer WHERE telegram_id=" + str(telegram_id)
        #print(sql)
        # С помощью метода execute объекта cursor можно выполнить запрос в базу данных из Python.
        # Он принимает SQL-запрос в качестве параметра и возвращает resultSet (строки базы данных):
        cursor.execute(sql)
        # Получить результат запроса из resultSet можно с помощью методов, например, fetchAll()
        row = cursor.fetchone()
        # Если такого пользователя нет то вернуть false если есть то true
        if row is None:
            exists = False
        else:
            global customer  
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            exists = True
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        print("exists ", exists)
        return exists
    except (Exception, Error) as error:
        print("check_telegram_id: ",error)        

# Проверка наличия пользовтаеля Telegram (phone_number) в базе данных пользователей
def check_phone_number(phone_number):
    print("check_phone_number")
    try:
        # Проверить, есть ли такой пользователь в базе данных
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        # SQL-запрос
        sql = "SELECT id, telegram_id, phone_number, first_name, last_name FROM customer WHERE phone_number='" + phone_number + "'"
        # С помощью метода execute объекта cursor можно выполнить запрос в базу данных из Python.
        # Он принимает SQL-запрос в качестве параметра и возвращает resultSet (строки базы данных):
        cursor.execute(sql)
        # Получить результат запроса из resultSet можно с помощью методов, например, fetchAll()
        row = cursor.fetchone()
        # Если такого пользователя нет то вернуть false если есть то true
        if row is None:
            exists = False
        else:
            # Пользователь
            global customer  
            customer = customer(row[0], row[1], row[2], row[3], row[4])
            exists = True
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        return exists
    except (Exception, Error) as error:
        print("check_phone_number ", error)        

# Добавление пользователя
def add_customer():
    print("add_customer")
    try:
        if customer.last_name is not None:
            print("1")
            sql = "INSERT INTO customer (telegram_id, phone_number, first_name, last_name) VALUES (" + str(customer.telegram_id) +", '" + customer.phone_number +"', '" + customer.first_name +"', '" + customer.last_name +"') "
        else:
            sql = "INSERT INTO customer (telegram_id, phone_number, first_name, last_name) VALUES (" + str(customer.telegram_id) +", '" + customer.phone_number +"', '" + customer.first_name +"', '') "
        #print(sql)
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor() 
        cursor.execute(sql)
        conn.commit()        
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        print("Пользователь добавлен")
        # Обновить экземпляр класа Customer (ролучить id таблицы Customer)
        check_telegram_id(customer.telegram_id)
        #print(customer.id)
        #print(customer.telegram_id)
        #print(customer.phone_number)
        #print(customer.first_name)
        #print(customer.last_name)
    except (Exception, Error) as error:
        print("add_customer ",error)
        bot.reply_to(message, 'упс')

4# Запись/проверка контакта в БД
@bot.message_handler(content_types=['contact']) #Объявили ветку, в которой прописываем логику на тот случай, если пользователь решит прислать номер телефона :) 
def contact(message):
    print("contact")
    try:
        # Пользователь
        global customer        
        # print(message.contact) Выводим в панели контактные данные
        #print(message.contact.user_id)
        #print(message.contact.phone_number)
        #print(message.contact.first_name)
        #print(message.contact.last_name)
        #print(message.contact.user_id)
        if message.contact.last_name is None:
            customer = Customer(None, message.contact.user_id, message.contact.phone_number, message.contact.first_name, None, None, None, None, None)
        else:
            customer = Customer(None, message.contact.user_id, message.contact.phone_number, message.contact.first_name, message.contact.last_name, None, None, None, None)
        # Проверить, есть ли такой пользователь в базе данных, если нет то добавить
        if check_telegram_id(customer.telegram_id):
            print("Пользователь существует")
        else:
            print("Необходимо добавить пользователя")
            add_customer()       
        # Подключаем клавиатуру
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # Указываем название кнопок, добавляем клавиатуру
        #markup.add('Поиск вакансии').add('Мои отклики').row('Изменить анкету')
        markup.add('Жұмыс іздеу').add('Менің жауаптарым').row('Сауалнаманы өзгерту')
        # Стартовое сообщение
        #msg = bot.reply_to(message, '\nЧто Вы хотите сделать?', reply_markup=markup)
        msg = bot.reply_to(message, '\nСіз не істегіңіз келеді?', reply_markup=markup)
        # Выбор действия 
        bot.register_next_step_handler(msg, menu)        
    except Exception as error:
        print("contact", error)
        bot.reply_to(message, 'упс')

# Список городов в которых есть не закрытые вакансии
def get_city(message):
    print("get_city")
    #if message.text=="На главную":
    if message.text=="Басты бетке":
        send_welcome(message)
    else:
        city_list = []
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT DISTINCT(city.title) "
        sql = sql + "FROM vacancy LEFT JOIN city ON vacancy.city_id=city.id  "
        sql = sql + "WHERE vacancy.date_close Is Null "
        sql = sql + "ORDER BY city.title "
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            city_list.append(row[0])        
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        return city_list

# Список категорий в городе в котрых есть не закрытые вакансии
def get_category(message):
    print("get_category")
    #if message.text=="На главную":
    if message.text=="Басты бетке":
        send_welcome(message)
    else:
        global global_city
        global_city = message.text
        print("get_category")
        category_list = []
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT DISTINCT(category.title) "
        sql = sql + "FROM vacancy LEFT JOIN city ON vacancy.city_id=city.id LEFT JOIN category ON vacancy.category_id=category.id  "
        sql = sql + "WHERE vacancy.date_close Is Null AND city.title='" + global_city + "'"
        sql = sql + "ORDER BY category.title"
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            category_list.append(row[0])        
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        return category_list

# Список позиций
def get_position(message):
    print("get_position")
    #if message.text=="На главную":
    if message.text=="Басты бетке":
        send_welcome(message)
    else:
        global global_category
        global_category = message.text
        position_list = []
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT vacancy.id, vacancy.datev, city.title AS city, organization.title AS organization, category.title AS category, vacancy.\"position\", vacancy.details, vacancy.salary, organization_id "
        sql = sql + "FROM vacancy LEFT JOIN city ON vacancy.city_id=city.id LEFT JOIN category ON vacancy.category_id=category.id LEFT JOIN organization ON vacancy.organization_id=organization.id "
        sql = sql + "WHERE vacancy.date_close Is Null AND city.title='" + global_city + "'  AND category.title='" + global_category + "' "
        sql = sql + "ORDER BY category.title"
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            position_list.append(row[5])
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        return position_list

# Список Организаций
def get_organization(message):
    print("get_organization")
    #if message.text=="На главную":
    if message.text=="Басты бетке":
        send_welcome(message)
    else:
        global global_position
        global_position = message.text
        organization_list = []
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "SELECT vacancy.id, vacancy.datev, city.title AS city, organization.title AS organization, category.title AS category, vacancy.\"position\", vacancy.details, vacancy.salary, organization_id "
        sql = sql + "FROM vacancy LEFT JOIN city ON vacancy.city_id=city.id LEFT JOIN category ON vacancy.category_id=category.id LEFT JOIN organization ON vacancy.organization_id=organization.id "
        sql = sql + "WHERE vacancy.date_close Is Null AND city.title='" + global_city + "' AND category.title='" + global_category + "' AND vacancy.\"position\"='" + global_position + "' "
        sql = sql + "ORDER BY category.title"
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            organization_list.append(row[3])
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        return organization_list

# Декоратор @message_handler реагирует на входящие сообщение.
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print("send_welcome")
    print(message.text)   
    try:
        # Проверить, есть ли такой пользователь в базе данных, если нет то предложить отправить контакт и добавить его
        if check_telegram_id(message.chat.id):
            #print("Пользователь существует")
            # print(message.contact) Выводим в панели контактные данные
            # customer = Customer(message.contact.telegram_id, message.contact.phone_number, message.contact.first_name, message.contact.last_name)
            # Подключаем клавиатуру
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            # Указываем название кнопок, добавляем клавиатуру
            #markup.add('Поиск вакансии').add('Мои отклики').row('Изменить анкету')
            markup.add('Жұмыс іздеу').add('Менің жауаптарым').row('Сауалнаманы өзгерту')
            # Выбор действия 
            bot.register_next_step_handler(message, menu)
            #bot.send_message(message.chat.id, welcome_message, reply_markup=markup)
            bot.send_message(message.chat.id, welcome_message, reply_markup=markup)
        else:
            #print("Пользователя не существует")
            # Подключаем клавиатуру
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True)
            # Указываем название кнопки, которая появится у пользователя
            #contact_button = types.KeyboardButton(text="Отправить контакт", request_contact=True)
            contact_button = types.KeyboardButton(text="Контактіні жіберу", request_contact=True)
            # Добавляем эту кнопку
            keyboard.add(contact_button)
            #bot.send_message(message.chat.id, welcome_message + "\nНажмите на кнопку \"Отправить контакт\" отправьте свой номер телефона.", reply_markup=keyboard)
            bot.send_message(message.chat.id, welcome_message + "\nТүймені басыңыз \"Контактіні жіберу\" телефон нөміріңізді жіберіңіз.", reply_markup=keyboard)
    except Exception as error:
        print(error)
        bot.reply_to(message, str(error))
    
def menu(message):
    print("menu")
    #print(message.chat.id)
    # Флаг - изменение досье
    global DOSSIER_FLAG
    DOSSIER_FLAG=False
    print("DOSSIER_FLAG", DOSSIER_FLAG)
    try:
        #if (message.text == u'Поиск вакансии'):
        if (message.text == u'Жұмыс іздеу'):
            #bot.send_message(message.chat.id, "Введите город");            
            #bot.register_next_step_handler(message, get_city);
            # Список городов с не закрытыми вакансиями
            city_list = get_city(message)
            # Подключаем клавиатуру
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            # Указываем название кнопок, добавляем клавиатуру
            for i in range(0, len(city_list)):
                markup.add(city_list[i])
            # Кнопка в начало (На главную)
            #markup.add("На главную")
            markup.add("Басты бетке")
            # Выбор действия 
            bot.register_next_step_handler(message, menu2)
            bot.send_message(message.chat.id, welcome_message, reply_markup=markup)
        #elif (message.text == u'Мои отклики'):
        elif (message.text == u'Менің жауаптарым'):
            # История откликов
            history(message)
        #elif (message.text == u'Изменить анкету'):
        elif (message.text == u'Сауалнаманы өзгерту'):
            # Изменить анкету
            bot.send_message(message.chat.id, "\n<b>ФИО:</b> " + customer.fio +
                             "\n<b>Дата рождения:</b> " + customer.birthday.strftime('%d.%m.%Y') +
                             "\n<b>Образование:</b> " + customer.education +
                             "\n<b>Опыт работы:</b> " + customer.experience , parse_mode=telegram.ParseMode.HTML )         
            dossier(message)
    except Exception as error:
        print("menu ", error)
        #bot.reply_to(message, str(error))

def menu2(message):
    print("menu2")
    #print(message.chat.id)
    #print(message.text)
    try:
        # Список городов с не закрытыми вакансиями
        category_list = get_category(message)
        # Подключаем клавиатуру
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # Указываем название кнопок, добавляем клавиатуру
        for i in range(0, len(category_list)):
            markup.add(category_list[i])
        # Кнопка в начало (На главную)
        # markup.add("На главную")            
        markup.add("Басты бетке")            
        # Выбор действия 
        bot.register_next_step_handler(message, menu3)
        bot.send_message(message.chat.id, message.text, reply_markup=markup)
    except Exception as error:
        print("menu2 ", error)
        #bot.reply_to(message, str(error))

def menu3(message):
    print("menu3")
    #print(message.chat.id)
    #print(message.text)
    try:
        # Список городов с не закрытыми вакансиями
        position_list = get_position(message)
        # Подключаем клавиатуру
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # Указываем название кнопок, добавляем клавиатуру
        for i in range(0, len(position_list)):
            markup.add(position_list[i])
        # Кнопка в начало (На главную)
        #markup.add("На главную")                        
        markup.add("Басты бетке")                        
        # Выбор действия 
        bot.register_next_step_handler(message, menu4)
        bot.send_message(message.chat.id, message.text, reply_markup=markup)
    except Exception as error:
        print("menu3 ", error)
        #bot.reply_to(message, str(error))

def menu4(message):
    print("menu4")
    #print(message.chat.id)
    #print(message.text)
    try:
        # Список городов с не закрытыми вакансиями
        organization_list = get_organization(message)
        # Подключаем клавиатуру
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # Указываем название кнопок, добавляем клавиатуру
        for i in range(0, len(organization_list)):
            markup.add(organization_list[i])
        # Кнопка в начало (На главную)
        #markup.add("На главную")            
        markup.add("Басты бетке")            
        # Выбор действия 
        bot.register_next_step_handler(message, show_vacancy)
        bot.send_message(message.chat.id, message.text, reply_markup=markup)
    except Exception as error:
        print("menu4 ", error)
        #bot.reply_to(message, str(error))
        
# История 
def show_vacancy(message):
    print("show_vacancy")
    #if message.text=="На главную":
    if message.text=="Басты бетке":
        send_welcome(message)
    else:    
        #print(message.chat.id)
        #print(message.text)
        global global_organization
        global_organization = message.text
        try:
            # Подключение к PostgreSQL 
            conn = get_connection_string()
            # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
            # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
            cursor = conn.cursor()
            sql = "SELECT vacancy.id, vacancy.datev, city.title AS city, organization.title AS organization, category.title AS category, vacancy.\"position\", vacancy.details, vacancy.salary, organization_id "
            sql = sql + "FROM vacancy LEFT JOIN city ON vacancy.city_id=city.id LEFT JOIN category ON vacancy.category_id=category.id LEFT JOIN organization ON vacancy.organization_id=organization.id "
            sql = sql + "WHERE vacancy.date_close Is Null AND city.title='" + global_city + "' AND category.title='" + global_category + "' AND vacancy.\"position\"='" + global_position + "' AND organization.title='" + global_organization + "' "
            sql = sql + "ORDER BY category.title"
            #print(sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            # id вакансии
            global vacancy_id        
            for row in results:
                vacancy_id = row[0]
                #bot.send_message(message.chat.id,  "<b>Город:</b> " + str(row[2]) + "\n<b>Организация:</b> " + str(row[3]) + "\n<b>Категория:</b> " + str(row[4]) + "\n<b>Позиция:</b> " + str(row[5]) + "\n<b>Подробности:</b> " + str(row[6]) + "\n<b>Зарплата:</b> " + str(row[7]) , parse_mode=telegram.ParseMode.HTML )                
                bot.send_message(message.chat.id,  "<b>Қала:</b> " + str(row[2]) + "\n<b>Ұйымдастыру:</b> " + str(row[3]) + "\n<b>Санат:</b> " + str(row[4]) + "\n<b>Позиция:</b> " + str(row[5]) + "\n<b>Толығырақ:</b> " + str(row[6]) + "\n<b>Жалақы:</b> " + str(row[7]) , parse_mode=telegram.ParseMode.HTML )                
            print("vacancy_id ", vacancy_id)               
            # Закрыть объект cursor после завершения работы.
            cursor.close()
            # Закрыть соединение после завершения работы.
            conn.close()
            # Подключаем клавиатуру
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            # Указываем название кнопок, добавляем клавиатуру
            #markup.add('Откликнуться').row('На главную')    
            markup.add('Жауап беру').row('Басты бетке')    
            # Выбор действия
            bot.register_next_step_handler(message, create_respond)
            bot.send_message(message.chat.id, message.text, reply_markup=markup)        
        except Exception as error:
            print("show_vacancy ", error)
            #bot.reply_to(message, 'упс')       

# Создать заявку
def create_respond(message):
    print("create_respond")
    print("customer.fio ", customer.fio)
    #if message.text=="На главную":
    if message.text=="Басты бетке":
        send_welcome(message)
    else:        
        try:
            #if (message.text == u'Откликнуться'):
            if (message.text == u'Жауап беру'):
                # Запросить ФИО 
                if (customer.fio is None) or (customer.fio==''):
                    print("0")
                    #message = bot.reply_to(message, """Введите ФИО полностью""")
                    message = bot.reply_to(message, """Толық аты-жөнін енгізіңіз""")
                    bot.register_next_step_handler(message, get_fio)
                else:
                    # Сразу отправить отклик
                    print("1")
                    send_respond(message)
            #elif (message.text == u'На главную'):
            elif (message.text == u'Басты бетке'):
                # В начало
                send_welcome(message)       
        except Exception as error:
            print("create_respond ", error)
            #bot.reply_to(message, str(error))

# Получить фио
def get_fio(message):
    print("get_fio")
    print(message.text)
    fio = message.text
    # Проверка чтобы не было пустым
    if len(fio) > 3:                
        customer.fio = fio
        #print(customer.fio)
        # Запросить дату рождения
        #message = bot.reply_to(message, """Введите дату рождения в формате дд.мм.гггг (например 21.06.1996)""")
        message = bot.reply_to(message, """Туған күніңізді дд.мм.гггг форматында енгізіңіз (мысалы, 21.06.1996)""")
        bot.register_next_step_handler(message, get_birthday) 
    else:
        print('Введите ФИО полностью')
        #bot.send_message(message.chat.id, 'Введите ФИО полностью')
        bot.send_message(message.chat.id, 'Толық аты-жөнін енгізіңіз')
        bot.register_next_step_handler(message, get_fio)    

# Получить дату рождения
def get_birthday(message):
    print("get_birthday")
    #print(message.text)
    # Проверка чтобы только дата
    while True:
        try:
            # дата
            birthday = message.text
            #print(birthday)
            # Проверка это дата?
            datetime.strptime(birthday, '%d.%m.%Y')
            customer.birthday = birthday
            #print(customer.birthday)
            # Запросить образование
            #message = bot.reply_to(message, """Введите сведения об образовании: учебное заведение, год завершения обучения, полученную специальность""")
            message = bot.reply_to(message, """Білімі туралы мәліметтерді енгізіңіз: оқу орны, оқу аяқталған жылы, алған мамандығы""")
            bot.register_next_step_handler(message, get_education)              
        except:
            print('Необходимо ввести именно дату, например 21.06.1996')
            #bot.send_message(message.chat.id, 'Необходимо ввести дату, например 21.06.1996')
            bot.send_message(message.chat.id, 'Күнді енгізу керек, мысалы 21.06.1996')
            bot.register_next_step_handler(message, get_birthday)            
        finally:
            break

# Получить Образование
def get_education(message):
    print("get_education")
    #print(message.text)
    education = message.text
    # Проверка чтобы не было пустым
    if len(education) > 2:                
        customer.education = education
        #print(customer.education)
        # Запросить опыт работы
        #message = bot.reply_to(message, """Введите кратко сведения об опыте работы (в произвольной форме)""")
        message = bot.reply_to(message, """Жұмыс тәжірибесі туралы қысқаша мәлімет енгізіңіз(еркін түрде)""")
        bot.register_next_step_handler(message, get_experience) 
    else:
        print('Если Вы еще учитесь введите учебное заведение, специальность или введите "Нет"')
        #bot.send_message(message.chat.id, 'Если Вы еще учитесь введите учебное заведение, специальность или введите "Нет"')
        bot.send_message(message.chat.id, 'Егер сіз әлі оқып жатсаңыз оқу орнын, мамандықты енгізіңіз немесе "жоқ" деп теріңіз')
        bot.register_next_step_handler(message, get_education)

# Получить опыт работы
def get_experience(message):
    print("get_experience")
    #print(message.text)
    experience = message.text
    # Проверка чтобы не было пустым
    if len(experience) > 2:                
        customer.experience = experience        
        #print(customer.experience)
        # Обновить сведения о пользователе в базе данных
        update_fio(customer.fio, customer.birthday, customer.education, customer.experience)
        # Записать отклик или вернуться в меню
        global DOSSIER_FLAG                
        if (DOSSIER_FLAG==True):
            DOSSIER_FLAG=False
            send_welcome(message)
        else:
            send_respond(message)
    else:
        print('Если у Вас нет опыта работы введите "Нет" или "Без опыта"')
        #bot.send_message(message.chat.id, 'Если у Вас нет опыта работы введите "Нет" или "Без опыта"')
        bot.send_message(message.chat.id, 'Егер сізде жұмыс тәжірибесі болмаса, "жоқ" немесе "тәжірибесіз"деп теріңіз')
        bot.register_next_step_handler(message, get_experience)

# Обновить сведения о пользователе в базе данных
def update_fio(fio, birthday, education, experience):
    print("update_fio")
    birthday = birthday[6:10] + '-' + birthday[3:5] + '-' + birthday[:2]     
    #print(fio)
    #print(birthday)
    #print(education)
    #print(experience)
    try:
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        sql = "UPDATE customer	SET fio='" + fio + "', birthday='" + birthday + "', education='" + education + "', experience='" + experience + "' WHERE id=" + str(customer.id)
        #print(sql)
        cursor.execute(sql)
        conn.commit()      
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
    except Exception as error:
        print(error)
        bot.reply_to(message, 'упс')

# Изменить анкету
def dossier(message):
    print("dossier")
    global DOSSIER_FLAG
    DOSSIER_FLAG=True
    print("DOSSIER_FLAG", DOSSIER_FLAG)    
    #message = bot.reply_to(message, """Введите ФИО полностью""")
    message = bot.reply_to(message, """Толық аты-жөнін енгізіңіз""")
    bot.register_next_step_handler(message, get_fio)

# Записать отклик
def send_respond(message):
    print("send_respond")
    #print(customer.id)
    #print(vacancy_id)
    # Текущая дата, время
    now = datetime.now() 
    try:
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()        
        sql = "INSERT INTO respond(dater, customer_id, vacancy_id) VALUES ('"+ str(now) + "', " + str(customer.id) + ", " + str(vacancy_id) + ")"
        print(sql)
        cursor.execute(sql)
        conn.commit()      
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        # Вывести сообщение        
        #bot.send_message(message.chat.id, "Отклик отправлен")
        bot.send_message(message.chat.id, "Жауап жіберілді")
        send_welcome(message)
    except Exception as error:
        print(error)
        bot.reply_to(message, 'упс')    

# История 
def history(message):
    try:
        # Подключение к PostgreSQL 
        conn = get_connection_string()
        # Вызов функции connect() приводит к созданию объекта-экземпляра от класса Connection.
        # Этот объект обеспечивает связь с файлом базы данных, представляет конкретную БД в программе                     
        cursor = conn.cursor()
        #sql = "SELECT respond.dater, respond.customer_id, customer.telegram_id, customer.phone_number, customer.first_name, customer.last_name, customer.fio, customer.birthday, customer.education, customer.experience, vacancy.id, vacancy.datev, city.title AS city, organization.title AS organization, category.title AS category, vacancy.\"position\", vacancy.details, vacancy.salary, organization_id "
        sql = "SELECT TO_CHAR(respond.dater, 'DD.MM.YYYY HH24:MI') AS DR, customer.phone_number, customer.fio, TO_CHAR(vacancy.datev, 'DD.MM.YYYY HH24:MI') AS DV, city.title AS city, organization.title AS organization, category.title AS category, vacancy.\"position\", vacancy.details, vacancy.salary "
        sql = sql + "FROM respond LEFT JOIN vacancy ON respond.vacancy_id=vacancy.id LEFT JOIN city ON vacancy.city_id=city.id LEFT JOIN category ON vacancy.category_id=category.id LEFT JOIN organization ON vacancy.organization_id=organization.id LEFT JOIN customer ON respond.customer_id=customer.id "
        sql = sql + "WHERE respond.customer_id='" + str(customer.id) + "'"
        sql = sql + " ORDER BY respond.dater"
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            #bot.send_message(message.chat.id,  "<b>Дата отклика:</b> " + str(row[0]) +
            #                 "\n<b>ФИО:</b> " + str(row[2]) +
            #                 "\n<b>Тел.:</b> " + str(row[1]) +
            #                 "\n<b>Дата вакансии:</b> " + str(row[3]) +
            #                 "\n<b>Город:</b> " + str(row[4]) +
            #                 "\n<b>Организация:</b> " + str(row[5]) +
            #                 "\n<b>Категория:</b> " + str(row[6]) +
            #                 "\n<b>Должность:</b> " + str(row[7]) +
            #                 "\n<b>Описание:</b> " + str(row[8]) +
            #                 "\n<b>Зарплата:</b> " + str(row[9]) , parse_mode=telegram.ParseMode.HTML )                            
            bot.send_message(message.chat.id,  "<b>Жауап күні:</b> " + str(row[0]) +
                             "\n<b>ТАӘ:</b> " + str(row[2]) +
                             "\n<b>Тел.:</b> " + str(row[1]) +
                             "\n<b>Жұмыс күні:</b> " + str(row[3]) +
                             "\n<b>Қала:</b> " + str(row[4]) +
                             "\n<b>Ұйымдастыру:</b> " + str(row[5]) +
                             "\n<b>Санат:</b> " + str(row[6]) +
                             "\n<b>Лауазымы:</b> " + str(row[7]) +
                             "\n<b>Сипаттама:</b> " + str(row[8]) +
                             "\n<b>Жалақы:</b> " + str(row[9]) , parse_mode=telegram.ParseMode.HTML )                
        # Закрыть объект cursor после завершения работы.
        cursor.close()
        # Закрыть соединение после завершения работы.
        conn.close()
        send_welcome(message)
    except Exception as error:
        print(error)
        bot.reply_to(message, 'упс')       

bot.polling(none_stop=True, interval=0)
