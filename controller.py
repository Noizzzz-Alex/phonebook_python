import model
import view


def start():
    print(view.menu)
    global phone_dict
    while True:
        chose = int(input('Выберите пункт меню: '))
        if chose == 1:
            print('_' * 120)
            model.open_file()
            print('_' * 120)
            if model.phone_dict == []:
                print('_' * 120)
                print('Контактов нет')
                print('_' * 120)

        if chose == 2:
            model.find_contact()
            #     print('_' * 120)
            #     print('Контакт найден')
            #     print('_' * 120)
            # else:
            #     print('_' * 120)
            #     print('Контакт не найден')
            #     print('_' * 120)
        if chose == 3:
            model.input_contact()
            print('_' * 120)
            print('Контакт добавлен')
            print('_' * 120)

        if chose == 4:
            model.edit_contact()
            print('_' * 120)
            print('Контакт изменен')
            print('_' * 120)

        if chose == 5:
            model.save_file()
            print('_' * 120)
            print('Контакты сохранены')
            print('_' * 120)

        if chose == 6:
            model.delete_contact()
            print('_' * 120)
            print('Контакт удален')
            print('_' * 120)

        if chose == 7:
            print('_' * 120)
            print('До свидания')
            print('_' * 120)
            break
