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
        
class Quiz(Widget):
    pass

class MyGUI(App):

    def build(self):
        return Quiz()
        
if __name__ == '__main__':
    MyGUI().run()