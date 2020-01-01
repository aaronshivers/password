from guizero import CheckBox
from settings import Settings


class MyCheckBox(CheckBox):
    def __init__(self, master, text, value=0):
        super().__init__(master)
        self.settings = Settings()
        self.value = value
        self.width = 'fill'
        self.text = text.capitalize()
        self.bg = self.settings.button_color
        self.text_color = self.settings.button_text
