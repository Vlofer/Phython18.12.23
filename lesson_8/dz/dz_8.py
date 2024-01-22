import os


# function for notes
def add(notes_list):
    """
    Додає в список нотатки
    :param notes_list: список для нотатків
    :return: оновленний список з нотатками
    """
    new_note_input = input("Enter a note: ")
    if new_note_input == '':
        print('пустота не рахується')
    else:
        notes_list.append(new_note_input)


# Function earliest
def earliest(notes_all, num_notes):
    """
    Виводіть список з нотатками спочатку старі потім нові
    :param notes_all: Готовий список з нотатками
    :return: Список з нотатками
    """
    for element in notes_all[:num_notes]:
        print(element)


# Function latest
def latest(notes_reverse_all, num_notes):
    """
    Виводить список з нотатками спочатку нові потім старі
    :param notes_reverse_all:  список з тотатками
    :return: перевернутий список
    """
    for element in reversed(notes_reverse_all[:num_notes]):
        print(element)


# Function longest
def longest(notes_long, num_notes):
    """
    Виводить список з нотатками по довжинні  спочатку самі довгі
    :param notes_long: список з нотатками
    :return: сортирований список
    """
    for element in sorted(notes_long, key=len, reverse=True)[:num_notes]:
        print(element)


# Function shortest
def shortest(notes_shortest, num_notes):
    """
    Виводить список з нотатками по довжинні спочатку самі короткі
    :param notes_shortest: список з нотатками
    :return: сортирований список
    """
    for element in sorted(notes_shortest, key=len, reverse=False)[:num_notes]:
        print(element)


# Function for Save files
def save_notes(num_notes):
    """
    Сохраняє нотатки в файл
    :return:
    """
    with open('notes.txt', mode='a') as fp:
        for item in num_notes:
            fp.writelines(item + '\n')


# Function load
def load_notes(num_notes):
    """
     Загружає сохраньонні нотатки в файлі, в змінну notes
    :return:Нічого
    """
    with open('notes.txt', mode='r') as fp:
        file_notes = fp.readlines()
        for line in file_notes:
            line.split('\n')
            num_notes.append(line)


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
    6. save - сохранити нотатки в файл
    7. load - вигрузить з файла
    8. clear - удалить
    9. Exit
    
''')

# while for comunication with user
while True:
    print('''
Виберіть що ви хочете зробити
    ''')
    user_input = input('Вибір: ')
    # try to int user input
    try:
        user_input = int(user_input)
    except ValueError:
        print('''
        |Введіть ціле число|''')
        continue

    if 0 < user_input < 10:
        # func add
        if user_input == 1:
            add(notes)
        # NUM NOTES
        elif user_input in [2, 3, 4, 5]:
            try:
                num_notes = int(input("Скільки потрібно показати нотатків: "))
                if num_notes < 0:
                    print("Більше 0 введи")
                    continue
            except ValueError:
                print("Числооооо!")
                continue
            # Other
            if user_input == 2:
                earliest(notes, num_notes)
            elif user_input == 3:
                latest(notes, num_notes)
            elif user_input == 4:
                longest(notes, num_notes)
            elif user_input == 5:
                shortest(notes, num_notes)
        elif user_input == 6:
            save_notes(notes)
            print('Нотатки збереженні в файл')
        elif user_input == 7:
            load_notes(notes)
            print('Віруси скачались гии')
        elif user_input == 8:
            os.remove('notes.txt')
            print("всьо пізда")
        elif user_input == 9:
            exit()
    else:
        print('''
        |ЧИСЛО ОТ 1 ДО 9!!!!|
        ''')

