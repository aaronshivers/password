from guizero import PushButton


class MyButton(PushButton):
    def __init__(self, master, command):
        super().__init__(master, command)
        self.text = 'get password'
        self.bg = '#92140C '
        self.text_color = '#FFF8F0'
        self.align = 'bottom'
        self.width = 'fill'
