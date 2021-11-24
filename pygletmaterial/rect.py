
# Library imports
from typing import Optional, Union

# Project imports
from pygletmaterial.vector2d import Vector2D


class Rect:

    def __init__(self, top_left: Optional[Vector2D] = None, bottom_right: Optional[Vector2D] = None,
                 top_right: Optional[Vector2D] = None, bottom_left: Optional[Vector2D] = None,
                 width: Union[float, int, None] = None, height: Union[float, int, None] = None,
                 center: Optional[Vector2D] = None):

        # Initialise tl/br to origin
        self._top_left = Vector2D(0, 0)
        self._bottom_right = Vector2D(0, 0)

        # Update parameters where provided
        if isinstance(top_left, Vector2D):
            self._top_left = top_left.copy()
        if isinstance(bottom_right, Vector2D):
            self._bottom_right = bottom_right.copy()
        if isinstance(top_right, Vector2D) and width is not None and height is not None:
            self._top_left = Vector2D(top_right.x - width, top_right.y)
            self._bottom_right = Vector2D(top_right.x, top_right.y - height)
        if isinstance(bottom_left, Vector2D) and width is not None and height is not None:
            self._top_left = Vector2D(bottom_left.x, bottom_left.y + height)
            self._bottom_right = Vector2D(bottom_left.x + width, bottom_left.y)
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if isinstance(center, Vector2D):
            self.center = center

    @property
    def size(self) -> Vector2D:
        return Vector2D(self.width, self.height)

    @property
    def top_left(self) -> Vector2D:
        return self._top_left.copy()

    @top_left.setter
    def top_left(self, value: Vector2D):
        h = self.height
        w = self.width
        self._top_left = value.copy()
        self._bottom_right = Vector2D(value.x + w, value.y - h)

    @property
    def top_right(self) -> Vector2D:
        return Vector2D(self._bottom_right.x, self._top_left.y)

    @top_right.setter
    def top_right(self, value: Vector2D):
        h = self.height
        w = self.width
        self._top_left = Vector2D(value.x - w, value.y)
        self._bottom_right = Vector2D(value.x, value.y - h)

    @property
    def bottom_left(self) -> Vector2D:
        return Vector2D(self._top_left.x, self._bottom_right.y)

    @bottom_left.setter
    def bottom_left(self, value: Vector2D):
        w = self.width
        h = self.height
        self._top_left = Vector2D(value.x, value.y + h)
        self._bottom_right = Vector2D(value.x + w, value.y)

    @property
    def bottom_right(self) -> Vector2D:
        return self._bottom_right.copy()

    @bottom_right.setter
    def bottom_right(self, value: Vector2D):
        w = self.width
        h = self.height
        self._bottom_right = value.copy()
        self._top_left = Vector2D(self._bottom_right.x - w, self._bottom_right.y + h)

    @property
    def width(self) -> int:
        return abs(self._bottom_right.x - self._top_left.x)

    @width.setter
    def width(self, value: int):
        self._bottom_right.x = self._top_left.x + value

    @property
    def height(self):
        return abs(self._top_left.y - self._bottom_right.y)

    @height.setter
    def height(self, value):
        self._bottom_right.y = self._top_left.y - value

    @property
    def center(self):
        return Vector2D(self._top_left.x + self.width/2, self._top_left.y - self.height/2)

    @center.setter
    def center(self, value):
        width = self.width
        height = self.height
        self._top_left.x = value.x - width/2
        self._top_left.y = value.y + height/2

    def copy(self) -> 'Rect':
        return Rect(top_left=self._top_left, bottom_right=self._bottom_right)

    def contains_point(self, point: Vector2D) -> bool:
        return self._top_left.x < point.x < self._bottom_right.x and \
            self.top_left.y > point.y > self._bottom_right.y

    def __repr__(self):
        return "Rect({}, {})".format(self._top_left.tuple(), self._bottom_right.tuple())

    def expand_to_contain_point(self, point: Vector2D):
        if self._top_left.x > point.x:
            self._top_left.x = point.x
        elif self._bottom_right.x < point.x:
            self._bottom_right.x = point.x

        if self._top_left.y < point.y:
            self._top_left.y = point.y
        elif self._bottom_right.y > point.y:
            self._bottom_right.y = point.y

    def expand_to_contain(self, rect: 'Rect'):
        self.expand_to_contain_point(rect.top_left)
        self.expand_to_contain_point(rect.top_right)
        self.expand_to_contain_point(rect.bottom_left)
        self.expand_to_contain_point(rect.bottom_right)



if __name__ == "__main__":

    r = Rect(Vector2D(5, 15), width=10, height=5)
    pass

    r.width = 20

    pass