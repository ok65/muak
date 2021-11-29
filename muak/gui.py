
# Library imports
import pyglet

# Project imports
from muak.window import Window
from muak.uiobject import UiObject
from muak.event import ExitEvent


class Muak(UiObject):

    def __init__(self):
        super().__init__(None, isroot=True)
        self.windows = [Window(self, (1024, 768))]

    def run(self):
        pyglet.app.run()

    def on_exit(self, event: ExitEvent):
        pyglet.app.exit()

