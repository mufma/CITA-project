#!usr/bin/python
import pyglet
window = pyglet.window.Window()
counter=.0

def load_anim():
    arrImages=[]
    for i in range(0,90):
        tmpImg=pyglet.resource.image("test_img"+str(i)+".png")
        arrImages.append(tmpImg)
    return arrImages

def update_frames(dt):
    global counter
    counter=(counter+5*dt)

@window.event
def on_draw():
    print counter
    pyglet.gl.glClearColor(0,0,0,0)
    window.clear()
    frames[int(counter)].blit(-80,-20,0,
                              frames[int(counter)].width,
                              frames[int(counter)].height)

frames = load_anim()
pyglet.clock.schedule_interval(update_frames,1/10.0)
pyglet.app.run()
