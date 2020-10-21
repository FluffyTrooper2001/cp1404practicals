"""
convert miles to kilometers
file: convert_m_km.kv
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


__author__ = "Michael Richards"

class Conversion(App):
    message = StringProperty()
    
    def build(self):
        self.title = "Convert Miles to Kilometers."
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root
    
    def convert(self):
        try:
            MILES = float(self.root.ids.input_miles.text)
        except:
            MILES = 0.0
        self.message = str(MILES * 1.60934)
    
    def increment(self):
        self.root.ids.input_miles.text = str(int(self.root.ids.input_miles.text)+1)
    
    def decrement(self):
        """Separate negative increment function for readability"""
        self.root.ids.input_miles.text = str(int(self.root.ids.input_miles.text)-1)

Conversion().run()