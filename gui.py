from guizero import Text, Box, Slider
from password import Password
from app import MyApp
from checkbox import MyCheckBox
from button import MyButton


class Gui:
    def __init__(self, password=''):
        self.app = MyApp()
        self.title = Text(self.app, text='Password Generator')
        self.password_field = Text(self.app, text=password, height='fill', width='fill')
        self.button = MyButton(self.app, command=self.get_password)
        self.password_length_slider = Slider(self.app)
        self.checkbox_container = Box(self.app, border=1)
        self.has_lowers_checkbox = MyCheckBox(self.checkbox_container, text='lowercase', value=1)
        self.has_uppers_checkbox = MyCheckBox(self.checkbox_container, text='uppercase')
        self.has_numbers_checkbox = MyCheckBox(self.checkbox_container, text='numbers')
        self.has_specials_checkbox = MyCheckBox(self.checkbox_container, text='special')

    def display_gui(self):
        self.app.display()

    def get_password(self):
        password = Password(
            self.password_length_slider.value,
            self.has_lowers_checkbox.value,
            self.has_uppers_checkbox.value,
            self.has_numbers_checkbox.value,
            self.has_specials_checkbox.value
        ).generate_password()
        self.update_password_field(password)

    def update_password_field(self, password):
        self.password_field.value = password

