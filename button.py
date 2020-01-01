from guizero import PushButton
from settings import Settings


class MyButton(PushButton):
    def __init__(self, master, command):
        super().__init__(master, command)
        self.settings = Settings()
        self.text = 'get password'.capitalize()
        self.bg = self.settings.button_color
        self.text_color = self.settings.button_text
        self.align = 'bottom'
        self.width = 'fill'
