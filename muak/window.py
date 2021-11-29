
# Library imports
import pyglet
from typing import Tuple, TYPE_CHECKING, Optional, List

# Project imports
if TYPE_CHECKING:
    from muak.gui import Gui
from muak.uiobject import UiObject
from muak.vector2d import Vector2D
from muak.event import *

"""
            -------------gui-------------
              V                       V
            Window                  Window
              V                       V
    --------Layout--------          Layout
      V       V       V               V
    Widget  Widget  Layout          Widget
                      V
                    Widget
"""


class Window(UiObject):

    def __init__(self, parent: UiObject, size: Tuple[int, int]):
        super().__init__(parent)
        self._window = pygletWindow(self, size)
        self._batches = [pyglet.graphics.Batch() for x in range(10)]

    @property
    def batch(self) -> List:
        return self._batches.copy()

    @property
    def width(self):
        return self._window.width

    @property
    def height(self):
        return self._window.height

    @property
    def window(self):
        return self

    @property
    def mouse_in_window(self) -> bool:
        return self._window._mouse_in_window

    @property
    def mouse_position(self) -> Optional[Vector2D]:
        return Vector2D(self._window._mouse_x, self._window._mouse_y) if self._window._mouse_in_window else None

    @property
    def anchor(self):
        return Vector2D(10, self._window.height-10)

    def on_resize(self, event: ResizeEvent):
        pass

    def on_draw(self, event: DrawEvent):
        self._window.clear()
        draws = 0
        for batch in self._batches:
            draws += batch.draw()

class pygletWindow(pyglet.window.Window):

    def __init__(self, parent, size: Tuple[int, int]):
        super().__init__(*size, resizable=True)
        self._parent = parent

    def on_mouse_motion(self, x, y, dx, dy):
        self._parent.event(MouseMoveEvent(self._parent, x=x, y=y, dx=dx, dy=dy))

    def on_mouse_press(self, x, y, button, modifiers):
        self._parent.event(GlobalMousePressEvent(self._parent, x=x, y=y, button=button, modifiers=modifiers))

    def on_mouse_release(self, x, y, button, modifiers):
        self._parent.event(GlobalMouseReleaseEvent(self._parent, x=x, y=y, button=button, modifiers=modifiers))

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self._parent.event(ResizeEvent(self._parent, width=width, height=height))

    def on_draw(self):
        self._parent.event(DrawEvent(self._parent))

    def on_close(self):
        super().on_close()
        self._parent.event(ExitEvent(self._parent, propagation=[PROPAGATE_UP]))

