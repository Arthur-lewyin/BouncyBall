import pgzrun
import random 

WIDTH = 400
HEIGHT = 400

red = random.randint(0,255)
Green = random.randint(0,255)
Blue = random.randint(0,255)
CLR = (red,Green,Blue)

GRAVITY = 2000.0

class Ball():
    def __init__ (self,initial_x,initual_y):
        self.x=initial_x
        self.y=initual_y
        self.vx=200
        self.vy=0
        self.radius =40


    def drawCircle(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)


ball=Ball(50,100)

def draw():
    screen.clear()
    screen.fill(color = "grey")
    ball.drawCircle()

def update(dt):
    #final velocity formula
    #v=u+(a*t)
    u=ball.vy
    ball.vy =u+(GRAVITY*dt)

    #displacement
    #s=(u+v)/2*t
    ball.y += (u+ball.vy)*0.5*dt
    if ball.y> HEIGHT or ball.y<ball.radius:
        #inelastic collission
        ball.vy = -ball.vy*0.9

    ball.x+=ball.vx*dt
    if ball.x> WIDTH -ball.radius or ball.x<ball.radius:
        ball.vx =- ball.vx
        

def on_key_down(key):
    if key ==keys.UP:
        ball.vy =-500




    

pgzrun.go()