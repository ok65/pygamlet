
# Library imports

# Project imports
from pygamlet.vector2d import Vector2D

class Rect:

    def __init__(self, top_left=None, bottom_right=None, width=None, height=None):

        self.top_left = top_left if top_left is not None else Vector2D(0,0)
        self.bottom_right = bottom_right if bottom_right is not None else Vector2D(0,0)

        if top_left is not None and width is not None:
            self.bottom_right.x = self.top_left.x + width
        elif bottom_right is not None and width is not None:
            self.top_left.x = self.bottom_right.x - width



    @property
    def size(self) -> Vector2D:
        return Vector2D(self._width, self._height)

    @property
    def top_left(self) -> Vector2D:
        return self._top_left

    @top_left.setter
    def top_left(self, value: Vector2D):
        self._top_left = value

    @property
    def width(self) -> int:
        return self.bottom_right.x - self.top_left.x

    @width.setter
    def width(self, value: int):
        self.top_left.x -= (value - self.width)/2
        self.bottom_right.x += (value - self.width) / 2

    def top_right(self):
        pass

    def bottom_left(self):
        pass

    def bottom_right(self):
        pass



    """
        x, y
        top, left, bottom, right
        topleft, bottomleft, topright, bottomright
        midtop, midleft, midbottom, midright
        center, centerx, centery
        size, width, height
        w, h
    """


if __name__ == "__main__":

    r = Rect(Vector2D(5, 5), width=10, height=20)
    pass

    r.width = 20

    pass

