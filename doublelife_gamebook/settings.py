from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from utils import images_path

class SettingsScreen(Screen):
    initialized = False
    widgets = {}
    
    def on_pre_enter(self):
        if not self.initialized:
            self.initialized = True
            self.widgets["title_layout"] = AnchorLayout(anchor_x = "center", anchor_y = "top")
            self.widgets["title_layout"].add_widget(Label(text='Settings', size_hint = (0.1,0.1)))
            self.widgets["exit_layout"] = AnchorLayout(anchor_x = "left", anchor_y = "bottom")
            self.widgets["exit_layout"].add_widget(Button(
                background_normal = f'{images_path}/arrow_left.png',
                background_down = f'{images_path}/arrow_left.png',
                size_hint = (.2, .1),
                border = [1,1,1,1],
                on_press = self.goto_menu))
                
        for name,widget in self.widgets.items():
            self.add_widget(widget)
    
    def on_leave(self):
        self.clear_widgets()
        
    def goto_menu(self, instance):
        self.manager.current = 'menu'
   

