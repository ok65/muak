
# Library imports
import pyglet
from typing import Optional, Dict

# Project imports
from pygletmaterial.widgets import Widget
from pygletmaterial.layouts import Layout
from pygletmaterial.defines import *
from pygletmaterial.rect import Rect


class Button(Widget):

    def __init__(self, parent: Layout, text: str, style: Optional[Dict] = None, z_index=1):
        super().__init__(parent, style)
        if style:
            self._style.update()
        margin = self._style.get("margin", 0)
        label = pyglet.text.Label(text, font_name="Arial", font_size=36, x=200, y=200, batch=parent.window.batch[z_index+1],
                                  anchor_y=VALIGN_TOP, color=(255, 0, 0, 255))
        box_width = label.content_width + (2 * margin)
        box_height = label.content_height + (2 * margin)
        box = pyglet.shapes.Rectangle(0, 0, box_width, box_height, color=(250, 250, 250), batch=parent.window.batch[z_index])
        box.anchor_y = box_height - margin
        box.anchor_x += margin
        self._sprites.extend((box, label))

