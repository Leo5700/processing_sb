
class MR(object):
    def __init__(self, ibx, iby, iboxSize, ilocked, ioverBox, ixOffset, iyOffset):
        self.bx = ibx
        self.by = iby
        self.boxSize = iboxSize
        self.locked = ilocked
        self.overBox = ioverBox
        self.xOffset = ixOffset
        self.yOffset = iyOffset


    def move(self, posX, posY):
        self.bx = posX
        self.by = posY

    def display(self):
        rect(self.bx, self.by, self.boxSize, self.boxSize)

    def checkOverBox(self):
        if self.bx - self.boxSize < mouseX < self.bx + self.boxSize and self.by - self.boxSize < mouseY < self.by + self.boxSize:
            self.overBox = True
        else:
            self.overBox = False
