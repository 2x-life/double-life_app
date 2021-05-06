from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from settings import SettingsScreen
from newgame import NewGameScreen
from utils import images_path

class MenuScreen(Screen):
    initialized = False
    widgets = {}
  
    def on_pre_enter(self):
        if not self.initialized:
            self.initialized = True
            self.widgets["title_layout"] = AnchorLayout(anchor_x = "center", anchor_y = "top")
            self.widgets["title_layout"].add_widget(Label(text='Menu', size_hint = (0.1,0.1)))
            self.widgets["settings_layout"] = AnchorLayout(anchor_x = "right", anchor_y = "top")
            self.widgets["settings_layout"].add_widget(Button(                   
                background_normal = f'{images_path}/settings.png',
                background_down = f'{images_path}/settings.png',
                border = [1,1,1,1],  
                size_hint = (.12, .08),
                on_press = lambda i: self.goto_settings()))
                
            self.widgets["exit_layout"] = AnchorLayout(anchor_x = "left", anchor_y = "bottom")
            self.widgets["exit_layout"].add_widget(Button(
                text = 'Exit',  
                size_hint = (.1, .1),
                on_press = lambda i: exit()))
                
            self.widgets["newgame_layout"] = AnchorLayout(anchor_x = "center", anchor_y = "center")
            self.widgets["newgame_layout"].add_widget(Button(
                text = 'New Game',  
                size_hint = (.5, .1),
                on_press = lambda i: self.goto_newgame()))

        for name,widget in self.widgets.items():
            self.add_widget(widget)
        
    def on_leave(self):
        self.clear_widgets()

    def goto_settings(self):
        if not self.manager.has_screen('settings'):
            self.manager.add_widget(SettingsScreen(name='settings'))
        self.manager.current = 'settings'
        
    def goto_newgame(self):
        if not self.manager.has_screen('newgame'):
            self.manager.add_widget(NewGameScreen(name='newgame'))
        self.manager.current = 'newgame'
    
    def exit(self, instance):
        exit()
