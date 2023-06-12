#in order to move buttons around here is the basic functionality

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)

        self.button2 = Button(text="Button 2", size_hint=(0.2, 0.1), pos_hint={'x': 0.5, 'y': 0.4})
        self.button2.bind(on_release=self.swap_buttons)
        self.add_widget(self.button2)

        self.button1 = Button(text="Button 1", size_hint=(0.2, 0.1), pos_hint={'x': 0.1, 'y': 0.4})
        self.button1.bind(on_release=self.swap_buttons)
        self.add_widget(self.button1)

        self.teleported = False

    def swap_buttons(self, button):
        if button == self.button1:
            if not self.teleported:
                self.button1.pos_hint = self.button2.pos_hint
                self.teleported = True
            else:
                self.button1.pos_hint = {'x': 0.1, 'y': 0.4}
                self.teleported = False


class MyApp(App):
    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    MyApp().run()
