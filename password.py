import string
import random


class Password:
    def __init__(
        self,
        length,
        has_lower_case=True,
        has_upper_case=False,
        has_numbers=False,
        has_special_chars=False
    ):
        self.length = length
        self.has_lower_case = has_lower_case
        self.has_upper_case = has_upper_case
        self.has_numbers = has_numbers
        self.has_special_chars = has_special_chars

    def get_characters(self):
        characters = ''

        if self.has_lower_case:
            characters += string.ascii_lowercase

        if self.has_upper_case:
            characters += string.ascii_uppercase

        if self.has_numbers:
            characters += string.digits

        if self.has_special_chars:
            characters += '!@#$%^&*'

        return characters

    def generate_password(self):
        return ''.join(
            random.choice(self.get_characters())
            for _ in range(self.length)
        )
