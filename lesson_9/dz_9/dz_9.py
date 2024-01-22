import json
from pprint import pprint
from uuid import uuid4


def display_student_data(d: dict) -> str:
    """
    Читаємо формує строку для виводна повних данних
    :param d: повні данні через айді гарвця
    :return: згрупованні дані о гравці
    """
    return f" {d['full_name']} played in {d['category']} and he has {d['rating']} power rating"



def viev_index(index_to_view: dict, source_uid_data: dict):
    """
    Функція виводить на екран в читабельному вигляді гравців, розділених по признаку в index_to_view
    тобто або по рейтингу, або по категорії
    :param index_to_view: назва нашого індекса для вводу
    :param source_uid_data: сам індекс, словник списком. Ключи словника - айдішніки ігроків, в яких данні
    :return: Ляпота згрупірованна адекватно
    """
    # перебираємо обьєкт з категоріями, та айдішніками
    for key, values in index_to_view.items():
        # Категорія
        print(f'Displaying {key} players:')
        # і айдішнік ми перетворюємо на повні данні які ми записали в обьєкті(словнику) - uid_index = dict()
        for uid in values:
            print(f'   {display_student_data(source_uid_data[uid])}')

#Откриваємо файл з нашими данними
data = json.load(open("discord_server.json", mode="r"))

category_index = dict()
rating_index = dict()
uid_index = dict()
# Добавляємо деякі данні в нашу базу данних
for players_data in data['players']:
    #Для кожного свій айді
    players_data['uid'] = str(uuid4())
    # Соєдіняємо імя та фамілію
    players_data['full_name'] = f"{players_data['name']} {players_data['surname']}"
    #створюємо словник, у якому ключ це айді ігрока, а значення данні про нього
    uid_index[players_data['uid']] = players_data
    #ЯКЩО ЗНАЧЕННЯ КЛЮЧА ['category'] являється одним із ключів category_index
    if players_data['category'] in category_index:
        #Додаємо уже до існуючої категорії айді гравця у якого є ця категорія
        category_index[players_data['category']].append(players_data['uid'])
    else:
        #Ми створюємо массив з імьям катергорії якої не було, та добавляємо айді гравців, у яких є ця категорія
        category_index[players_data['category']] = list()
        category_index[players_data['category']].append(players_data['uid'])

    # Теж саме але з рейтингом
    if players_data['rating'] in rating_index:
        rating_index[players_data['rating']].append(players_data['uid'])
    else:
        rating_index[players_data['rating']] = list()
        rating_index[players_data['rating']].append(players_data['uid'])
print("Сортування за категоріями")
viev_index(category_index, uid_index)
print('_' * 100)
print("Сортування за Уровнєм гри")
viev_index(rating_index, uid_index)

# сохранити додаткові данні в джсон
json.dump({"players": list(uid_index.values())}, open("discord_server.json", mode="w"), indent=4)