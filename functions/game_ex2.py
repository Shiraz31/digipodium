import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2, HEIGHT//2))

def draw():
    screen.fill('white')
    p.draw()

def p_move():
    '''function to move player'''
    if keyboard.left:
        p.x -= 3
    if keyboard.right:
        p.x +=3
    if keyboard.up:
        p.y -=3
    if keyboard.down:
        p.y +=3
        
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
    p_move()
    handle_boundary()
    print(p.x, p.y, p.angle)

pgzrun.go()
