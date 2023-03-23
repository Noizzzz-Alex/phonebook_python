import contacts


class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.contacts_list = []
        self.load_contacts()

    def __str__(self):
        return '\n'.join([str(contact) for contact in self.contacts_list])

    def load_contacts(self):
        with open(self.path, 'r', encoding="UTF-8") as f:
            temp_data = f.readlines()
            for line in temp_data:
                temp_cont = line.strip().split(';')
                self.contacts_list.append(contacts.Contact(*temp_cont))

    # def add_contact(self, name: str, phone: str, comment: str):
    #     self.contacts.append(contacts.Contact(name, phone, comment))
    #     self.save_contacts()
