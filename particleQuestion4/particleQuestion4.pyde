import random
import particle


def setup():
    global Balls
    Balls = []
    for i in range (10): 
        Ball = particle.Particle()
        Balls.append(Ball)
        
       
    size(800,400)
    background(0)
     
  
def draw():
    background(0)
    stroke(220,45,86) 
    global Balls
    for i in range(len(Balls)):
        Ball = Balls[i]
        Ball.draw_it()
        Ball.move()
        for j in range (10): 
            line (Ball.pos_x, Ball.pos_y, Balls[j].pos_x, Balls[j].pos_y)
