
def start(function):
    return function
def menu(choise):
    while True:
        print('''
        Главное меню:
        1. Открыть файл телефоннной книги
        2. Сохранить файл телефоннной книги
        3. Показать все контакты
        4. Добавить контакт
        5. Добавить контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход''')
        choise =int(input('Введите номер пункта меню: '))
        if choise == 1:
            if phone_book == []:
                print('Телефонная книга пуста')
        if choise == 2:
            pass
        if choise == 3:
            pass
        if choise == 4:
            pass
        if choise == 5:
            pass
        if choise == 6:
            pass
        if choise == 7:
            pass
        if choise == 8:
            print('Всего доброго')
            break

#def open_file():
    #with open_file('phonebook.txt')
phone_book = []
start(menu(' '))