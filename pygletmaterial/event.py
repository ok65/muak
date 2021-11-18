
# Library imports
from typing import TYPE_CHECKING, Optional
import re

# Project imports
if TYPE_CHECKING:
    from uiobject import UiObject


class Event:

    def __init__(self, source: 'UiObject', data: dict, propagate_down: bool = True,
                 propagate_up: bool = False, propagate_only: bool = True):
        self.name = type(self).__name__
        self._handle = self._handle_name()
        self.data = data
        self.propagate_up = propagate_up
        self.propagate_down = propagate_down
        self.propagate_only = propagate_only
        self.source = source

    @property
    def handle(self):
        return self._handle

    def _handle_name(self):
        return "on"+re.sub(r"([A-Z])", "_\\g<0>", type(self).__name__, 0, re.MULTILINE).lower().replace("_event", "")


class ResizeEvent(Event): pass

class DrawEvent(Event): pass

class ExitEvent(Event): pass