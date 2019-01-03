'''
181220
Перемещаемый квадрат. 
TODO Сделать их 4 шт.

атрибуты ширина/высота, активен/нет
методы перемещение
'''

from mr import MR


boxSize = 20
overBox = False
dragged = False
rects = []

def setup():
    size(640, 360)
    global bx, by
    rectMode(RADIUS)
    noFill()

    rects.append(MR(100, 100, 20, 1, 1, 0, 0))
    rects.append(MR(100, 200, 20, 1, 1, 0, 0))
    rects.append(MR(200, 100, 20, 1, 1, 0, 0))
    rects.append(MR(200, 200, 20, 1, 1, 0, 0))
    
def draw():  
    background(204)

    for r in rects:
        r.display()
        r.checkOverBox()
        if r.overBox and dragged:
            r.move(mouseX, mouseY)
    
def mouseDragged():
    global dragged
    dragged = True        

def mouseReleased():
    global dragged
    dragged = False
    
