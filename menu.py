import book

pb = book.PhoneBook('DB_contacts.txt')

while True:
    print(pb.print_menu())
    chose = input('Выберите пункт меню: ')
    while True:
        if 0 < chose.isdigit() < 7:
            break
        else:
            print('Некорректный ввод')
            chose = input('Выберите пункт меню: ')
    if chose == '1':
        print(pb)
    if chose == '2':
        lookup_value = input('Кого ищем?: ')
        print(book.PhoneBook.search_contact(pb, lookup_value))
    if chose == '3':
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        book.PhoneBook.add_contact(pb, name, phone, comment)
    if chose == '4':
        index = int(input('Введите индекс контакта: '))
        name = input('Введите имя или нажмите Enter чтобы оставить без изменений: ')
        phone = input('Введите номер или нажмите Enter чтобы оставить без изменений: ')
        comment = input('Введите комментарий или нажмите Enter чтобы оставить без изменений: ')
        book.PhoneBook.change_contact(index - 1, name, phone, comment)
    if chose == '5':
        index = int(input('Введите индекс контакта для удаления: '))
        book.PhoneBook.delete_contact(pb, index - 1)
    if chose == '6':
        break
