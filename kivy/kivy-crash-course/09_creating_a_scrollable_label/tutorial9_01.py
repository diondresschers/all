from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.base import runTouchApp
from kivy.lang import Builder # This can read Kivy Language

# benath is not a separate file,
Builder.load_string('''
<ScrollableLabel>:
    text: str('some realy realy long string ' * 10)
    font_size: 50
    #color: 1, 0, 0, 1
    text_size: self.size
''')

class ScrollableLabel(Label):
    pass

runTouchApp(ScrollableLabel())
