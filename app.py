from guizero import App
from settings import Settings


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.title = self.settings.title
        self.font = self.settings.font
        self.text_size = self.settings.font_size
        self.bg = self.settings.background_color
