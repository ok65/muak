
import pyglet

from muak.widgets.widget import Widget
from muak.defines import *
from muak.rect import Rect


class Label(Widget):

    def __init__(self, parent, text, position, z_index=1):
        super().__init__(parent=parent)
        label = pyglet.text.Label(text, font_name="Arial", font_size=36, x=position.x, y=position.y,
                                  batch=parent.window.batch[z_index], anchor_y=VALIGN_TOP, color=(255, 0, 0, 255))
        self._rect = Rect(top_left=position, width=label.content_width, height=label.content_height)
        self._rect.bottom_left = position
        self._sprites.append(label)
        print("Label added to batch")
        self.show_bb()