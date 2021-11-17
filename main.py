
from pygletmaterial.gui import Gui
from pygletmaterial.widget import Widget
from pygletmaterial.rect import Rect
from pygletmaterial.vector2d import Vector2D


if __name__ == "__main__":

    gui = Gui()

    w1 = Widget(gui, window=gui.windows[0], bb=Rect(center=Vector2D(512, 384), width=100, height=30))

    gui.run()

