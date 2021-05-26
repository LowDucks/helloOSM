# Kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

# Kivy MapView
from kivy.garden.mapview import MapView, MapMarkerPopup
# Kivy properties
from kivy.properties import NumericProperty, StringProperty

class MainScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class Content(MapView):
    def build(self):
        return self

class POIMarkerPopup(MapMarkerPopup):
    latitude = NumericProperty()
    longitude = NumericProperty()
    title = StringProperty()
    description = StringProperty()
    imageUrl = StringProperty()


class MapApp(App):

     def build(self):
         return Builder.load_file('mapViewGUI.kv')

     def change_screen(self, screen, direction):
         self.root.transition.direction = direction
         self.root.current = screen


if __name__ in ('__main__', '__android__'):
    MapApp().run()
