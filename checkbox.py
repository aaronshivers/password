from guizero import CheckBox


class MyCheckBox(CheckBox):
    def __init__(self, master, text, value=0):
        super().__init__(master)
        self.value = value
        self.width = 'fill'
        self.text = text.capitalize()
        self.bg = '#111D4A'
        self.text_color = '#FFF8F0'
