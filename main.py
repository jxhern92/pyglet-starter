import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create some text
label = pyglet.text.Label('Hello, world', x = 250, y = 200)

# Create a sprite
img= pyglet.image.load('assets/hero/Old hero.png')
smol_img = img.get_region(x=14, y=15, width=18, height=19)
img1= pyglet.image.load('assets/hero/sliced/idle-1.png')
img2= pyglet.image.load('assets/hero/sliced/idle-2.png')
img3= pyglet.image.load('assets/hero/sliced/idle-3.png')
img4= pyglet.image.load('assets/hero/sliced/idle-4.png')


def update(dt):
  pass


# Start the event loop
@window.event
def on_draw():
    window.clear()
    label.draw()
    smol_img.blit(100, 150)
    img1.blit(150, 150)
    img2.blit(125, 150)
    img3.blit(175, 150)
    img4.blit(200, 150)
pyglet.clock.schedule(update)
pyglet.app.run()
