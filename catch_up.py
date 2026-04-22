from pygame import *

window = display.set_mode((1200, 600))
display.set_caption('Догонялки')
background = transform.scale(image.load('43.jpg'), (1200, 600))


sprite1 = transform.scale(image.load('cat.png'), (100, 120))
sprite2 = transform.scale(image.load('3.png'), (100, 100))

x1 = 200
y1 = 250
x2 = 400
y2 = 250

speed = 10
clock = time.Clock()
FPS = 60


game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False


    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 1095:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 495:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 1095:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 495:
        y2 += speed


    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    display.update()
    clock.tick(FPS)