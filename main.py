db_phonebook = 'phonebook.txt'
phone_book = []
phone_dict = {}


def start(function):
    return function


def menu(choise):
    while True:
        print('''
Главное меню:
1. Показать все контакты
2. Найти контакт
3. Добавить контакт
4. Изменить контакт
5. Сохранить в файл
6. Удалить контакт
7. Выход''')

        choise = int(input('Введите номер пункта меню: '))
        if choise == 1:
            print('_' * 120)
            open_file()
            print('_' * 120)
            if phone_dict == []:
                print('_' * 120)
                print('Контактов нет')
                print('_' * 120)

        if choise == 2:
            find_contact()
            print('_' * 120)
            print('Контакт найден')
            print('_' * 120)


        if choise == 3:
            input_contact()
            print('_' * 120)
            print('Контакт добавлен')
            print('_' * 120)

        if choise == 4:
            edit_contact()
            print('_' * 120)
            print('Контакт изменен')
            print('_' * 120)

        if choise == 5:
            save_file()
            print('_' * 120)
            print('Контакты сохранены')
            print('_' * 120)

        if choise == 6:
            delete_contact()
            print('_' * 120)
            print('Контакт удален')
            print('_' * 120)

        if choise == 7:
            print('_' * 120)
            print('До свидания')
            print('_' * 120)
            break


def open_file():
    with open(db_phonebook, 'r', encoding='UTF -8') as file:
        temp_list = file.readlines()
        i = 0
        for line in temp_list:
            temp_contact = line.strip().split(';')
            # print(temp_contact)
            temp_dict = {'name': temp_contact[0],
                         'phone_number': temp_contact[1],
                         'comment': temp_contact[2]}
            phone_book.append(temp_dict)
            i += 1
            print(f'{i}. {temp_contact[0]:.<30}{temp_contact[1]:.<30}:{temp_contact[2]}')


def input_contact():
    dict_temp = {}
    dict_temp['name'] = input('Введите ФИО: ')
    dict_temp['phone_number'] = int(input('Введите номер телефона: '))
    dict_temp['comment'] = input('Введите комментарий: ')
    phone_book.append(dict_temp)
    # print(phone_book)


def save_file():
    with open(db_phonebook, 'w', encoding='UTF -8') as file:
        for contact in phone_book:
            file.write(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}\n')


def find_contact():
    find_name = input('Введите ФИО: ')
    for contact in phone_book:
        if contact['name'] == find_name:
            print(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}')
        else:
            print('Контакт не найден')


def delete_contact():
    find_name = input('Введите ФИО: ')
    for contact in phone_book:
        if contact['name'] == find_name:
            phone_book.remove(contact)
            print(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}')
        else:
            print('Контакт не найден')


def edit_contact():
    find_name = input('Введите ФИО: ')
    for contact in phone_book:
        if contact['name'] == find_name:
            print(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}')
            contact['name'] = input('Введите ФИО: ')
            contact['phone_number'] = int(input('Введите номер телефона: '))
            contact['comment'] = input('Введите комментарий: ')
            print(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}')
            return contact
        else:
            print('Контакт не найден')


start(menu('MENU'))
