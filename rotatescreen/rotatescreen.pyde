
# tx, ty, rx, ry, rz = 0, 0, 0, 0, 0


def setup():
    size(640, 360, P3D)
    noStroke()
    fill(204)
    global tx, ty, tz, rx, ry, rz
    tx, ty, tz, rx, ry, rz = 0, 0, 0, 0, 0, 0
    
    global dt, dr
    dt, dr = 2, PI/180

def draw():
    global tx, ty, tz, rx, ry, rz
    
    if keyPressed:
        if key == 'd':
            tx += dt

        if key == 'a':
            tx -= dt

        if key == 's':
            ty += dt

        if key == 'w':
            ty -= dt

        if key == 'e':
            tz += dt

        if key == 'q':
            tz -= dt


        if key == 't':
            rx += dr

        if key == 'g':
            rx -= dr

        if key == 'h':
            ry += dr

        if key == 'f':
            ry -= dr

        if key == 'r':
            rz += dr

        if key == 'y':
            rz -= dr
    


    background(0)

    pushMatrix()
    translate(tx, ty, tz)
    rotateX(rx)
    rotateY(ry)
    rotateZ(rz)
    fill(100)
    rect(0, 0, 40, 40)
    rect(width, height, 40, 40)
    rect(0, 0, width, height)
    rect(-40, -40, 40, 40)
    popMatrix()

    fill(200)
    rect(0, 0, 60, 60)

