from PointAndCo import Point


class DragAndDropOperation:
    def __init__(self, owner, startPos):
        self.owner = owner
        self.startPos = Point(startPos)
        print(f'Start Drp on pos={startPos}')

    def on_drag(self, newPos):
        newPos = Point(newPos)
        print(f'Drag to pos={newPos}')

    def on_drop(self, dropPos):
        dropPos = Point(dropPos)
        rPos = self.owner.transposeBack(dropPos)
        print(f'Drop on pos={dropPos}  rPos={rPos}')


class Drp_DrawLine(DragAndDropOperation):
    def __init__(self, owner, startPos, lineObj):
        super().__init__(owner, startPos)

        self.lineObj = lineObj

    def on_drag(self, newPos):
        newPos = Point(newPos)
        sx, sy = self.startPos.xy
        ex, ey = newPos.xy
        self.owner.coords(self.lineObj.widget, sx, sy, ex, ey)

    def on_drop(self, dropPos):
        dropPos = Point(dropPos)
        rPos = self.owner.transposeBack(dropPos)
        print(f'Drop on pos={dropPos}  rPos={rPos}')
        self.lineObj.end = rPos
        self.owner.redraw()
