from kivy.app import App

from kivy.uix.scatter import Scatter # This tracks stuff
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout # This replaces the main screen like a desktop
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty # zo kan je properties van een Widget gebruiken in andere Widgets

import random

class ScatterTextWidget(BoxLayout):

    text_colour = ListProperty([1, 0, 0, 1]) # Now we defined a new Kivy property.

    def change_label_colour(self, *args):
        colour = [random.random(), random.random(), random.random()] + [1]
        label = self.ids['mijn_labeltje'] # Kivy bevat alle IDs in de *.kv file, dus Python weet over welke label het gaat.
        label.color = colour
        self.text_colour = colour # Dit is beter dan losse `id` te zetten.

    #def on_text_colour(self, *args): # Kivy voert dit uit op het moment dat de kleur wijzigt.
        #do_whatever()

class TutorialApp(App): # Kivy is going to check for a *.kv file which is the name of the Class minus `App`, thus `tutorial.kv`
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()
