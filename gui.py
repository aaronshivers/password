from guizero import App, Text, CheckBox, PushButton
from settings import Settings
from password import Password


class Gui:
    def __init__(self, password=''):
        # self.settings = Settings()
        self.app = App(title='Password Generator')
        self.title = Text(self.app, text='Password Generator')
        self.password_field = Text(self.app, text=password)
        self.button = PushButton(self.app, command=self.get_password, text='get password')
        self.checkbox_lowers = CheckBox(self.app, text='lowercase')
        self.checkbox_uppers = CheckBox(self.app, text='uppercase')
        self.checkbox_numbers = CheckBox(self.app, text='numbers')
        self.checkbox_specials = CheckBox(self.app, text='special')

        self.checkbox_lowers.value = 1

    def run_gui(self):
        while True:
            self._display_gui()

    def _display_gui(self):
        self.app.display()

    def get_password(self):
        password = Password(20, True, True, True, True).generate_password()
        self.update_password_field(password)

    def update_password_field(self, password):
        self.password_field.value = password
