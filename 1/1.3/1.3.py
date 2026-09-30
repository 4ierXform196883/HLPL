import math


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self == other

    def __hash__(self):
        return hash((self.x, self.y))

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.dot(other)
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        """Число * вектор."""
        return self * other

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def length(self):
        return abs(self)

    def __str__(self):
        return f"<{self.x}; {self.y}>"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    a = Vector2D(3, 4)
    b = Vector2D(1, 2)
    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a * 2 =", a * 2)
    print("2 * a =", 2 * a)
    print("a * b =", a * b)
    print("|a| =", a.length())
    print("repr:", [a, b])
