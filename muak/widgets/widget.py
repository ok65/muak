
# Library imports
from typing import TYPE_CHECKING, Optional, Dict
import pyglet.shapes

# Project imports
if TYPE_CHECKING:
    from muak.layouts import Layout
from muak.uiobject import UiObject
from muak.rect import Rect
from muak.vector2d import Vector2D
from muak.event import *
from muak.style import Style


class Widget(UiObject):

    def __init__(self, parent: 'Layout', style: Optional[Dict] = None):
        super().__init__(parent)
        self._enable = True
        self._show = True
        self._mouse_on = False
        self._anchor = Vector2D(0, 0)
        self._debug_sprites = []
        self._sprites = []
        self._style = Style(parent=self, style_dict=style)

    @property
    def style(self) -> Style:
        return self._style

    @property
    def anchor(self) -> Vector2D:
        return self._anchor

    def move(self, pos: Vector2D):
        self._anchor = pos
        self._anchor.x += self._style.get("margin", 0)
        self._anchor.y -= self._style.get("margin", 0)

        try:
            width = self._sprites[0].content_width
            height = self._sprites[0].content_height
        except AttributeError:
            width = self._sprites[0].width
            height = self._sprites[0].height

        self._rect = Rect(top_left=self._anchor, width=width, height=height)

        for sprite in self._sprites:
            sprite.position = self._anchor

        #self.show_bb()

    def on_init(self):
        pass

    def on_enable(self, enable: bool):
        pass

    def on_show(self, show: bool):
        pass

    def on_mouse_over(self, event: MouseOverEvent):
        print("wax on")

    def on_mouse_out(self, event: MouseOutEvent):
        print("wax off")

    def on_mouse_press(self, event: MousePressEvent):
        pass

    def on_mouse_release(self, event: MouseReleaseEvent):
        pass

    @property
    def enable(self) -> bool:
        return self._enable

    @enable.setter
    def enable(self, value: bool):
        self._enable = value

    @property
    def show(self) -> bool:
        return self._show

    @show.setter
    def show(self, value: bool):
        self._show = value

    def on_mouse(self):
        if not self._mouse_on:
            if self.is_mouse_on():
                self._mouse_on = True
                self.on_mouse_over(True)
                #self._evt.dispatch_event("on_mouse_over", self._mouse_on)
        else:
            if not self.is_mouse_on():
                self._mouse_on = False
                self.on_mouse_over(False)
                #self._evt.dispatch_event("on_mouse_over", self._mouse_on)
            else:
                #self.window._
                pass


