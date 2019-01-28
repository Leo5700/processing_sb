'''
import processing.video.*;

Capture video;

void setup() {
  size(320, 240);
  video = new Capture(this, width, height);
  video.start();  
}

void draw() {
  if (video.available()) {
    video.read();
    image(video, 0, 0, width, height);
  } 
}
'''

# import processing.video

add_library('video')
import processing.video as pv

def setup():
    size(640, 480)
    global video
    video = pv.Capture(this, width, height)
    video.start()

# def movieEvent(m):
    # m.read()
    # video.read()

def draw():
    video.read()
    image(video, 0, 0, width, height)
