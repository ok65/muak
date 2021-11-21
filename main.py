
# Library imports
from pygletmaterial.gui import Gui
from pygletmaterial.widgets import Label
from pygletmaterial.vector2d import Vector2D
from pygletmaterial.layouts import HorizontalLayout
from pygletmaterial.window import pygletWindow

from pyglet.shapes import Line
import pyglet

"""
class pWindow:

    def __init__(self):
        self.window = Wind()
        self.batch = pyglet.graphics.Batch()


class Wind(pyglet.window.Window):

    def __init__(self):
        super().__init__(1024, 768, resizable=True)


    def on_draw(self):
        self.clear()
        self.batch.draw()
"""


if __name__ == "__main__":

    gui = Gui()

    layout = HorizontalLayout(gui.windows[0])

    #la1 = Label("hi", x=200, y=200, batch=wind.batch)

    l1 = Label(layout, "Hello", Vector2D(512, 384))
    l2 = Label(layout, "world", Vector2D(0,0))
    l3 = Label(layout, "keep", Vector2D(0, 0))
    l4 = Label(layout, "coding", Vector2D(0, 0))
    layout.layout()


    gui.run()

