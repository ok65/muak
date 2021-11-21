
# Library imports
import pyglet
from typing import Tuple, TYPE_CHECKING, Optional

# Project imports
if TYPE_CHECKING:
    from pygletmaterial.gui import Gui
from pygletmaterial.uiobject import UiObject
from pygletmaterial.vector2d import Vector2D
from pygletmaterial.event import ResizeEvent, DrawEvent, ExitEvent

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
        self._batch = pyglet.graphics.Batch()

    @property
    def batch(self):
        return self._batch

    @property
    def width(self):
        return self._window.width

    @property
    def height(self):
        return self._window.height

    @property
    def mouse_in_window(self) -> bool:
        return self._window._mouse_in_window

    @property
    def mouse_position(self) -> Optional[Vector2D]:
        return Vector2D(self._window._mouse_x, self._window._mouse_y) if self._window.mouse_in_window else None

    @property
    def anchor(self):
        return Vector2D(10, self._window.height-10)

    def on_resize(self, event: ResizeEvent):
        pass

    def on_draw(self, event: DrawEvent):
        self._window.clear()
        print("window clear")
        x = self._batch.draw()
        print("batch draw ({})".format(x))


class pygletWindow(pyglet.window.Window):

    def __init__(self, parent, size: Tuple[int, int]):
        super().__init__(*size, resizable=True)
        self._parent = parent

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self._parent.event(ResizeEvent(self._parent, {"width": width, "height": height}, propagate_only=False))

    def on_draw(self):
        #self._parent.event(DrawEvent(self._parent, {}, propagate_only=False))
        self._parent.on_draw(0)

    def on_close(self):
        super().on_close()
        self._parent.event(ExitEvent(self._parent, {}, propagate_only=False, propagate_up=True, propagate_down=False))