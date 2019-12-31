import string
import random


class Password:
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    special_chars = '!@#$%^&*'

    def __init__(self, length, has_lower_case=True, has_upper_case=False, has_numbers=False, has_special_chars=False):
        self.length = length
        self.has_lower_case = has_lower_case
        self.has_upper_case = has_upper_case
        self.has_numbers = has_numbers
        self.has_special_chars = has_special_chars

    def get_characters(self):
        characters = ''

        if self.has_lower_case:
            characters += Password.lower_case

        if self.has_upper_case:
            characters += Password.upper_case

        if self.has_numbers:
            characters += Password.numbers

        if self.has_special_chars:
            characters += Password.special_chars

        return characters

    def generate_password(self):
        return ''.join(random.choice(self.get_characters()) for _ in range(self.length))
