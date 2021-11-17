
# Library imports
from typing import TYPE_CHECKING, Optional
from sigbox import SignalBoxClass, SignalDecorator
from pyglet.event import EventDispatcher
from pyglet.window import Window

# Project imports
if TYPE_CHECKING:
    from pygletmaterial.gui import Gui
from pygletmaterial.rect import Rect


class Widget(SignalBoxClass):

    def __init__(self, gui: 'Gui', window: Optional[Window], bb: Optional[Rect]):
        super().__init__(["init", "enable", "show", "mouse_over"])
        self.signals.bind("init", self.on_init)
        self.signals.bind("enable", self.on_enable, )
        self._window = window if window else gui.windows[0]
        self._gui = gui
        self._evt = EventDispatcher()
        self._enable = True
        self._show = True
        self._mouse_on = False
        self._bb = bb.copy()

    def on_init(self):
        pass

    def on_enable(self, enable: bool):
        pass

    def on_show(self, show: bool):
        pass

    def on_mouse_over(self):
        print("mouse on")

    @property
    def window(self):
        return self._window

    @property
    def enable(self) -> bool:
        return self._enable

    @enable.setter
    def enable(self, value: bool):
        self._enable = value
        self._evt.dispatch_event("on_enable", value)

    @property
    def show(self) -> bool:
        return self._show

    @show.setter
    def show(self, value: bool):
        self._show = value
        self._evt.dispatch_event("on_show", value)

    def is_mouse_on(self):
        if self.window.mouse_in_window:
            return self._bb.contains_point(self.window.mouse_position)

    def mouse_update(self):
        if not self._mouse_on:
            if self.is_mouse_on():
                self._mouse_on = True
                self._evt.dispatch_event("on_mouse_over")
        else:
            if not self.is_mouse_on():
                self._mouse_on = False
                self._evt.dispatch_event("on_mouse_out")


