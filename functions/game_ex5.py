import pgzrun
from random import randint

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2, HEIGHT//2))
c = Actor('cookie_img', (randint(0, WIDTH), randint(0, HEIGHT)))
title = "IRON-MAN GAME "
score = 0
music.play('bgm')
music.set_volume(0.5)
def draw():
    screen.fill('white')
    screen.draw.text(title, center=(WIDTH//2, 30),fontsize=60, color='black', align='center',shadow=(.2,1),scolor="red")
    screen.draw.text(f'score: {score}', (10,10), fontsize=10,color='black')
    p.draw()
    c.draw()

def p_move():
    if keyboard.right and p.right < WIDTH:
        p.x +=3
        p.angle = -10
    if keyboard.left and p.left > 0:
        p.x -= 3
        p.angle = 10
    if keyboard.up and p.top > 0:
        p.y -=3
    if keyboard.down and p.bottom < HEIGHT:
        p.y +=3

def update():
    global score #tells python ,to change the value of global variable score
    p_move()
    if p.colliderect(c):
        score +=1
        c.pos = (randint(0, WIDTH), randint(0, HEIGHT))
        sounds.s1.play()
        # sounds.bgm.play()
    print(p.x, p.y, p.angle)

pgzrun.go()
