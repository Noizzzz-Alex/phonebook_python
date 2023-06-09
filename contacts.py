class Contact:
    def __init__(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f'{self.name:.<30} | {self.phone:.<30} | {self.comment}'

    def to_string(self):
        return f'{self.name};{self.phone};{self.comment}'

    # def to_string_print(self):
    #     return f'{self.name:.<30} | {self.phone:.<30} | {self.comment}'
