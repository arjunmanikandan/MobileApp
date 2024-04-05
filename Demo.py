from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
import speech_recognition as sr
from kivy.core.window import Window
from record import main
from transcribe import voice_text
from summary import summarize
import json

screen_helper = """
ScreenManager:
    ProfileScreen:
    MenuScreen:

<ProfileScreen>:
    Screen:
        Image:
            source: "RT image.jfif"
            size_hint: None, None
            width: "360dp"
            height: "640dp"
            pos_hint: {'center_x':.5, 'center_y':.2}
        MDLabel:
            text: 'WELCOME'
            font_name: 'Georgia'
            font_size: "48dp"
            halign: "center"
            color: "#ffcc00"
            pos_hint: {'center_y':.8}
        MDTextField:
            hint_text: "Username"
            icon_right: 'account'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {'center_x':.5, 'center_y':.65}
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        MDTextField:
            id: psswd
            hint_text: "Password"
            password: True
            icon_right: 'eye-off'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {'center_x':.5, 'center_y':.5}
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        BoxLayout:
            size_hint: .85, None
            height: "30dp"
            pos_hint: {'center_x':.5, 'center_y':.4}
            spacing: "5dp"
            MDCheckbox:
                id: cb
                size_hint: None, None
                width: "30dp"
                height: "30dp"
                pos_hint: {'center_x':.5, 'center_y':.5}
                on_press:
                    psswd.password = False if psswd.password == True else True
            MDLabel:
                text: "[ref=Show Password]Show Password[/ref]"
                markup: True
                pos_hint: {'center_x':.5, 'center_y':.5}
                on_ref_press:
                    cb.active = False if cb.active == True else True
                    psswd.password = False if psswd.password == True else True
            BoxLayout:
                size_hint: .6, None
                height: "30dp"
                pos_hint: {'center_x':.5, 'center_y':.3}
                spacing: "5dp"
            MDRectangleFlatButton:
                text: 'Login'
                pos_hint: {'center_x':.5, 'center_y':.3}
                on_press: root.manager.current = 'menu'
<MenuScreen>:
    name: 'menu'
    RelativeLayout:
        orientation: 'vertical'
        pos: self.pos
    Label:
        text: 'Speech to Text'
        pos_hint: {'center_x':0.5, 'center_y':0.905}
        font_size: (self.height/15)* 0.7
    Button:
        text:'Record'
        size_hint: 0.3,0.1
        pos_hint:{'center_x': 0.47, 'center_y': 0.705}
        on_press: root.record()
    Button:
        text:'Summarizer'
        size_hint: 0.3,0.1
        pos_hint:{'center_x': 0.47, 'center_y': 0.589}
        on_press: root.summarizer()
    TextInput:
        id: totext
        pos_hint:{'center_x': 0.47, 'center_y': 0.305}
        size_hint: 0.8,0.4
        font_size:"10dp"
        readonly:True
"""

class ProfileScreen(Screen):
    pass

class MenuScreen(Screen):
    def record(self):
        main()
        voice_text()
        summarize()

    def summarizer(self):
        str1 = """"""
        with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\summary.json","r") as file:
            result = json.load(file)
        str1=""
        for item in result:
            item = str(item).replace("{"," ").replace("}"," ").replace("'"," ")
            str1+=item+"\n"
        self.ids.totext.text = str1 
        
class RecorderApp(MDApp):  # Inherit from MDApp
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen

if __name__ == '__main__':
    Window.size = (360, 640)
    RecorderApp().run()
