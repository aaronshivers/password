from guizero import App


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.title = 'Password Generator'
        self.font = 'helvetica'
        self.text_size = '20'
        self.bg = '#FFF8F0'
