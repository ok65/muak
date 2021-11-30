
# Library imports
from typing import TYPE_CHECKING, Union, Iterable, List
import inspect

# Project imports
if TYPE_CHECKING:
    from muak.uiobject import UiObject
from muak.event import StyleChangeEvent
import muak.color as color
from muak.defines import *


class Style:

    def __init__(self, parent: 'UiObject', style_dict: dict = None):
        self._parent = parent
        self._text_color = color.BLACK
        self._background_color = color.WHITE
        self._font_size = 14
        self._font_weight = NORMAL
        self._font_family = "Arial"
        self._text_align = LEFT
        self._padding = _TopRightBottomLeft.zero()
        self._margin = _TopRightBottomLeft.zero()
        self._z_index = 1
        if style_dict:
            self.update(style_dict)

    def update(self, update_dict: dict):
        for k, v in update_dict.items():
            try:
                getattr(self, k)
            except AttributeError:
                continue
            else:
                setattr(self, k, v)

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
    def font_family(self):
        return self._font_family

    @font_family.setter
    def font_family(self, value: str):
        self._font_family = value

    @property
    def text_align(self) -> str:
        return self._text_align

    @text_align.setter
    def text_align(self, value: str):
        self._text_align = value
        self._style_change("text_align", value)

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, value: Union[float, Iterable[float]]):
        self._padding = _TopRightBottomLeft(value)
        self._style_change("padding", self._padding)

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def margin(self, value: Union[float, Iterable[float]]):
        self._margin = _TopRightBottomLeft(value)
        self._style_change("margin", self._margin)

    @property
    def z_index(self):
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = value
        self._style_change("z_index", value)

    def _style_change(self, style, value):
        self._parent.event(StyleChangeEvent(None, (style, value), propagation=[NO_PROPAGATION]))


class _TopRightBottomLeft:

    def __init__(self, value_list: Union[tuple, list, float]):
        # All same
        if not isinstance(value_list, list):
            self._top = self._right = self._bottom = self._left = value_list
        # [top, right, bottom, left]
        elif len(value_list) == 4:
            self._top = value_list[0]
            self._right = value_list[1]
            self._bottom = value_list[2]
            self._left = value_list[3]
        # [top, right+left, bottom]
        elif len(value_list) == 3:
            self._top = value_list[0]
            self._right = value_list[1]
            self._bottom = value_list[2]
            self._left = value_list[1]
        # [top+bottom, right+left]
        elif len(value_list) == 2:
            self._top = value_list[0]
            self._right = value_list[1]
            self._bottom = value_list[0]
            self._left = value_list[1]
        else:
            raise Exception("Expected float/int or list of 2-4 values instead got{}".format(repr(value_list)))

    @classmethod
    def zero(cls):
        return _TopRightBottomLeft([0,0,0,0])

    @property
    def top(self) -> float:
        return self._top

    @top.setter
    def top(self, value: float):
        self._top = value

    @property
    def right(self) -> float:
        return self._top

    @right.setter
    def right(self, value: float):
        self._top = value

    @property
    def bottom(self) -> float:
        return self._top

    @bottom.setter
    def bottom(self, value: float):
        self._top = value

    @property
    def left(self) -> float:
        return self._top

    @left.setter
    def left(self, value: float):
        self._top = value

    @property
    def all(self) -> List[float]:
        return [self._top, self._right, self._bottom, self._left]



if __name__ == "__main__":


    style = Style(None)

    print(style.margin.bottom)
    print(style.margin)




