from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)

        self.teleported = False

    def swap_buttons(self, button):
        if button == self.ids.button1:
            if not self.teleported:
                animation = Animation(pos_hint=self.ids.button2.pos_hint, duration=1)
                animation.start(self.ids.button1)
                self.teleported = True
            else:
                animation = Animation(pos_hint={'x': 0.1, 'y': 0.4}, duration=1)
                animation.start(self.ids.button1)
                self.teleported = False


class MyApp(App):
    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    MyApp().run()
