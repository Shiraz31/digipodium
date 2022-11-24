import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2, HEIGHT//2))

def draw():
    screen.fill('white')
    p.draw()

def p_move():

 def handle_boundary(): 

    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x = WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT

def update():
    print(p.x, p.y, p.angle)

pgzrun.go()