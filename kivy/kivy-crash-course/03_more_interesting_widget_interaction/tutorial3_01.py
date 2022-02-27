from kivy.app import App

from kivy.uix.scatter import Scatter # This tracks stuff
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout # This replaces the main screen like a desktop
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical') # The default orientation is horizontal.
        t = TextInput(font_size=150,
                      size_hint_y=None,
                      height=200,
                      text='default'
        );
        f = FloatLayout()
        s = Scatter() # You can disable scaling or rotation
        l = Label(text = 'default',
                  font_size = 150
        )
        t.bind(text=l.setter('text')) # The `some_function` has still be created manually

        # You can only return one of above instances, so the others have to be children of the one returning.
        f.add_widget(s)
        s.add_widget(l)
        b.add_widget(f)
        b.add_widget(t)
        return b # we now are only returning the boxlayout

if __name__ == "__main__":
    TutorialApp().run()