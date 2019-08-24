class Point:
    def __init__(self, xtp=0, y=0):
        if isinstance(xtp, (tuple, list, set)) and len(xtp) == 2:
            x, y = xtp
        elif isinstance(xtp, Point):
            x, y = xtp.x, xtp.y
        elif isinstance(xtp, (int, float)):
            x = xtp
        else:
            raise TypeError("Only numbers, tuples and Points allowed")
        self.x = x
        self.y = y

    @property
    def xy(self):
        return self.x, self.y

    def __eq__(self, other):
        if not isinstance(other, Point):
            try:
                other = Point(other)
            except:
                return False

        return self.xy == other.xy

    def __repr__(self):
        return f'Point(x={self.x},y={self.y})'

    def __str__(self):
        return f'({self.x},{self.y})'


class Rectangle:
    def __init__(self, srt, end=None):
        if isinstance(srt, (tuple, list, set)) and len(srt) == 4:
            sx, sy, ex, ey = srt
        elif isinstance(srt, Rectangle):
            sx, sy, ex, ey = srt.flat_xy()
        else:
            if end is None:
                end = Point()
            sx, sy = Point(srt).xy
            ex, ey = Point(end).xy
        sx, ex = min(sx, ex), max(sx, ex)
        sy, ey = min(sy, ey), max(sy, ey)
        self.start = Point(sx, sy)
        self.end = Point(ex, ey)

    @property
    def width(self):
        return self.end.x - self.start.x

    @property
    def height(self):
        return self.end.y - self.start.y

    def flat_xy(self):
        return self.start.xy + self.end.xy

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            try:
                other = Rectangle(other)
            except:
                return False

        return self.flat_xy() == other.flat_xy()

    def __repr__(self):
        return f'Rectangle(start={repr(self.start)},end={repr(self.end)})'

    def __str__(self):
        return f'[{self.start}-{self.end}]'
