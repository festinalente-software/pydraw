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
