from kivy.app import App

from kivy.uix.scatter import Scatter # This tracks stuff
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout # This replaces the main screen like a desktop
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import random

class ScatterTextWidget(BoxLayout):
    pass

class TutorialApp(App): # Kivy is going to check for a *.kv file which is the name of the Class minus `App`, thus `tutorial.kv`
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()
