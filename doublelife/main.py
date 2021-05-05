__version__ = "0.1.0"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from doublelife.menu import MenuScreen

class MainApp(App):

    def build(self):
        Config.set('graphics', 'width', '450')
        Config.set('graphics', 'height', '800')
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        return sm

def main():
    MainApp().run()

if __name__ == '__main__':
    main()

