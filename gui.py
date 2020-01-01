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
        self.checkbox_box = Box(self.app, border=1)
        self.checkbox_lowers = MyCheckBox(self.checkbox_box, text='lowercase', value=1)
        self.checkbox_uppers = MyCheckBox(self.checkbox_box, text='uppercase')
        self.checkbox_numbers = MyCheckBox(self.checkbox_box, text='numbers')
        self.checkbox_specials = MyCheckBox(self.checkbox_box, text='special')

    def run_gui(self):
        while True:
            self._display_gui()

    def _display_gui(self):
        self.app.display()

    def get_password(self):
        password = Password(
            self.password_length_slider.value,
            self.checkbox_lowers.value,
            self.checkbox_uppers.value,
            self.checkbox_numbers.value,
            self.checkbox_specials.value
        ).generate_password()
        self.update_password_field(password)

    def update_password_field(self, password):
        self.password_field.value = password

