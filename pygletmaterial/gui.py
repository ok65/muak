
# Library imports
import pyglet

# Project imports
from pygletmaterial.window import Window
from pygletmaterial.uiobject import UiObject
from pygletmaterial.event import ExitEvent


class Gui(UiObject):

    def __init__(self):
        super().__init__(None)
        self._gui_root = True
        self.windows = [Window(self, (1024, 768))]

    def run(self):
        pyglet.app.run()

    def on_exit(self, event: ExitEvent):
        pyglet.app.exit()

