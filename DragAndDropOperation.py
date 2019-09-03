from PointAndCo import Point

import logging
logger = logging.getLogger(__name__)

class DragAndDropOperation:
    def __init__(self, owner, startPos):
        self.owner = owner
        self.startPos = Point(startPos)
        logger.debug (f'Start Drp on pos={startPos}')

    def on_drag(self, newPos):
        newPos = Point(newPos)
        logger.debug (f'Drag to pos={newPos}')

    def on_drop(self, dropPos):
        dropPos = Point(dropPos)
        rPos = self.owner.transposeBack(dropPos)
        logger.debug (f'Drop on pos={dropPos}  rPos={rPos}')


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
        logger.debug (f'Drop on pos={dropPos}  rPos={rPos}')
        self.lineObj.end = rPos
        self.owner.redraw()


class Drp_MoveObject(DragAndDropOperation):
    def __init__(self, owner, startPos, selectedObj):
        super().__init__(owner, startPos)

        self.selectedObj = selectedObj
        self.widget = self.selectedObj.widget
        self.coords = self.owner.coords(self.widget)

    def on_drag(self, newPos):
        newPos = Point(newPos)
        sx, sy = self.startPos.xy
        nx, ny = newPos.xy
        dx, dy = nx - sx, ny - sy
        ncoords = [n + (dx if (i % 2 == 0) else dy) for i, n in enumerate(self.coords)]
        self.owner.coords(self.widget, *ncoords)

    def on_drop(self, dropPos):
        dropPos = Point(dropPos)
        rstart = self.owner.transposeBack(self.startPos)
        rdrop = self.owner.transposeBack(dropPos)
        delta = rdrop - rstart
        self.selectedObj.moveBy(delta)
        self.owner.redraw()
