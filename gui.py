from guizero import Text, Box, Slider, TextBox
from password import Password
from app import MyApp
from checkbox import MyCheckBox
from button import MyButton
from settings import Settings


class Gui:
    def __init__(self, password=''):
        self.app = MyApp()
        self.settings = Settings()
        self.title = Text(self.app, text='Password Generator')
        self.password_field = TextBox(self.app, text=password, height=4, width='fill', multiline=True)
        self.input_container = Box(self.app, border=1, align='bottom')
        self.password_length_slider = Slider(self.input_container, width='fill')
        self.button = MyButton(self.input_container, command=self.get_password)
        self.has_lowers_checkbox = MyCheckBox(self.input_container, text='lowercase', value=1)
        self.has_uppers_checkbox = MyCheckBox(self.input_container, text='uppercase')
        self.has_numbers_checkbox = MyCheckBox(self.input_container, text='numbers')
        self.has_specials_checkbox = MyCheckBox(self.input_container, text='special')

        self.password_length_slider.bg = self.settings.secondary
        self.password_length_slider.text_color = self.settings.button_text
        self.input_container.width = 'fill'

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

