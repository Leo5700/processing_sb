

'''

181220
Перемещаемый квадрат. 
TODO Сделать их 4 шт.

атрибуты ширина/высота, активен/нет
методы перемещение


'''





boxSize = 20
overBox = False
locked = False
dragged = False
xOffset = 0.0
yOffset = 0.0

rects = []

def setup():
    size(640, 360)
    global bx, by
    bx = width / 2.0
    by = height / 2.0
    rectMode(RADIUS)
    noFill()

    # global dragged
    # dragged = False

    # global locked
    # locked = False

    
    rects.append(mr(100, 100, 20, 1, 1, 0, 0))
    rects.append(mr(100, 200, 20, 1, 1, 0, 0))
    rects.append(mr(200, 100, 20, 1, 1, 0, 0))
    rects.append(mr(200, 200, 20, 1, 1, 0, 0))


    # global locked, dragged
    # locked, dragged = False, False

    
def draw():
    global overBox
    
    background(204)
    if bx - boxSize < mouseX < bx + boxSize and by - boxSize < mouseY < by + boxSize:
        overBox = True
    else:
        overBox = False
    rect(bx, by, boxSize, boxSize)
    rect(bx, by, 3, 3)


    for r in rects:
        r.display()
        r.checkOverBox()
        if r.overBox and locked:
            r.checkOffset()
            print(r.overBox, r.overBox)
            print(r.xOffset, r.yOffset)
            if dragged:
                r.bx = mouseX - r.xOffset 
                r.by = mouseY - r.yOffset
        else:
            print('1111111')














def mousePressed():
    global locked
    locked = True
    
def mouseDragged():
    global dragged
    if locked:
        dragged = True
        
def mouseReleased():
    global locked
    locked = False
    # dragged = False
    # print('released')
    # print(locked)


'''
def mousePressed():
    global locked, xOffset, yOffset
    
    if overBox:
        locked = True
    else:
        locked = False
    xOffset = mouseX - bx
    yOffset = mouseY - by
    
def mouseDragged():
    global bx, by

    if locked:
        bx = mouseX - xOffset
        by = mouseY - yOffset
        
def mouseReleased():
    global locked
    locked = False
'''




class mr(object):
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

    def checkOffset(self):
        # if self.overBox:
        #     self.locked = True
        self.xOffset = mouseX - self.bx
        self.yOffset = mouseY - self.by
        # else:
            # self.locked = False
