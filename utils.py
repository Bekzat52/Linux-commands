" Файл с дополнительными функциями"
from dataclasses import dataclass
from typing_extensions import dataclass_transform
from utils import validate_id


data_base={
296: {'name': 'Бекзат', 'password': 'скала', 'info': '...'}, 
134: {'name': 'Эртай', 'password': 'пароль', 'info': '...'}, 
987: {'name': 'Оомат', 'password': 'Кыргызстан', 'info': '...'}, 
273: {'name': 'Имран', 'password': '12345', 'info': '...'}, 
596: {'name': 'Жийде', 'password': 'return', 'info': '...'}, 
514: {'name': 'Манас', 'password': 'Маке', 'info': '...'}, 
912: {'name': 'Арафат', 'password': '54321', 'info': '...'}, 
801: {'name': 'Элжаз', 'password': 'парол', 'info': '...'}, 
518: {'name': 'Гулсана', 'password': '312', 'info': '...'}, 
366: {'name': 'Эркайым', 'password': 'Айдин', 'info': '...'}, 
861: {'name': 'Бекназ', 'password': 'Арёль', 'info': '...'}, 
599: {'name': 'Эдиль', 'password': 'ьлорап', 'info': '...'}, 
567: {'name': 'Айгул', 'password': 'май', 'info': '...'}, 
394: {'name': 'Закир', 'password': '@@@', 'info': '...'}, 
672: {'name': 'Бегайым', 'password': 'makers', 'info': '...'}, 
182: {'name': 'Мырзайым', 'password': 'Bootcamp2221', 'info': '...'}, 
770: {'name': 'Даниэл', 'password': 'covid19', 'info': '...'}, 
420: {'name': 'Жибек', 'password': '1404', 'info': '...'}, 
556: {'name': 'Калысбек', 'password': 'стол', 'info': '...'}, 
570: {'name': 'Ырыс', 'password': 'suuuuuuuuiiiiiiiiiiii', 'info': '...'}, 
954: {'name': 'Айканыш', 'password': 'qwerty', 'info': '...'}, 
149: {'name': 'Арген', 'password': '11172332', 'info': '...'}, 
267: {'name': 'Нурмухамед', 'password': 'Не верный', 'info': '...'}, 
209: {'name': 'Бектур', 'password': '0101', 'info': '...'}, 
731: {'name': 'Алан', 'password': 'душу питона', 'info': '...'}, 
718: {'name': 'Куба', 'password': '1', 'info': '...'}, 
653: {'name': 'Жаангер', 'password': 'ох блин', 'info': '...'}, 
405: {'name': 'Богдан', 'password': 'Кудайберген', 'info': '...'}, 
698: {'name': 'Айгерим', 'password': 'синий маркер', 'info': '...'}, 
744: {'name': 'Настя', 'password': 'Python21', 'info': '...'}, 
689: {'name': 'Жаркынай', 'password': 'Мафия', 'info': '...'}}

def generate_id(ids):
    """ Принимает список существующих id.
    Возвращает новое id в дипазоне от 100 до 1000
    """
    import random
    id_ = random.randint(100,999)
    while id_ in ids:
        id_ = random.randint(100, 999)
    return id_ 


def validate_password(p1, p2) :
    """
    Принимает 2 пароля если они не совпадают вызывается ошибка
    """

    if p1 != p2:
        raise Exception("Пароли не совпадают")



def create():
    from utils import generate_id, validate_password
    name = input('Введите имя:')
    password = input('Введите пароль:')
    password2 = input('Введите подтверждение пароля:')
    validate_password(password, password2)
    info = input('Введите информацию о вас ')
    id_ = generate_id(data_base.keys())
    data_base[id_] = {
        'name' : name,
        'password' : password,
        'info' : info
    }
print ('Вы были успешно добавлены в python21')

def read(u_id):
    """Принимает id юзера, выводит его имя и информацию.
    Если такого юзера нет вызывается Exception  """
    if u_id not in data_base:
        raise Exception('Такого юзера нет')
    name = data_base[u_id]['name']
    info = data_base[u_id]['info']
    print(f"""
============= {u_id} ============
Name: {name}
Info: {info}    
=================================
    """)
read(134)

create()
from pprint import pprint
pprint(data_base)


def read_db(name):
    import json


"""Файл с дополнительными функциями"""


def generate_id(ids):
    """
    Принимает список существующих id
    Возвращает новое id в диапазоне от 100 до 1000
    """
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids:
        id_ = random.randint(100, 1000)
    return str(id_)

def validate_passwords(p1, p2):
    """
    Принимает 2 пароля
    Если они не совпадают, вызывается ошибка
    """
    if p1 != p2:
        raise Exception("Пароли не совпадают")

def validate_id(ids, u_id):
    """
    Принимает список существующих id и id, которое нужно проверить
    Если такого id нет в списке, вызывается Exception
    """
    if u_id not in ids:
        raise Exception("Такого юзера нет")


def read_db(name):
    """
    Принимает название файла
    Возвращает данные из бд в виде python обьектов
    """
    import json
    with open(name, "r") as file:
        db = json.load(file)
    return db

def write_to_db(name, data):
    """
    Принимает название файла и данные для записи
    Записывает эти данные в файл
    """
    import json
    with open(name, "w", encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False)