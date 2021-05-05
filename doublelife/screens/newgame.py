from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from doublelife.screens.story import StoryScreen
from doublelife.utils import images_path

class NewGameScreen(Screen):
    initialized = False
    widgets = {}
    
    def on_pre_enter(self):
        if not self.initialized:
            self.initialized = True
            self.widgets["title_layout"] = AnchorLayout(anchor_x = "center", anchor_y = "top")
            self.widgets["title_layout"].add_widget(Label(text='New Game', size_hint = (0.1,0.1)))
            
            self.widgets["exit_layout"] = AnchorLayout(anchor_x = "left", anchor_y = "bottom")
            self.widgets["exit_layout"].add_widget(Button(
                background_normal = f'{images_path}/arrow_left.png',
                background_down = f'{images_path}/arrow_left.png',
                size_hint = (.2, .1),
                border = [1,1,1,1],
                on_press = lambda i: self.goto_menu()))
                
            self.widgets["stories_layout"] = AnchorLayout(anchor_x = "center", anchor_y = "center")
            self.widgets["stories_layout"].add_widget(BoxLayout(orientation='vertical', size_hint = (0.5, 0.7)))
            self.widgets["stories_layout"].children[0].add_widget(Button(
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
            self.manager.add_widget(StoryScreen(name=story.get_title()))
            self.manager.get_screen(story.get_title()).story = story
        self.manager.current = story.get_title()
   

