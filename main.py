import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
kivy.require('1.0.6')


def click_but1(instance):
    instance.text = "hello"

class MyApp(App):
    but1 = Button(on_press = click_but1)
    but2 = Button(on_press=click_but1)
    but3 = Button(on_press=click_but1)
    but4 = Button(on_press=click_but1)
    lay = BoxLayout(padding = 10,orientation = 'vertical ')
    lay.add_widget(but1)
    lay.add_widget(but2)
    lay.add_widget(but3)
    lay.add_widget(but4)
    def build(self):
        return self.lay


if __name__ == '__main__':
    MyApp().run()
