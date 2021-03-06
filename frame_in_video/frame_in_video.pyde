


add_library('video')
import processing.video as pv


from mr import MR


boxSize = 20
overBox = False
dragged = False
rects = []

def setup():
    size(1024, 768)

    global bx, by
    rectMode(RADIUS)
    noFill()

    rects.append(MR(100, 100, 20, 1, 1, 0, 0))
    rects.append(MR(100, 200, 20, 1, 1, 0, 0))
    rects.append(MR(200, 200, 20, 1, 1, 0, 0))
    rects.append(MR(200, 100, 20, 1, 1, 0, 0))
    
    global video
    video = pv.Capture(this, width, height)
    video.start()

    
def draw():  
    # background(204)

    video.read()
    image(video, 0, 0, width, height)


    beginShape()
    for r in rects:
        noFill()
        r.display()
        r.checkOverBox()
        if r.overBox and dragged:
            r.move(mouseX, mouseY)
        vertex(r.bx, r.by)
    fill(100, 255)

    endShape(CLOSE)

    
def mouseDragged():
    global dragged
    dragged = True        

def mouseReleased():
    global dragged
    dragged = False
