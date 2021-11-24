
from typing import Union, TYPE_CHECKING


if TYPE_CHECKING:
    from pygletmaterial.uiobject import UiObject
from pygletmaterial.layouts.layout import Layout
from pygletmaterial.window import Window
from pygletmaterial.widgets import Widget


class HorizontalLayout(Layout):

    def __init__(self, parent: 'UiObject', padding=10):
        super().__init__(parent)
        self.padding = padding

    def add(self, widget: Widget):
        self._children.append(widget)

    def layout(self):
        pos = self.parent.anchor.copy()
        pos.x += self.padding
        pos.y -= self.padding

        max_row_height = 0
        for widget in self.widgets:
            max_row_height = widget.bounds.height if widget.bounds.height > max_row_height else max_row_height
            if pos.x + widget.bounds.width > self.window.width:
                pos.x = 0
                pos.y -= max_row_height
                max_row_height = 0

            widget.move(pos)
            pos.x += widget.bounds.width
        self.resize_rect()
