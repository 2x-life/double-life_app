__version__ = "0.1.0"

import kivy.app as kv_app
import kivy.uix.screenmanager as kv_screenmanager
import kivy.config as kv_config
import menu


class MainApp(kv_app.App):

    def build(self):
        kv_config.Config.set('graphics', 'width', '450')
        kv_config.Config.set('graphics', 'height', '800')
        sm = kv_screenmanager.ScreenManager()
        sm.add_widget(menu.MenuScreen(name='menu'))
        return sm

def main():
    MainApp().run()

if __name__ == '__main__':
    main()

