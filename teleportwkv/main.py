#here is an example of the functionality of the same teleportation but with a kv file

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)

        self.teleported = False

    def swap_buttons(self, button):
        if button == self.ids.button1:
            if not self.teleported:
                self.ids.button1.pos_hint = self.ids.button2.pos_hint
                self.teleported = True
            else:
                self.ids.button1.pos_hint = {'x': 0.1, 'y': 0.4}
                self.teleported = False


class MyApp(App):
    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    MyApp().run()
