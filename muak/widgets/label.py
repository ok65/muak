
import pyglet

from muak.widgets.widget import Widget
from muak.defines import *
from muak.rect import Rect
from muak.vector2d import Vector2D
from muak.layouts import Layout


class Label(Widget):

    def __init__(self, parent: Layout, text: str, position: Vector2D):
        super().__init__(parent=parent)
        self.position = position
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self.draw()

    def draw(self):
        label = pyglet.text.Label(self._text, font_name=self.style.font_family, font_size=self.style.font_size,
                                  x=self.position.x, y=self.position.y, batch=self.parent.window.batch[self.style.z_index],
                                  anchor_y=VALIGN_TOP, color=self.style.text_color)
        self._rect = Rect(top_left=self.position, width=label.content_width, height=label.content_height)
        self._rect.bottom_left = self.position
        self._sprites.append(label)
        print("Label added to batch")
        self.show_bb()