from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial

def callback(instance):
    print('yeet')
        
class MyGUI(App):

    def build(self):
        wid = Widget()

        label = Label(text='0')
        button = Button(text='Hello world', font_size=14)
        button.bind(on_press=callback)

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(label)
        layout.add_widget(button)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root
        
if __name__ == '__main__':
    MyGUI().run()