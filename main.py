
# Library imports
from pygletmaterial.gui import Gui
from pygletmaterial.widgets import Label
from pygletmaterial.vector2d import Vector2D
from pygletmaterial.layouts import HorizontalLayout


if __name__ == "__main__":

    gui = Gui()

    layout = HorizontalLayout(gui.windows[0])

    l1 = Label(layout, "Hello", Vector2D(512, 384))
    #l2 = Label(layout, "world -  qwd qwd qwd qwd qwd", Vector2D(0,0))
    #l3 = Label(layout, "apples qwd qwd qwd qw dqwd", Vector2D(0, 0))
    #l4 = Label(layout, "and pears qwd qwd qwd qwd qwd", Vector2D(0, 0))
    #layout.layout()

    gui.run()

