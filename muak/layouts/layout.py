
# Library imports
from typing import Union

# Project imports
from muak.widgets import Widget
from muak.window import Window
from muak.rect import Rect
from muak.uiobject import UiObject
from muak.event import *


class Layout(UiObject):

    def __init__(self, parent: UiObject):
        super().__init__(parent)
        self._rect = Rect()
        self.show_bb()
        self._last_mouseover = None

    @property
    def parent(self):
        return self._parent

    @property
    def window(self) -> Window:
        if isinstance(self._parent, Window):
            return self._parent
        else:
            return self._parent.window

    @property
    def widgets(self):
        return [uiobj for uiobj in self._children if isinstance(uiobj, Widget)]

    @property
    def anchor(self):
        return None

    @property
    def bounds(self):
        return self._rect.copy()

    def add(self, widget: 'Widget'):
        pass

    def on_global_mouse_press(self, event: GlobalMousePressEvent):
        for widget in self.widgets:
            if widget.is_mouse_on():
                widget.event(MousePressEvent(widget, event.position.x, event.position.y, event.button, event.modifiers,
                                             propagation=[NO_PROPAGATION]))
                break

    def on_global_mouse_release(self, event: GlobalMouseReleaseEvent):
        for widget in self.widgets:
            if widget.is_mouse_on():
                widget.event(MouseReleaseEvent(widget, event.position.x, event.position.y, event.button, event.modifiers,
                                             propagation=[NO_PROPAGATION]))
                break

    def on_mouse_move(self, event: MouseMoveEvent):
        for widget in self.widgets:
            if widget.is_mouse_on():
                if widget is self._last_mouseover:
                    return
                widget.event(MouseOverEvent(source=widget, propagation=[NO_PROPAGATION]))
                if self._last_mouseover:
                    self._last_mouseover.event(MouseOutEvent(source=self._last_mouseover, propagation=[NO_PROPAGATION]))
                self._last_mouseover = widget
                break
            elif self._last_mouseover:
                self._last_mouseover.event(MouseOutEvent(source=self._last_mouseover, propagation=[NO_PROPAGATION]))
                self._last_mouseover = None

    def on_resize(self, event: ResizeEvent):
        print("Layout resize event!")
        self.layout()
        self.show_bb()

    def layout(self):
        pass

    def resize_rect(self):
        if len(self.widgets):
            self._rect = self.widgets[0].bounds.copy()
            for widget in self.widgets[1:]:
                self._rect.expand_to_contain(widget.bounds)
