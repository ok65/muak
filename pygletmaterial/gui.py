
# Library imports
import pyglet

# Project imports
from pygletmaterial.window import Window


class Gui:

    def __init__(self):
        self.windows = [Window(self, (1024, 768))]
        self.batch = [pyglet.graphics.Batch()]

    def run(self):
        pyglet.app.run()