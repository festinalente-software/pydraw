import unittest

from DrawingContext import DrawingContext
from PointAndCo import Point, Rectangle


class TestDrawingContext(unittest.TestCase):

    def test_init_simple(self):
        src = Rectangle([0, 0, 200, 100])
        dst = Rectangle([0, 0, 200, 100])
        tobj = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(0, 0), tobj.o_translate())
        self.assertEqual(Point(0, 0), tobj.t_translate())
        self.assertEqual(1, tobj.scale())

        src = Rectangle([0, 0, 200, 100])
        dst = Rectangle([0, 0, 300, 100])
        tobj = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(0, 0), tobj.o_translate())
        self.assertEqual(Point(50, 0), tobj.t_translate())
        self.assertEqual(1, tobj.scale())

        src = Rectangle([0, 0, 200, 100])
        dst = Rectangle([0, 0, 200, 200])
        tobj = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(0, 0), tobj.o_translate())
        self.assertEqual(Point(0, 50), tobj.t_translate())
        self.assertEqual(1, tobj.scale())

    def test_init_simple_border(self):
        src = Rectangle([0, 0, 200, 100])
        dst = Rectangle([0, 0, 200, 100])
        tobj = DrawingContext(src, dst, border=0.05)
        self.assertEqual(Point(0, 0), tobj.o_translate())
        self.assertEqual(Point(10, 5), tobj.t_translate())
        self.assertEqual(0.9, tobj.scale())

        src = Rectangle([0, 0, 200, 100])
        dst = Rectangle([0, 0, 300, 100])
        tobj = DrawingContext(src, dst, border=0.05)
        self.assertEqual(Point(0, 0), tobj.o_translate())
        self.assertEqual(Point(60, 5), tobj.t_translate())
        self.assertEqual(0.9, tobj.scale())

        src = Rectangle([0, 0, 200, 100])
        dst = Rectangle([0, 0, 200, 200])
        tobj = DrawingContext(src, dst, border=0.05)
        self.assertEqual(Point(0, 0), tobj.o_translate())
        self.assertEqual(Point(10, 55), tobj.t_translate())
        self.assertEqual(0.9, tobj.scale())

    def test_init_src_translated(self):
        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([0, 0, 200, 100])
        tobj = DrawingContext(src, dst)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(0, 0), tobj.t_translate())
        self.assertEqual(1, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([0, 0, 200, 100])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(50, 25), tobj.t_translate())
        self.assertEqual(0.5, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([0, 0, 2000, 1000])
        tobj = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(0, 0), tobj.t_translate())
        self.assertEqual(10, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([0, 0, 2000, 1000])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(500.0, 250.0), tobj.t_translate())
        self.assertEqual(5, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([0, 0, 2000, 100])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(950.0, 25.0), tobj.t_translate())
        self.assertEqual(0.5, tobj.scale())

    def test_init_srcUdst_translated(self):
        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 200, 100])
        tobj = DrawingContext(src, dst)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(15.0, 10.0), tobj.t_translate())
        self.assertEqual(0.9, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 200, 100])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(60.0, 32.5), tobj.t_translate())
        self.assertEqual(0.45, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 2000, 1000])
        tobj = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(15.0, 10.0), tobj.t_translate())
        self.assertEqual(9.9, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 2000, 1000])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(510.0, 257.5), tobj.t_translate())
        self.assertEqual(4.95, tobj.scale())

        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 2000, 100])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(960.0, 32.5), tobj.t_translate())
        self.assertEqual(0.45, tobj.scale())

    def test_transpose(self):
        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 210, 110])
        ctx = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(10, 10), ctx.transpose(Point(100, 100)))
        self.assertEqual(Point(210, 110), ctx.transpose(Point(300, 200)))

        ctx = DrawingContext(src, dst, border=0.1)
        self.assertEqual(Point(30, 20), ctx.transpose(Point(100, 100)))
        self.assertEqual(Point(190, 100), ctx.transpose(Point(300, 200)))

        ctx = DrawingContext(src, dst, border=0.5)
        self.assertEqual(Point(110, 60), ctx.transpose(Point(100, 100)))
        self.assertEqual(Point(110, 60), ctx.transpose(Point(300, 200)))

        ctx = DrawingContext(src, dst, border=1)
        self.assertEqual(Point(210, 110), ctx.transpose(Point(100, 100)))
        self.assertEqual(Point(10, 10), ctx.transpose(Point(300, 200)))

    def test_transpose_back(self):
        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 210, 110])
        ctx = DrawingContext(src, dst, border=0)
        self.assertEqual(Point(100, 100), ctx.transposeBack(Point(10, 10)))
        self.assertEqual(Point(300, 200), ctx.transposeBack(Point(210, 110)))

        for src in [Point(100, 100), Point(300, 200)]:
            self.assertEqual(src, ctx.transposeBack(ctx.transpose(src)))

        ctx = DrawingContext(src, dst, border=0.1)
        for src in [Point(100, 100), Point(300, 200)]:
            self.assertEqual(src, ctx.transposeBack(ctx.transpose(src)))

        ctx = DrawingContext(src, dst, border=0.5)
        for src in [Point(100, 100), Point(300, 200)]:
            self.assertEqual(src, ctx.transposeBack(src))

        ctx = DrawingContext(src, dst, border=1)
        for src in [Point(100, 100), Point(300, 200)]:
            p = ctx.transposeBack(ctx.transpose(src))
            x, y = round(p.x), round(p.y)
            self.assertEqual(src, Point(x, y))


    def test_repr(self):
        src = Rectangle([100, 100, 300, 200])
        dst = Rectangle([10, 10, 2000, 100])
        tobj = DrawingContext(src, dst, border=0.25)
        self.assertEqual(Point(-100, -100), tobj.o_translate())
        self.assertEqual(Point(960.0, 32.5), tobj.t_translate())
        self.assertEqual(0.45, tobj.scale())

        s_ref = 'DrawingContext(orig=Rectangle(Point(100,100),Point(300,200)),target=Rectangle(Point(10,10),Point(2000,100)),border=0.25)'
        self.assertEqual(s_ref, repr(tobj))

        s_ref = '(orig=Rectangle(Point(100,100),Point(300,200)),target=[(10,10)-(2000,100)],border=0.25) -> o_translate=(-100,-100),scale=0.45,t_translate=(960.0,32.5)'
        self.assertEqual(s_ref, str(tobj))

