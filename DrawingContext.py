from PointAndCo import Point, Rectangle


class DrawingContext:

    def __init__(self, orig, target, border=0):
        self.orig_rect = Rectangle(orig)
        self.target_rect = Rectangle(target)
        self.target_border = border

    @property
    def orig_rect(self):
        return self._orig_rect

    @orig_rect.setter
    def orig_rect(self, newValue):
        self._orig_rect = Rectangle(newValue)
        self.set_dirty()

    @property
    def target_rect(self):
        return self._target_rect

    @target_rect.setter
    def target_rect(self, newValue):
        self._target_rect = Rectangle(newValue)
        self.set_dirty()

    @property
    def target_border(self):
        return self._target_border

    @target_border.setter
    def target_border(self, newValue):
        self._target_border = newValue
        self.set_dirty()

    def set_dirty(self):
        self._dirty = True

    def recalc_transpose_parameters_if_necessary(self):
        orig = self.orig_rect
        target = self.target_rect
        border = self.target_border

        oextent = orig.extent
        textent = target.extent

        self._o_translate = -orig.start

        ff = textent / oextent * (1 - 2 * border)
        self._scale = min(ff.xy)

        center_offset = (textent - (oextent * self._scale)) / 2
        self._t_translate = target.start + center_offset

    def o_translate(self):
        if self._dirty:
            self.recalc_transpose_parameters_if_necessary()
        return self._o_translate

    def t_translate(self):
        if self._dirty:
            self.recalc_transpose_parameters_if_necessary()
        return self._t_translate

    def scale(self):
        if self._dirty:
            self.recalc_transpose_parameters_if_necessary()
        return self._scale

    def transpose(self, point):
        return (point + self.o_translate()) * self.scale() + self.t_translate()

    def scaled(self, size):
        return size * self.scale()

    def transposeBack(self, pos):
        if self.scale():
            return (pos - self.t_translate()) / self.scale() - self.o_translate()
        else:
            return Point(pos)

    def __repr__(self):
        return f'{self.__class__.__name__}(orig={repr(self.orig_rect)},target={repr(self.target_rect)},border={repr(self.target_border)})'

    def __str__(self):
        return f'(orig={repr(self.orig_rect)},target={self.target_rect},border={self.target_border})' + \
               f' -> o_translate={self.o_translate()},scale={self.scale()},t_translate={self.t_translate()}'
