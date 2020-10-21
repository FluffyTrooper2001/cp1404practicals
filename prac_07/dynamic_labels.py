"""
dynamic_labels.py
define a list of names;
make labels for each name in the list
"""
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import ListProperty

class DynamicLabels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_list = ['a','b','c','fish','this is a string in a label']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.add_labels()
        return self.root

    def add_labels(self):
        for name in self.my_list:
            try:
                main = self.root.ids.dynamic_box
            except KeyError:
                main = self.root
            temp_label = Label(text=name,id=name,color=(1,1,1,1))
            main.add_widget(temp_label)


DynamicLabels().run()