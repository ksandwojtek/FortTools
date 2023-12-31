import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

kivy.require('2.2.1')
Config.set('kivy', 'text_font', ['fortnite'])


class FortTools(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.4, 0.3)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # self.window.add_widget(Image(source="icon.png"))
        return self.window


if __name__ == "__main__":
    FortTools().run()
