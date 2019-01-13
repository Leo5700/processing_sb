
# tx, ty, rx, ry, rz = 0, 0, 0, 0, 0


def setup():
    size(640, 360, P3D)
    noStroke()
    fill(204)
    global tx, ty, rx, ry, rz
    tx, ty, rx, ry, rz = 0, 0, 0, 0, 0
    
    global sent, senr
    sent, senr = 2, PI/180

def draw():
    global tx, ty, rx, ry, rz
    
    if keyPressed:
        if key == 'q':
            tx += sent
        if key == 'a':
            tx -= sent
        if key == 'w':
            ty += sent
        if key == 's':
            ty -= sent
        if key == 'e':
            rx += senr
        if key == 'd':
            rx -= senr
        if key == 'r':
            ry += senr
        if key == 'f':
            ry -= senr
        if key == 't':
            rz += senr
        if key == 'g':
            rz -= senr
    
    background(0)
    # lights()
    # fov = PI/3.0; 
    # cameraZ = (height/2.0) / tan(fov/2.0); 
    # perspective(fov, width/height, cameraZ/2, cameraZ*2)
    translate(tx, ty, 0)
    rotateX(rx)
    rotateY(ry)
    rotateZ(rz)
    # fill(100)
    # box(160)
    fill(100)
    rect(0, 0, 40, 40)
    rect(width, height, 40, 40)
    rect(0, 0, width, height)
    rect(-40, -40, 40, 40)
    


'''

Camera
When looking at a 3D scene in a Processing window, we can think of our view of the scene as a camera. Zoom in closer to the objects and we can imagine a camera zooming in. Rotate around the scene and the camera rotates. Of course, there is no actual camera, this is just a convenient device to help us understand how to traverse a 3D scene. Simulating a camera can be done through clever transformations at the beginning of draw() by using translate(), rotate(), and scale() to manipulate our view of the scene. Nevertheless, for convenience there is also a camera() function whose purpose is also to simulate a camera. The function defines a camera as having an "eye position", i.e. the camera location, a scene "center" which tells the camera which way to point, and an upward axis which aligns the camera vertically.

The default camera position is essentially right between your eyes: a location out in front of the window aligned straight up and pointing towards the screen. Here are the numbers for the default position.

Eye position: width/2, height/2, (height/2) / tan(PI/6)
Scene center: width/2, height/2, 0
Upwards axis: 0, 1, 0
When written in code, this looks like:

camera(width/2, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0);

Any of the arguments in the camera() function can be made into a variable to simulate camera movements. For example, by moving the x position of the eye according to the mouse, you can rotate around an object to see it from a different angle.


void setup() {
  size(640, 360, P3D);
}

void draw() {
  background(0);
  camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0);
  translate(width/2, height/2, -100);
  stroke(255);
  noFill();
  box(200);
}

If you move both the eye position and the scene's center according to the mouse, you can create the effect of panning.


void setup() {
  size(640, 360, P3D);
}

void draw() {
  background(0);
  camera(mouseX, height/2, (height/2) / tan(PI/6), mouseX, height/2, 0, 0, 1, 0);
  translate(width/2, height/2, -100);
  stroke(255);
  noFill();
  box(200);
}

'''
