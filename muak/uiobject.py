
# Library imports
from typing import List, Optional
import pyglet

# Project imports
from muak.event import Event
from muak.rect import Rect


class UiObject:

    def __init__(self, parent, isroot: Optional[bool] = False):
        self._children = []
        self._parent = parent
        self._gui_root = False
        self._rect = Rect()
        self._isroot = isroot
        if not isroot:
            self._parent.add(self)

    @property
    def bounds(self):
        return self._rect

    @property
    def children(self) -> List:
        return self._children.copy()

    @property
    def window(self):
        return self._parent.window

    @property
    def parent(self) -> List:
        return self._parent

    def add(self, obj: 'UiObject'):
        self._children.append(obj)

    def reparent(self, new_parent):
        self._parent = new_parent

    def show_bb(self):
        self._debug_sprites = []
        l1 = pyglet.shapes.Line(*self._rect.top_left.tuple(), *self._rect.top_right.tuple(), width=5, color=(255, 0, 0), batch=self.window.batch[0])
        l2 = pyglet.shapes.Line(*self._rect.top_right.tuple(), *self._rect.bottom_right.tuple(), width=5, color=(255, 0, 0), batch=self.window.batch[0])
        l3 = pyglet.shapes.Line(*self._rect.bottom_right.tuple(), *self._rect.bottom_left.tuple(), width=5, color=(255, 0, 0), batch=self.window.batch[0])
        l4 = pyglet.shapes.Line(*self._rect.bottom_left.tuple(), *self._rect.top_left.tuple(), width=5, color=(255, 0, 0), batch=self.window.batch[0])
        self._debug_sprites = [l1, l2, l3, l4]

    def is_mouse_on(self):
        if self.window.mouse_in_window:
            return self._rect.contains_point(self.window.mouse_position)

    def event(self, event: Event):

        # If propagate only flag is set, do not handle locally. Clear flag for next recipient.
        # Otherwise call local on_eventname() method
        if event.propagate_only:
            event.propagate_only = False
        else:
            if event.handle in dir(self):
                getattr(self, event.handle)(event)

        # Send event to children if propagate down flag is set
        if event.propagate_down:
            for child in self._children:
                child.event(event)

        # Send event to parent if propagate up flag is set
        if event.propagate_up and not self._gui_root:
            self._parent.event(event)
