from kivy.app import App

from kivy.uix.scatter import Scatter # This tracks stuff
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout # This replaces the main screen like a desktop
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty, ObjectProperty # zo kan je properties van een Widget gebruiken in andere Widgets

from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)

from kivy.graphics.context_instructions import Color

import random

class ScatterTextWidget(BoxLayout):
    text_colour = ListProperty([1, 0, 0, 1]) # Now we defined a new Kivy property.

    # every widget has a canvas on which you can draw...

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)

    def change_label_colour(self, *args):
        colour = [random.random(), random.random(), random.random()] + [1]
        self.text_colour = colour # Dit is beter dan losse `id` te zetten.

class TutorialApp(App): # Kivy is going to check for a *.kv file which is the name of the Class minus `App`, thus `tutorial.kv`
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()
