from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


Window.size = (300, 533)

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    def pumplist(self):
        print('pumplist')

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("dafcontrol.kv")

class DAFControlApp(App):
    def build(self):
        return kv


if __name__=='__main__':
    DAFControlApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ClassNameWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def pumplist(self, instance):
        print('pumplist')

        for i in range(3):
            window = new SecondWindow()
            App

class ClassNameApp(App):
    def build(self):

        return ClassNameWindow()

if __name__=='__main__':
    ClassNameApp().run()
