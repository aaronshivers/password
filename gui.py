from guizero import Text, CheckBox, PushButton, Box, Slider
from settings import Settings
from password import Password
from app import MyApp


class Gui:
    def __init__(self, password=''):
        # self.settings = Settings()
        self.app = MyApp()
        self.title = Text(self.app, text='Password Generator')
        self.password_field = Text(self.app, text=password)
        self.button = PushButton(self.app, command=self.get_password, text='get password')
        self.password_length_slider = Slider(self.app)
        self.checkbox_box = Box(self.app, border=1)
        self.checkbox_lowers = CheckBox(self.checkbox_box, text='lowercase')
        self.checkbox_uppers = CheckBox(self.checkbox_box, text='uppercase')
        self.checkbox_numbers = CheckBox(self.checkbox_box, text='numbers')
        self.checkbox_specials = CheckBox(self.checkbox_box, text='special')

        self.checkbox_lowers.value = 1
        # self.checkbox_box.align = 'bottom'
        self.checkbox_box.width = 'fill'

    def run_gui(self):
        while True:
            self._display_gui()

    def _display_gui(self):
        # self.app.font = 'helvetica'
        # self.app.text_size = '20'
        # self.app.bg = '#FFF8F0'
        self.password_field.height = 'fill'
        self.password_field.width = 'fill'
        self.button.bg = '#92140C '
        self.button.text_color = '#FFF8F0'
        self.button.align = 'bottom'
        self.button.width = 'fill'
        self.checkbox_lowers.bg = '#111D4A'
        self.checkbox_lowers.text_color = '#FFF8F0'
        self.checkbox_lowers.width = 'fill'
        self.checkbox_uppers.bg = '#111D4A'
        self.checkbox_uppers.text_color = '#FFF8F0'
        self.checkbox_uppers.width = 'fill'
        self.checkbox_numbers.bg = '#111D4A'
        self.checkbox_numbers.text_color = '#FFF8F0'
        self.checkbox_numbers.width = 'fill'
        self.checkbox_specials.bg = '#111D4A'
        self.checkbox_specials.text_color = '#FFF8F0'
        self.checkbox_specials.width = 'fill'
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

