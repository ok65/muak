
# Library import
import operator
import math


class Vector2D:

    __slots__ = ['_x', '_y']

    def __init__(self, x_or_pair=None, y = None, bearing = None, magnitude = None):
        """
        2D Integer vector class, 'inspired' by pygame/cocos2d etc
        :param x_or_pair:
        :param y:
        :param bearing:
        :param magnitude:
        """

        # Initialise internal x/y values to zero
        self._x = 0
        self._y = 0

        # Set x and y by various different means
        if bearing is not None and magnitude is not None:
            self.x = magnitude * math.cos(math.radians(bearing))
            self.y = magnitude * math.sin(math.radians(bearing))
        elif y is not None:
            self.x = x_or_pair
            self.y = y
        elif x_or_pair is not None:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            raise Exception("Not enough parameters passed")

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = int(value)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = int(value)

    def tuple(self) -> tuple:
        return self.x, self.y

    def copy(self):
        return Vector2D(self.x, self.y)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Invalid subscript "+str(key)+" to Vector2D")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript "+str(key)+" to Vector2D")

    # String representaion (for debugging)
    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    # Comparison
    def __eq__(self, other):
        if hasattr(other, "__getitem__") and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        else:
            return False

    def __ne__(self, other):
        if hasattr(other, "__getitem__") and len(other) == 2:
            return self.x != other[0] or self.y != other[1]
        else:
            return True

    def __nonzero__(self):
        return bool(self.x or self.y)

    # Generic operator handlers
    def _o2(self, other, f):
        "Any two-operator operation where the left operand is a Vector2D"
        if isinstance(other, Vector2D):
            return Vector2D(f(self.x, other.x),
                            f(self.y, other.y))
        elif (hasattr(other, "__getitem__")):
            return Vector2D(f(self.x, other[0]),
                            f(self.y, other[1]))
        else:
            return Vector2D(f(self.x, other),
                             f(self.y, other))

    def _r_o2(self, other, f):
        "Any two-operator operation where the right operand is a Vector2D"
        if (hasattr(other, "__getitem__")):
            return Vector2D(f(other[0], self.x),
                            f(other[1], self.y))
        else:
            return Vector2D(f(other, self.x),
                            f(other, self.y))

    def _io(self, other, f):
        "inplace operator"
        if (hasattr(other, "__getitem__")):
            self.x = f(self.x, other[0])
            self.y = f(self.y, other[1])
        else:
            self.x = f(self.x, other)
            self.y = f(self.y, other)
        return self

    # Addition
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif hasattr(other, "__getitem__"):
            return Vector2D(self.x + other[0], self.y + other[1])
        else:
            return Vector2D(self.x + other, self.y + other)
    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        elif hasattr(other, "__getitem__"):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other
            self.y += other
        return self

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        elif (hasattr(other, "__getitem__")):
            return Vector2D(self.x - other[0], self.y - other[1])
        else:
            return Vector2D(self.x - other, self.y - other)
    def __rsub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(other.x - self.x, other.y - self.y)
        if (hasattr(other, "__getitem__")):
            return Vector2D(other[0] - self.x, other[1] - self.y)
        else:
            return Vector2D(other - self.x, other - self.y)
    def __isub__(self, other):
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        elif (hasattr(other, "__getitem__")):
            self.x -= other[0]
            self.y -= other[1]
        else:
            self.x -= other
            self.y -= other
        return self

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x*other.x, self.y*other.y)
        if (hasattr(other, "__getitem__")):
            return Vector2D(self.x*other[0], self.y*other[1])
        else:
            return Vector2D(self.x*other, self.y*other)
    __rmul__ = __mul__

    def __imul__(self, other):
        if isinstance(other, Vector2D):
            self.x *= other.x
            self.y *= other.y
        elif (hasattr(other, "__getitem__")):
            self.x *= other[0]
            self.y *= other[1]
        else:
            self.x *= other
            self.y *= other
        return self

    # Division
    def __div__(self, other):
        return self._o2(other, operator.div)
    def __rdiv__(self, other):
        return self._r_o2(other, operator.div)
    def __idiv__(self, other):
        return self._io(other, operator.div)

    def __floordiv__(self, other):
        return self._o2(other, operator.floordiv)
    def __rfloordiv__(self, other):
        return self._r_o2(other, operator.floordiv)
    def __ifloordiv__(self, other):
        return self._io(other, operator.floordiv)

    def __truediv__(self, other):
        return self._o2(other, operator.truediv)
    def __rtruediv__(self, other):
        return self._r_o2(other, operator.truediv)
    def __itruediv__(self, other):
        return self._io(other, operator.floordiv)

    # Modulo
    def __mod__(self, other):
        return self._o2(other, operator.mod)
    def __rmod__(self, other):
        return self._r_o2(other, operator.mod)

    def __divmod__(self, other):
        return self._o2(other, operator.divmod)
    def __rdivmod__(self, other):
        return self._r_o2(other, operator.divmod)

    # Exponentation
    def __pow__(self, other):
        return self._o2(other, operator.pow)
    def __rpow__(self, other):
        return self._r_o2(other, operator.pow)

    # Bitwise operators
    def __lshift__(self, other):
        return self._o2(other, operator.lshift)
    def __rlshift__(self, other):
        return self._r_o2(other, operator.lshift)

    def __rshift__(self, other):
        return self._o2(other, operator.rshift)
    def __rrshift__(self, other):
        return self._r_o2(other, operator.rshift)

    def __and__(self, other):
        return self._o2(other, operator.and_)
    __rand__ = __and__

    def __or__(self, other):
        return self._o2(other, operator.or_)
    __ror__ = __or__

    def __xor__(self, other):
        return self._o2(other, operator.xor)
    __rxor__ = __xor__

    # Unary operations
    def __neg__(self):
        return Vector2D(operator.neg(self.x), operator.neg(self.y))

    def __pos__(self):
        return Vector2D(operator.pos(self.x), operator.pos(self.y))

    def __abs__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def __invert__(self):
        return Vector2D(-self.x, -self.y)

    # vectory functions
    def get_length_sqrd(self):
        return self.x**2 + self.y**2

    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __setlength(self, value):
        length = self.get_length()
        self.x *= value/length
        self.y *= value/length
    length = property(get_length, __setlength, None, "gets or sets the magnitude of the vector")

    def rotate(self, angle_degrees):
        radians = math.radians(angle_degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x*cos - self.y*sin
        y = self.x*sin + self.y*cos
        self.x = x
        self.y = y

    def get_reflected(self):
        return Vector2D(self.x * -1, self.y * -1)

    def reflected(self):
        return self.get_reflected()

    def reflect(self):
        self.x = self.x * -1
        self.y = self.y * -1

    def rotated(self, angle_degrees):
        radians = math.radians(angle_degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x*cos - self.y*sin
        y = self.x*sin + self.y*cos
        return Vector2D(x, y)

    def get_angle(self):
        if (self.get_length_sqrd() == 0):
            return 0
        return math.degrees(math.atan2(self.y, self.x))
    def __setangle(self, angle_degrees):
        self.x = self.length
        self.y = 0
        self.rotate(angle_degrees)
    angle = property(get_angle, __setangle, None, "gets or sets the angle of a vector")

    def get_angle_between(self, other):
        cross = self.x*other[1] - self.y*other[0]
        dot = self.x*other[0] + self.y*other[1]
        return math.degrees(math.atan2(cross, dot))

    def normalized(self):
        length = self.length
        if length != 0:
            return self/length
        return Vector2D(self)

    def normalised(self):
        return self.normalized()

    def normalize_return_length(self):
        length = self.length
        if length != 0:
            self.x /= length
            self.y /= length
        return length

    def normalise_return_length(self):
        return self.normalize_return_length()

    def perpendicular(self):
        return Vector2D(-self.y, self.x)

    def perpendicular_normal(self):
        length = self.length
        if length != 0:
            return Vector2D(-self.y/length, self.x/length)
        return Vector2D(self)

    def dot(self, other):
        return float(self.x*other[0] + self.y*other[1])

    def get_distance(self, other):
        return math.sqrt((self.x - other[0])**2 + (self.y - other[1])**2)

    def get_dist_sqrd(self, other):
        return (self.x - other[0])**2 + (self.y - other[1])**2

    def projection(self, other):
        other_length_sqrd = other[0]*other[0] + other[1]*other[1]
        projected_length_times_other_length = self.dot(other)
        return other*(projected_length_times_other_length/other_length_sqrd)

    def clamp(self, max, min):
        if self.x > max:
            self.x = max
        elif self.x < min:
            self.x = min
        if self.y > max:
            self.y = max
        elif self.y < min:
            self.y = min

        return self

    def cross(self, other):
        return self.x*other[1] - self.y*other[0]

    def interpolate_to(self, other, range):
        return Vector2D(self.x + (other[0] - self.x)*range, self.y + (other[1] - self.y)*range)

    def convert_to_basis(self, x_vector, y_vector):
        return Vector2D(self.dot(x_vector)/x_vector.get_length_sqrd(), self.dot(y_vector)/y_vector.get_length_sqrd())

    def __getstate__(self):
        return [self.x, self.y]

    def __setstate__(self, dict):
        self.x, self.y = dict
