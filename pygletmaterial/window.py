
# Library imports
import pyglet
from typing import Tuple, TYPE_CHECKING, Optional

# Project imports
if TYPE_CHECKING:
    from pygletmaterial.gui import Gui
from pygletmaterial.vector2d import Vector2D


class Window(pyglet.window.Window):

    def __init__(self, gui: 'Gui', size: Tuple[int, int]):
        super().__init__(*size, resizable=True)
        self._gui = gui
        self._widgets = []

    @property
    def mouse_position(self) -> Optional[Vector2D]:
        return Vector2D(self._mouse_x, self._mouse_y) if self._mouse_in_window else None

    @property
    def mouse_in_window(self) -> bool:
        return self._mouse_in_window

    def on_mouse_motion(self, x, y, dx, dy):
        for widget in self._widgets:
            widget.mouse_update()