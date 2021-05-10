import kivy.uix.screenmanager as kv_screenmanager
import kivy.uix.anchorlayout as kv_anchorlayout
import kivy.uix.label as kv_label
import kivy.uix.button as kv_button
import utils as dl_gb_utils # doublelife_gamebook.utils

class SettingsScreen(kv_screenmanager.Screen):
    initialized = False
    widgets = {}
    
    def on_pre_enter(self):
        if not self.initialized:
            self.initialized = True
            self.widgets["title_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "center", anchor_y = "top")
            self.widgets["title_layout"].add_widget(kv_label.Label(text='Settings', size_hint = (0.1,0.1)))
            self.widgets["exit_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "left", anchor_y = "bottom")
            self.widgets["exit_layout"].add_widget(kv_button.Button(
                background_normal = f'{dl_gb_utils.images_path}/arrow_left.png',
                background_down = f'{dl_gb_utils.images_path}/arrow_left.png',
                size_hint = (.2, .1),
                border = [1,1,1,1],
                on_press = self.goto_menu))
                
        for name,widget in self.widgets.items():
            self.add_widget(widget)
    
    def on_leave(self):
        self.clear_widgets()
        
    def goto_menu(self, instance):
        self.manager.current = 'menu'
   

