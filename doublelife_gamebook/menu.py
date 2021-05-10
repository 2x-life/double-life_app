import kivy.uix.screenmanager as kv_screenmanager
import kivy.uix.anchorlayout as kv_anchorlayout
import kivy.uix.label as kv_label
import kivy.uix.button as kv_button
import settings as dl_gb_settings # doublelife_gamebook.settings
import newgame as dl_gb_newgame # doublelife_gamebook.newgame
import utils as dl_gb_utils # doublelife_gamebook.utils

class MenuScreen(kv_screenmanager.Screen):
    initialized = False
    widgets = {}
  
    def on_pre_enter(self):
        if not self.initialized:
            self.initialized = True
            self.widgets["title_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "center", anchor_y = "top")
            self.widgets["title_layout"].add_widget(kv_label.Label(text='Menu', size_hint = (0.1,0.1)))
            self.widgets["settings_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "right", anchor_y = "top")
            self.widgets["settings_layout"].add_widget(kv_button.Button(                   
                background_normal = f'{dl_gb_utils.images_path}/settings.png',
                background_down = f'{dl_gb_utils.images_path}/settings.png',
                border = [1,1,1,1],  
                size_hint = (.12, .08),
                on_press = lambda i: self.goto_settings()))
                
            self.widgets["exit_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "left", anchor_y = "bottom")
            self.widgets["exit_layout"].add_widget(kv_button.Button(
                text = 'Exit',  
                size_hint = (.1, .1),
                on_press = lambda i: exit()))
                
            self.widgets["newgame_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "center", anchor_y = "center")
            self.widgets["newgame_layout"].add_widget(kv_button.Button(
                text = 'New Game',  
                size_hint = (.5, .1),
                on_press = lambda i: self.goto_newgame()))

        for name,widget in self.widgets.items():
            self.add_widget(widget)
        
    def on_leave(self):
        self.clear_widgets()

    def goto_settings(self):
        if not self.manager.has_screen('settings'):
            self.manager.add_widget(dl_gb_settings.SettingsScreen(name='settings'))
        self.manager.current = 'settings'
        
    def goto_newgame(self):
        if not self.manager.has_screen('newgame'):
            self.manager.add_widget(dl_gb_newgame.NewGameScreen(name='newgame'))
        self.manager.current = 'newgame'
    
    def exit(self, instance):
        exit()
