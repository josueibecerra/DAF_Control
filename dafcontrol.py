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
    pass


class FourthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("dafcontrol.kv")

class DAFControlApp(App):
    def build(self):
        return kv


if __name__=='__main__':
    DAFControlApp().run()
