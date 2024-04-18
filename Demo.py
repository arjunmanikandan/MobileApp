from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from record import main
from transcribe import voice_text
from summary import summarize
import json
import datetime

screen_helper = """
ScreenManager:
    MDScreen:
    ProfileScreen:
    MenuScreen:
    SummarizerScreen:

<MDScreen>
    name: 'mdscreen'
    Screen:
        canvas.before:
            Color:
                rgba: (1, 1, 1, 1)
            Rectangle:
                source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\RT_background.png"
                size: root.width, root.height
                pos: self.pos
                            
    MDFloatLayout:
        Image:
            source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\RT_logo.png"
            size_hint: .8, .8
            pos_hint: {'center_x': .5, 'center_y':.55}
        MDIconButton:
            icon: "chevron-right"
            theme_icon_color: "Custom"
            icon_color: 211/255, 230/255, 61/255, 1
            pos_hint: {'center_x': .7, 'center_y':.1}
            on_press: root.manager.current = 'profile'
        MDLabel:
            text: 'Click Here'
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBoldItalic.ttf'
            theme_text_color: "Custom"
            text_color: 1,1,1,1 
            font_size: "18sp" 
            pos_hint: {'center_x': .9, 'center_y':.1}
    
<ProfileScreen>:
    name: 'profile'
    Screen:
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\medical_logo.png"
            size_hint: .8, .8
            pos_hint: {'center_x': .5, 'center_y': .85}
        MDTextField:
            hint_text: "Username"
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint_x: None
            width: 300
            font_size: "20sp"
            mode: "round"
            icon_right: 'account'        
        MDTextField:
            hint_text: "Password"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: None
            width: 300
            font_size: "20sp"
            mode: "round"
            icon_right: 'eye-off'
        MDLabel:
            text:"Don't have an account? Sign up for RandomTrees"
            font_size: "12sp"
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-Regular.ttf'
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .3}
        MDLabel:
            text:  "or"
            font_size: "12sp"
            color: rgba(52, 0, 231, 255)
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            halign: "center"
            pos_hint: {"center_y": .23}
        
        MDLabel:
            text:  "Social Media Login"
            font_size: "12sp"
            color: rgba(135, 133, 193, 255)
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-Regular.ttf'
            halign: "center"
            pos_hint: {"center_y": .17}
        MDGridLayout:
            cols:3
            size_hint: .45, .07
            pos_hint: {"center_x": .5, "center_y": .1}
            Image:
                source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\google.png"
            Image:
                source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\facebook.png"
            Image:
                source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\apple.png"

        MDRectangleFlatButton:
            text: "Login"
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            size_hint: None, None
            pos_hint: {"center_x": .5, "center_y": .4}
            size: self.size
            halign: "center"
            pos: self.pos
            mode: "round"
            on_press: root.manager.current = 'menu'
                            
<MenuScreen>:
    name: 'menu'
    pos: self.pos
    Screen:
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1    
        Image:
            source: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\audio_wave.png'
            size: .2, .2
            pos_hint: {'center_x': .5, 'center_y':.64}    
        MDLabel:
            text: "HI, Jaikanth!"
            font_size: "18sp"
            color:  0/255, 0/255, 0/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            pos_hint: {'center_x': .56, 'center_y': .95}  
        MDLabel:
            text:root.result
            font_size: "14sp"
            color: 8/255, 124/255, 180/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            pos_hint: {'center_x': .56, 'center_y': .90}
        MDLabel:
            text: "Voice Recogntion"
            font_size: "18sp"
            color: 0/255, 0/255, 0/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            pos_hint: {'center_x': .56, 'center_y': .83}
        MDLabel:
            text: "Save Time with our Speech Transcription"
            font_size: "14sp"
            color: 8/255, 124/255, 180/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-Regular.ttf'
            pos_hint: {'center_x': .56, 'center_y': .78}
        
        Image:
            source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\profile.gif"
            pos_hint: {'center_x': .85, 'center_y': .94}
            size: 55, 55
            size_hint: None, None
            
        TextInput:
            id: totext
            color: 1, 1, 1, 1
            pos_hint:{'center_x': 0.49, 'center_y': 0.290}
            size_hint: 0.8,0.4
            font_size: '10dp'
            readonly: True

        MDBoxLayout:
            adaptive_height: True
            spacing: 50
            padding: 10
            
            MDIconButton:
                icon: 'magnify'
            MDIconButton:
                icon: 'home'
            MDIconButton:
                icon: 'microphone'
                on_press: root.record()
            MDIconButton:
                icon: 'chevron-right'
                on_press: root.manager.current = 'summarizer'
            
<SummarizerScreen>
    name: 'summarizer'
    orientation: 'vertical'
    pos: self.pos
    Screen:
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1
            
        MDBoxLayout:
            md_bg_color: 237/255, 206/255, 186/255, 1
            size_hint_y: .37
            pos_hint: {"top": 1}

            FitImage:
                source: r"C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\profile.png"
                size_hint: .8, .8
            
        MDLabel:
            text: "Back"
            font_size: "18sp"
            color: 0/255, 0/255, 0/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-Regular.ttf'
            pos_hint: {'center_x': .615, 'center_y': .949}
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_y': .95}
            on_press: root.manager.current = 'menu'
        MDLabel:
            text: "Medical Text Summarizer"
            font_size: "20sp"
            color: 0/255, 0/255, 0/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            pos_hint: {'center_x': .56, 'center_y': .83}
        MDLabel:
            text: "Turning long texts into short summaries."
            font_size: "14sp"
            color: 31/255, 32/255, 110/255, 1
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-Regular.ttf'
            pos_hint: {'center_x': .56, 'center_y': .78}
        MDRectangleFlatButton:
            text: "Summarizer"
            font_name: r'C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\fonts\\Poppins-SemiBold.ttf'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, "center_y": .15}
            size: self.size
            halign: "center"
            pos: self.pos
            mode: "round"
            on_press:root.summarizer()
        TextInput:
            id: totext
            color: 1, 1, 1, 1
            pos_hint:{'center_x': 0.49, 'center_y': 0.410}
            size_hint: 0.9,0.4
            font_size: '10dp'
            readonly: True
            radius: [20,]
            mode: "round"
        MDBoxLayout:
            adaptive_height: True
            spacing: 50
            padding: 10
            
            MDIconButton:
                icon: 'magnify'
            MDIconButton:
                icon: 'note'
            MDIconButton:
                icon: 'home'
            MDIconButton:
                icon: 'apps'  
"""

class MDScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class MenuScreen(Screen):
    d = datetime.datetime.now()
    result = d.strftime("%A %d. %B %Y")
    def record(self):
        main()
        voice_text()
        summarize()
        with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\text.json","r") as file:
            result = json.load(file)
            self.ids.totext.text = result["text"]

class SummarizerScreen(Screen):
    def summarizer(self):
        with open(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\summary.json","r") as file:
            result = json.load(file)
            self.ids.totext.text = result["text"]

class MedNarrateApp(MDApp):
    def build(self):
        self.icon="C:\\Users\\ADMIN\\Videos\\mobile_app\\medical_summarization\\icons\\app_icon.png"
        screen = Builder.load_string(screen_helper)
        return screen

if __name__ == '__main__':
    Window.size = (350,580)
    MedNarrateApp().run()
