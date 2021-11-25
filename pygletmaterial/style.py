
# Library imports
from typing import Tuple, TYPE_CHECKING

# Project imports
if TYPE_CHECKING:
    from pygletmaterial.uiobject import UiObject
from pygletmaterial.event import StyleChangeEvent, NO_PROPAGATION
import pygletmaterial.color as color 


_UDLR = Tuple[float, float, float, float]

BOLD = "bold"
NORMAL = "normal"
SEMIBOLD = "semibold"
LEFT = "left"
CENTER = "center"
RIGHT = "right"


class Style:

    def __init__(self, parent: 'UiObject'):
        self._parent = parent
        self._text_color = color.BLACK
        self._background_color = color.WHITE
        self._font_size = 14
        self._font_weight = NORMAL
        self._text_align = LEFT
        self._padding = (0, 0, 0, 0)
        self._margin = (0, 0, 0, 0)

    @property
    def text_color(self) -> color.Color:
        return self._text_color

    @text_color.setter
    def text_color(self, value: color.Color):
        self._text_color = value
        self._style_change("text_color", value)

    @property
    def background_color(self) -> color.Color:
        return self._background_color

    @background_color.setter
    def background_color(self, value: color.Color):
        self._background_color = value
        self._style_change("background_color", value)

    @property
    def font_size(self) -> float:
        return self._font_size

    @font_size.setter
    def font_size(self, value: float):
        self._font_size = value
        self._style_change("font_size", value)

    @property
    def font_weight(self) -> str:
        return self._font_weight

    @font_weight.setter
    def font_weight(self, value: str):
        self._font_weight = value
        self._style_change("font_weight", value)

    @property
    def text_align(self) -> str:
        return self._text_align

    @text_align.setter
    def text_align(self, value: str):
        self._text_align = value
        self._style_change("text_align", value)

    @property
    def padding(self) -> _UDLR:
        return self._padding

    @padding.setter
    def padding(self, value: _UDLR):
        self._padding = value
        self._style_change("padding", value)

    @property
    def margin(self) -> _UDLR:
        return self._margin

    @margin.setter
    def margin(self, value: _UDLR):
        self._margin = value
        self._style_change("margin", value)

    def _style_change(self, style, value):
        self._parent.event(StyleChangeEvent(None, (style, value), propagation=[NO_PROPAGATION]))