db_phonebook = 'phonebook.txt'
phone_book = []
phone_dict = {}


def open_file():
    with open(db_phonebook, 'r', encoding='UTF -8') as file:
        temp_list = file.readlines()
        i = 0
        for line in temp_list:
            temp_contact = line.strip().split(';')
            phone_dict = {'name': temp_contact[0],
                          'phone_number': temp_contact[1],
                          'comment': temp_contact[2]}
            phone_book.append(phone_dict)
            i += 1
            print(f'{i}. {temp_contact[0]:.<30}{temp_contact[1]:.<30}:{temp_contact[2]}')


def input_contact():
    dict_temp = {'name': input('Введите ФИО: '), 'phone_number': int(input('Введите номер телефона: ')),
                 'comment': input('Введите комментарий: ')}
    phone_book.append(dict_temp)


def save_file():
    with open(db_phonebook, 'w', encoding='UTF -8') as file:
        for contact in phone_book:
            file.write(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}\n')


def find_contact():
    temp_list = []
    find_name = input('Введите искомое: ')
    for contact in phone_book:
        for _ in contact.values():
            if find_name in _:
                temp_list.append(contact)
                # print(f'{contact["name"]};{contact["phone_number"]};{contact["comment"]}')
                print(
                    f'{contact["name"]:.<30}{contact["phone_number"]:.<30}:{contact["comment"]}')


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
