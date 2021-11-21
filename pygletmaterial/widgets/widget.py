
# Library imports
from typing import TYPE_CHECKING, Optional

import pyglet.shapes
from pyglet.event import EventDispatcher

# Project imports
if TYPE_CHECKING:
    from pygletmaterial.layouts import Layout
from pygletmaterial.uiobject import UiObject
from pygletmaterial.rect import Rect
from pygletmaterial.vector2d import Vector2D


class Widget(UiObject):

    def __init__(self, parent: 'Layout'):
        super().__init__(parent)
        self._enable = True
        self._show = True
        self._mouse_on = False
        self._rect = Rect()
        self._anchor = Vector2D(0, 0)
        self._debug_sprites = []
        self._sprites = []

    @property
    def parent(self):
        return self._parent

    @property
    def bounds(self):
        return self._rect

    @property
    def anchor(self) -> Vector2D:
        return self._anchor

    def move(self, pos: Vector2D):
        self._anchor = pos

        self._rect = Rect(top_left=self._anchor, width=self._sprites[0].content_width, height=self._sprites[0].content_height)

        for sprite in self._sprites:
            sprite.position = self._anchor

        self.show_bb()

    def show_bb(self):
        self._debug_sprites = []
        l1 = pyglet.shapes.Line(*self._rect.top_left.tuple(), *self._rect.top_right.tuple(), color=(255, 0, 0), batch=self.window.batch)
        l2 = pyglet.shapes.Line(*self._rect.top_right.tuple(), *self._rect.bottom_right.tuple(), color=(255, 0, 0), batch=self.window.batch)
        l3 = pyglet.shapes.Line(*self._rect.bottom_right.tuple(), *self._rect.bottom_left.tuple(), color=(255, 0, 0), batch=self.window.batch)
        l4 = pyglet.shapes.Line(*self._rect.bottom_left.tuple(), *self._rect.top_left.tuple(), color=(255, 0, 0), batch=self.window.batch)

        self._debug_sprites = [l1, l2, l3, l4]

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
    def window(self):
        return self._parent.window

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

    def is_mouse_on(self):
        self.a =  self.window.mouse_in_window
        pass
        if self.window.mouse_in_window:
            return self._rect.contains_point(self.window.mouse_position)

    def mouse_update(self):

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


