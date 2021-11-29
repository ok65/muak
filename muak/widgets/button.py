
# Library imports
import pyglet
from typing import Optional, Dict

# Project imports
from muak.widgets import Widget
from muak.layouts import Layout
from muak.defines import *
from muak.rect import Rect


class Button(Widget):

    def __init__(self, parent: Layout, text: str, style: Optional[Dict] = None):
        super().__init__(parent, style)
        self._text = text

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value

    def draw(self):
        margin = self._style.get("margin", 0)
        label = pyglet.text.Label(text, font_name="Arial", font_size=36, x=200, y=200,
                                  batch=parent.window.batch[z_index + 1],
                                  anchor_y=VALIGN_TOP, color=(255, 0, 0, 255))
        box_width = label.content_width + (2 * margin)
        box_height = label.content_height + (2 * margin)
        box = pyglet.shapes.Rectangle(0, 0, box_width, box_height, color=(250, 250, 250),
                                      batch=parent.window.batch[z_index])
        box.anchor_y = box_height - margin
        box.anchor_x += margin
        self._sprites.extend((box, label))

    def color(self):
        pass