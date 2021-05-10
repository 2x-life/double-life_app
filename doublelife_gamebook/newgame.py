import kivy.uix.screenmanager as kv_screenmanager
import kivy.uix.anchorlayout as kv_anchorlayout
import kivy.uix.boxlayout as kv_boxlayout
import kivy.uix.label as kv_label
import kivy.uix.button as kv_button
import story as dl_gb_story # doublelife_gamebook.story
import utils as dl_gb_utils # doublelife_gamebook.utils

class NewGameScreen(kv_screenmanager.Screen):
    initialized = False
    widgets = {}
    
    def on_pre_enter(self):
        if not self.initialized:
            self.initialized = True
            self.widgets["title_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "center", anchor_y = "top")
            self.widgets["title_layout"].add_widget(kv_label.Label(text='New Game', size_hint = (0.1,0.1)))
            
            self.widgets["exit_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "left", anchor_y = "bottom")
            self.widgets["exit_layout"].add_widget(kv_button.Button(
                background_normal = f'{dl_gb_utils.images_path}/arrow_left.png',
                background_down = f'{dl_gb_utils.images_path}/arrow_left.png',
                size_hint = (.2, .1),
                border = [1,1,1,1],
                on_press = lambda i: self.goto_menu()))
                
            self.widgets["stories_layout"] = kv_anchorlayout.AnchorLayout(anchor_x = "center", anchor_y = "center")
            self.widgets["stories_layout"].add_widget(kv_boxlayout.BoxLayout(orientation='vertical', size_hint = (0.5, 0.7)))
            self.widgets["stories_layout"].children[0].add_widget(kv_button.Button(
                text = "Undefined Title",
                # ~ on_press = lambda i: self.goto_story(story1.s1)))
                on_press = lambda i: print("Story not defined")))
                
        for name,widget in self.widgets.items():
            self.add_widget(widget)
    
    def on_leave(self):
        self.clear_widgets()
        
    def goto_menu(self):
        self.manager.current = "menu"
        
    def goto_story(self, story):
        if not self.manager.has_screen(story.get_title()):
            self.manager.add_widget(dl_gb_story.StoryScreen(name=story.get_title()))
            self.manager.get_screen(story.get_title()).story = story
        self.manager.current = story.get_title()
   

