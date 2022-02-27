from kivy.app import App

from kivy.uix.scatter import Scatter # This tracks stuff
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout # This replaces the main screen like a desktop

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter() # You can disable scaling or rotation
        l = Label(text = 'Hello',
                  font_size = 150,
        )
        # You can only return one of above instances, so the others have to be children of the one returning.
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == "__main__":
    TutorialApp().run()