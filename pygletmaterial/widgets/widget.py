
# Library imports
from typing import TYPE_CHECKING, Optional, Dict
import pyglet.shapes

# Project imports
if TYPE_CHECKING:
    from pygletmaterial.layouts import Layout
from pygletmaterial.uiobject import UiObject
from pygletmaterial.rect import Rect
from pygletmaterial.vector2d import Vector2D


class Widget(UiObject):

    def __init__(self, parent: 'Layout', style: Optional[Dict] = None):
        super().__init__(parent)
        self._enable = True
        self._show = True
        self._mouse_on = False
        self._anchor = Vector2D(0, 0)
        self._debug_sprites = []
        self._sprites = []
        self._style = style if style else {}

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

    def on_mouse_over(self, mouse_on: bool):
        print("mouse on: {}".format(mouse_on))
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


