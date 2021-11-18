
import pyglet

from pygletmaterial.widgets.widget import Widget
from pygletmaterial.vector2d import Vector2D
from pygletmaterial.rect import Rect

VALIGN_TOP = "top"
VALIGN_CENTER = "center"
VALIGN_BASELINE = "baseline"
VALIGN_BOTTOM = "bottom"
HALIGN_LEFT = "left"
HALIGN_CENTER = "center"
HALIGN_RIGHT = "right"


class Label(Widget):

    def __init__(self, parent, text, position):
        super().__init__(parent=parent)
        label = pyglet.text.Label(text, font_name="Arial", font_size=36, x=position.x, y=position.y,
                                  batch=parent.window.batch, anchor_y=VALIGN_TOP, color=(255, 0, 0, 255))
        self._rect = Rect(top_left=position, width=label.content_width, height=label.content_height)
        self._rect.bottom_left = position
        self._sprites.append(label)
        print("Label added to batch")
        self.show_bb()