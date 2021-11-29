
# Library imports
from typing import TYPE_CHECKING, Optional, List, Tuple
import re
import pyglet

# Project imports
from muak.vector2d import Vector2D
if TYPE_CHECKING:
    from muak.uiobject import UiObject




class Event:

    def __init__(self, source: 'UiObject', propagation: Optional[List] = None):
        propagation = propagation if propagation else [PROPAGATE_DOWN]
        self.name = type(self).__name__
        self._handle = self._handle_name()
        self.propagate_up = PROPAGATE_UP in propagation
        self.propagate_down = PROPAGATE_DOWN in propagation
        self.propagate_only = NO_LOCAL_INVOKE in propagation
        self.source = source

    @property
    def handle(self):
        return self._handle

    def _handle_name(self):
        return "on"+re.sub(r"([A-Z])", "_\\g<0>", type(self).__name__, 0, re.MULTILINE).lower().replace("_event", "")


class ResizeEvent(Event):
    def __init__(self, source: 'UiObject', width: int, height: int, propagation: Optional[List] = None):
        super().__init__(source=source, propagation=propagation)
        self.height = height
        self.width = width


class DrawEvent(Event): pass


class ExitEvent(Event): pass


class MouseMoveEvent(Event):
    def __init__(self, source: 'UiObject', x: int, y: int, dx: int, dy: int, propagation: Optional[List] = None):
        super().__init__(source=source, propagation=propagation)
        self.position = Vector2D(x, y)
        self.delta = Vector2D(dx, dy)

class _MouseButtonEvent(Event):
    def __init__(self, source: 'UiObject', x: int, y: int, button, modifiers, propagation: Optional[List] = None):
        super().__init__(source=source, propagation=propagation)
        self.position = Vector2D(x, y)
        self.button = button
        self.lmb = button == pyglet.window.mouse.LEFT
        self.rmb = button == pyglet.window.mouse.RIGHT
        self.mmb = button == pyglet.window.mouse.MIDDLE
        self.modifiers = modifiers

class GlobalMousePressEvent(_MouseButtonEvent): pass
class GlobalMouseReleaseEvent(_MouseButtonEvent): pass
class MousePressEvent(_MouseButtonEvent): pass
class MouseReleaseEvent(_MouseButtonEvent): pass


class MouseOverEvent(Event): pass
class MouseOutEvent(Event): pass


class StyleChangeEvent(Event):
    def __init__(self, source: 'UiObject', change: Tuple, propagation: Optional[List] = None):
        super().__init__(source=source, propagation=propagation)
        self.change = change