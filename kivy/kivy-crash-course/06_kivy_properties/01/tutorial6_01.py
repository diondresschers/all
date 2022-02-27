from kivy.app import App

from kivy.uix.scatter import Scatter # This tracks stuff
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout # This replaces the main screen like a desktop
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import random

class ScatterTextWidget(BoxLayout):
    def change_label_colour(self, *args):
        colour = [random.random(), random.random(), random.random()] + [1]
        label = self.ids['mijn_labeltje'] # Kivy bevat alle IDs in de *.kv file, dus Python weet over welke label het gaat.
        label.color = colour

        labeltje_1 = self.ids['labeltje_1'] # Beide zijn precies hetzelfde (zie onder) alleen een andere notatie.
        labeltje_2 = self.ids.labeltje_2  # Beide zijn precies hetzelfde (zie boven) alleen een andere notatie.

        labeltje_1.color = colour
        labeltje_2.color = colour

        
class TutorialApp(App): # Kivy is going to check for a *.kv file which is the name of the Class minus `App`, thus `tutorial.kv`
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()
