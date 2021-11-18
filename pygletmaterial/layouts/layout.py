
# Library imports
from typing import Union

# Project imports
from pygletmaterial.widgets import Widget
from pygletmaterial.window import Window
from pygletmaterial.rect import Rect
from pygletmaterial.uiobject import UiObject


class Layout(UiObject):

    def __init__(self, parent: UiObject):
        super().__init__(parent)
        self._rect = Rect()

    @property
    def parent(self):
        return self._parent

    @property
    def window(self):
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

    def on_resize(self):
        print("Layout resize event!")

    def layout(self):
        if len(self.widgets):
            self._rect = self.widgets[0].bounds.copy()
            for widget in self.widgets[1:]:
                self._rect.expand_to_contain(widget.bounds)