import unittest

from PointAndCo import Point, Rectangle


class TestPoint(unittest.TestCase):

    def test_init_default(self):
        tobj = Point()
        self.assertIsNotNone(tobj)
        self.assertEqual(0, tobj.x)
        self.assertEqual(0, tobj.y)

    def test_init(self):
        tobj = Point(5, 9)
        self.assertIsNotNone(tobj)
        self.assertEqual(5, tobj.x)
        self.assertEqual(9, tobj.y)

    def test_init_tuple(self):
        tobj = Point((5, 9), 27)
        self.assertIsNotNone(tobj)
        self.assertEqual(5, tobj.x)
        self.assertEqual(9, tobj.y)

    def test_init_float(self):
        tobj = Point(5.0, 3)
        self.assertIsNotNone(tobj)
        self.assertEqual(5, tobj.x)
        self.assertEqual(3, tobj.y)

    def test_init_Point(self):
        pt = Point(7.0, 13.78)
        tobj = Point(pt)
        self.assertIsNotNone(tobj)
        self.assertEqual(7, tobj.x)
        self.assertEqual(13.78, tobj.y)

    def test_init_failed(self):
        def f1():
            return Point({'x': 3, 'y': 4})

        self.assertRaises(TypeError, f1)

        def f2():
            return Point((1, 2, 3))

        self.assertRaises(TypeError, f2)

    def test_xy(self):
        tobj = Point(5, 9)
        self.assertEqual((5, 9), tobj.xy)

    def test_eq(self):
        tobj = Point(5, 9)
        self.assertTrue(tobj == tobj)
        self.assertTrue(tobj == Point(5, 9))
        self.assertTrue(tobj == (5, 9))
        self.assertTrue(Point(3, 0) == 3)

        self.assertFalse(tobj == Point())
        self.assertFalse(tobj == Point(15, 9))
        self.assertFalse(tobj == Point(5, 19))
        self.assertFalse(tobj == (5, 19))

        self.assertFalse(tobj == (5, 9, 11))

    def test_repr(self):
        tobj = Point(5, 9)
        r = repr(tobj)
        self.assertTrue(r == 'Point(5,9)')

    def test_str(self):
        tobj = Point(5, 9)
        s = str(tobj)
        self.assertTrue(s == '(5,9)')
        self.assertTrue(f'{tobj}' == '(5,9)')

    def test_add(self):
        p1 = Point(1, 3)
        p2 = Point(5, 9)
        p3 = p1 + p2
        self.assertEqual(Point(6, 12), p3)

        tobj = Point(p1)
        tobj += p2
        self.assertEqual(Point(6, 12), tobj)

        p4 = p1 + (6, 10)
        self.assertEqual(Point(7, 13), p4)

    def test_sub(self):
        p1 = Point(1, 3)
        p2 = Point(5, 9)
        p3 = p2 - p1
        self.assertEqual(Point(4, 6), p3)

        tobj = Point(p2)
        tobj -= p1
        self.assertEqual(Point(4, 6), tobj)

        p4 = p2 - (6, 10)
        self.assertEqual(Point(-1, -1), p4)

    def test_mul(self):
        p1 = Point(1, 3)
        tobj = p1 * 2
        self.assertEqual(Point(2, 6), tobj)
        tobj = p1 * Point(3, 2)
        self.assertEqual(Point(3, 6), tobj)
        tobj = p1 * (2, 3)
        self.assertEqual(Point(2, 9), tobj)
        tobj = -p1
        self.assertEqual(Point(-1, -3), tobj)

    def test_div(self):
        p1 = Point(1, 3)
        tobj = p1 / 2
        self.assertEqual(Point(0.5, 1.5), tobj)
        tobj = p1 / Point(3, 2)
        self.assertEqual(Point(1 / 3, 3 / 2), tobj)

    def test_ng(self):
        p1 = Point(1, 3)
        tobj = -p1
        self.assertEqual(Point(1, 3), p1)
        self.assertEqual(Point(-1, -3), tobj)


class TestRectangle(unittest.TestCase):

    def test_init(self):
        s = Point(1, 3)
        e = Point(5, 9)
        tobj = Rectangle(s, e)
        self.assertEqual(s, tobj.start)
        self.assertEqual(e, tobj.end)

        tobj = Rectangle(e, s)
        self.assertEqual(s, tobj.start)
        self.assertEqual(e, tobj.end)

    def test_init_Rectangle(self):
        oRect = Rectangle((1, 3, 5, 9))
        tobj = Rectangle(oRect)
        self.assertEqual(tobj.start, Point(1, 3))

    def test_init_Points(self):
        tobj = Rectangle(Point(5, 9), Point(1, 3))
        self.assertEqual(tobj.start, Point(1, 3))

        tobj = Rectangle(Point(1, 3))
        self.assertEqual(tobj.start, Point(0, 0))
        self.assertEqual(tobj.end, Point(1, 3))

        tobj = Rectangle(Point(-1, -3))
        self.assertEqual(tobj.end, Point(0, 0))
        self.assertEqual(tobj.start, Point(-1, -3))

    def test_init_list(self):
        tobj = Rectangle((1, 3, 5, 9))
        self.assertEqual(tobj.start, Point(1, 3))

        tobj = Rectangle([1, 3, 5, 9])
        self.assertEqual(tobj.start, Point(1, 3))

        sobj = {1, 3, 5, 9}
        tobj = Rectangle(sobj)
        self.assertEqual(tobj.start, Point(1, 3))

    def test_width(self):
        s = Point(3, 9)
        e = Point(5, 1)
        tobj = Rectangle(s, e)
        self.assertEqual(2, tobj.width)

    def test_height(self):
        s = Point(3, 9)
        e = Point(5, 1)
        tobj = Rectangle(s, e)
        self.assertEqual(8, tobj.height)

    def test_extent(self):
        s = Point(3, 9)
        e = Point(5, 1)
        tobj = Rectangle(s, e)
        self.assertEqual((2, 8), tobj.extent)

    def test_eq(self):
        s = Point(3, 9)
        e = Point(5, 1)
        tobj = Rectangle(s, e)
        self.assertTrue(tobj == Rectangle((3, 1, 5, 9)))
        self.assertTrue(tobj == (3, 1, 5, 9))
        self.assertFalse(tobj == (3, 1, 5, 9, 8))
        self.assertFalse(tobj == [3, 1, 5, 9, 8])
        self.assertFalse(tobj == {3, 1, 5, 9, 8})

    def test_repr(self):
        tobj = Rectangle([1, 3, 5, 9])
        r = repr(tobj)
        self.assertEqual('Rectangle(Point(1,3),Point(5,9))', r)

    def test_str(self):
        tobj = Rectangle([1, 3], [5, 9])
        s = str(tobj)
        self.assertTrue(s == '[(1,3)-(5,9)]')
        self.assertTrue(f'{tobj}' == '[(1,3)-(5,9)]')

    def test_center(self):
        tobj = Rectangle([100, 100], [300, 300])
        center = tobj.center()
        self.assertEqual(Point(200, 200), center)
