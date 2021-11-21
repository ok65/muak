
# Library imports
from typing import List, Optional

# Project imports
from pygletmaterial.event import Event


class UiObject:

    def __init__(self, parent, isroot: Optional[bool] = False):
        self._children = []
        self._parent = parent
        self._gui_root = False
        if not isroot:
            self._parent.add(self)

    def add(self, obj: 'UiObject'):
        self._children.append(obj)

    @property
    def children(self) -> List:
        return self._children.copy()

    @property
    def parent(self) -> List:
        return self._parent

    def reparent(self, new_parent):
        self._parent = new_parent

    def event(self, event: Event):

        print(event.name)

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
