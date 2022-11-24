import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2, HEIGHT//2))

title = "IRON-MAN GAME "

def draw():
    screen.fill('black')
    screen.draw.text(title, (10,10)centre=(WIDTH//2, 30),fontsize=60,
    color='white', align='center',shadow=(.2,1),scolor="red")
    p.draw()

def p_move():
    '''function to move player'''
    if keyboard.left:
        p.x -=3
        p.angle = 10
    elif keyboard.right:
        p.x += 3
        p.angle = -10


    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x = WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT

def update():
    p_move()
    handle_boundary()
    print(p.x, p.y, p.angle)

pgzrun.go()
