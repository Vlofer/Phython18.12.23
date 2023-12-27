# function for notes
def add(notes_list):
    """
    Додає в список нотатки
    :param notes_list: список для нотатків
    :return: оновленний список з нотатками
    """
    new_note_input = input("Enter a note: ")
    notes_list.append(new_note_input)


def earliest(notes_all):
    """
    Виводіть список з нотатками спочатку старі потім нові
    :param notes_all: Готовий список з нотатками
    :return: Список з нотатками
    """
    for element in notes_all:
        print(element)


def latest (notes_reverse_all):
    """
    Виводить список з нотатками спочатку нові потім старі
    :param notes_reverse_all:  список з тотатками
    :return: перевернутий список
    """
    for element in reversed(notes_reverse_all):
        print(element)


def longest(notes_long):
    """
    Виводить список з нотатками по довжинні  спочатку самі довгі
    :param notes_long: список з нотатками
    :return: сортирований список
    """
    for element in sorted(notes_long, key=len, reverse=True):
        print(element)


def shortest(notes_shortest):
    """
    Виводить список з нотатками по довжинні спочатку самі короткі
    :param notes_shortest: список з нотатками
    :return: сортирований список
    """
    for element in sorted(notes_shortest, key=len, reverse=False):
        print(element)


# array with notes
notes = list()

# instruction
print('''
    Інструкція:
    1. add - Додати нотатку
    2. earliest - Вивести нотатки  Нові - Старі
    3. latest -  Вивести нотатки Старі - Нові
    4. longest - Вивести нотатки по довжині Довгі - Короткі
    5. shortest - Вивести нотатки по довжині Короткі - Довгі
    6. Exit
''')

# while for comunication with user
while True:
    print('''
Виберіть що ви хочете зробити
    ''')
    user_input = input('Вибір: ')
    try:
        user_input = int(user_input)
    except ValueError:
        print('''
        |Введіть ціле число|''')
        continue
    if 0 < user_input < 7:
        if user_input == 1:
            add(notes)
        elif user_input == 2:
            earliest(notes)
        elif user_input == 3:
            latest(notes)
        elif user_input == 4:
            longest(notes)
        elif user_input == 5:
            shortest(notes)
        elif user_input == 6:
            exit()
    else:
        print('''
        |ЧИСЛО ОТ 1 ДО 6!!|
        ''')