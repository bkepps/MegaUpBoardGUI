from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial

def prnt(messag, instance):
    print(messag)
        
class MyGUI(App):

    def build(self):
        wid = Widget()

        #label = Label(text='0')
        buttonA = Button(text='A', on_press=partial(prnt, 'A'))
        buttonB = Button(text='B', on_press=partial(prnt, 'B'))
        buttonC = Button(text='C', on_press=partial(prnt, 'C'))
        buttonD = Button(text='D', on_press=partial(prnt, 'D'))

        layout = BoxLayout(size_hint=(1, None), height=50)
        #layout.add_widget(label)
        layout.add_widget(buttonA)
        layout.add_widget(buttonB)
        layout.add_widget(buttonC)
        layout.add_widget(buttonD)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root
        
if __name__ == '__main__':
    MyGUI().run()