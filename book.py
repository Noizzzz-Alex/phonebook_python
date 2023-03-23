import contacts


class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.contacts_list = []
        self.load_contacts()

    def __str__(self):
        result = ''
        i = 0
        for contact in self.contacts_list:
            i += 1
            result += f'{i:<5}{contact.__str__()} \n'
        return result
        # return '\n'.join([contact.to_string() for contact in self.contacts_list])

    def load_contacts(self):
        with open(self.path, 'r', encoding="UTF-8") as f:
            temp_data = f.readlines()
            for line in temp_data:
                temp_cont = line.strip().split(';')
                self.contacts_list.append(contacts.Contact(*temp_cont))

    def save(self):
        temp_data = '\n'.join([contact.to_string() for contact in self.contacts_list])
        with open(self.path, 'w', encoding="UTF-8") as f:
            f.write(temp_data)

    def add_contact(self, name, phone, comment):
        self.contacts_list.append(contacts.Contact(name, phone, comment))
        self.save()

    def search_contact(self, lookup_value):
        temp_dict = []
        for contact in self.contacts_list:
            if lookup_value in contact.to_string():
                temp_dict.append(f'{contact.__str__()}')
        return '\n'.join(temp_dict)

    def delete_contact(self, index: int):
        self.contacts_list.pop(index)
        self.save()

    def change_contact(self, index: int, name: str, phone: str, comment: str):
        name = name if name != '' else self.contacts_list[index].name
        phone = phone if phone != '' else self.contacts_list[index].phone
        comment = comment if comment != '' else self.contacts_list[index].comment
        self.contacts_list[index] = contacts.Contact(name, phone, comment)
        self.save()

    def print_menu(self):
        return f'1. Все контакты\n' \
               f'2. Поиск контакта\n' \
               f'3. Добавить контакт\n' \
               f'4. Изменить контакт\n' \
               f'5. Удалить контакт\n' \
               f'6. Выход\n'
