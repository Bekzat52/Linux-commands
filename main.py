"============ CRUD =============="
# create
# read
# update
# delete
from utils import validate_id

database = {
    "Бекзат": "скала",
    "Эртай": "пароль",
    "Оомат": "Кыргызстан",
    "Имран": "12345",
    "Жийде": "return",
    "Манас": "Маке",
    "Арафат": "54321",
    "Элжаз": "парол",
    "Гулсана": "312",
    "Эркайым": "Айдин",
    "Бекназ": "Арёль",
    "Эдиль": "ьлорап",
    "Айгул": "май",
    "Закир": "@@@",
    "Бегайым": "makers",
    "Мырзайым": "Bootcamp2221",
    "Даниэл": "covid19",
    "Жибек": "1404",
    "Калысбек": "стол",
    "Ырыс": "suuuuuuuuiiiiiiiiiiii",
    "Айканыш": "qwerty",
    "Арген": "11172332",
    "Нурмухамед": "Не верный",
    "Бектур": "0101",
    "Алан": "душу питона",
    "Жаангер": "ох блин",
    "Богдан": "Кудайберген",
    "Айгерим": "синий маркер",
    "Настя": "Python21"
}
import random
ids = []
for key, value in database.copy().items():
    id = random.randint(100,999)
    while id in ids:
        id = random.randint(100, 999)
    ids.append(id)
    database[id] = {
        'name': key,
        'password': value,
        'info': '...'
    }
    del database[key]

print(database)

data_base={
"296": {"name": "Бекзат", "password": "скала", "info": "..."}, 
"134": {"name": "Эртай", "password": "пароль", "info": "..."}, 
"987": {"name": "Оомат", "password": "Кыргызстан", "info": "..."}, 
"273": {"name": "Имран", "password": "12345", "info": "..."}, 
"596": {"name": "Жийде", "password": "return", "info": "..."}, 
"514": {"name": "Манас", "password": "Маке", "info": "..."}, 
"912": {"name": "Арафат", "password": "54321", "info": "..."}, 
"801": {"name": "Элжаз", "password": "парол", "info": "..."}, 
"518": {"name": "Гулсана", "password": "312", "info": "..."}, 
"366": {"name": "Эркайым", "password": "Айдин", "info": "..."}, 
"861": {"name": "Бекназ", "password": "Арёль", "info": "..."}, 
"599": {"name": "Эдиль", "password": "ьлорап", "info": "..."}, 
"567": {"name": "Айгул", "password": "май", "info": "..."}, 
"394": {"name": "Закир", "password": "@@@", "info": "..."}, 
"672": {"name": "Бегайым", "password": "makers", "info": "..."}, 
"182": {"name": "Мырзайым", "password": "Bootcamp2221", "info": "..."}, 
"770": {"name": "Даниэл", "password": "covid19", "info": "..."}, 
"420": {"name": "Жибек", "password": "1404", "info": "..."}, 
"556": {"name": "Калысбек", "password": "стол", "info": "..."}, 
"570": {"name": "Ырыс", "password": "suuuuuuuuiiiiiiiiiiii", "info": "..."}, 
"954": {"name": "Айканыш", "password": "qwerty", "info": "..."}, 
"149": {"name": "Арген", "password": "11172332", "info": "..."}, 
"267": {"name": "Нурмухамед", "password": "Не верный", "info": "..."}, 
"209": {"name": "Бектур", "password": "0101", "info": "..."}, 
"731": {"name": "Алан", "password": "душу питона", "info": "..."}, 
"718": {"name": "Куба", "password": "1", "info": "..."}, 
"653": {"name": "Жаангер", "password": "ох блин", "info": "..."}, 
"405": {"name": "Богдан", "password": "Кудайберген", "info": "..."}, 
"698": {"name": "Айгерим", "password": "синий маркер", "info": "..."}, 
"744": {"name": "Настя", "password": "Python21", "info": "..."}, 
"689": {"name": "Жаркынай", "password": "Мафия", "info": "..."}}

def read(u_id):
    """Принимает id юзера, выводит его имя и информацию.
    Если такого юзера нет вызывается Exception  """
    validate_id(data_base.keys(), u_id)
    name = data_base[u_id]["name"]
    info = data_base[u_id]['info']
    print(f"""
============= {u_id} ============
Name: {name}
Info: {info}    
=================================
    """)
read(134)

def delete(u_id):
    "Принимает id  пользоватеоя если юзер существуется .то он удаляется из бд если юзера нет вызывается ошибка"
    validate_id(data_base.keys(), u_id)
    del data_base[u_id]
delete()


def update(u_id):
    """
    Принимает id юзера 
    Выводит старые данные
    Принимает новые данные
    Изменяет в базе данных
    """
    validate_id(data_base.keys(), u_id)
    read(u_id)
    name = 