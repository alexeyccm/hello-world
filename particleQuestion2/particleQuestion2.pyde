import random
import particle


def setup():
    global Pieces
    Pieces = []
    for i in range (1): 
        Piece = particle.Particle()
        Pieces.append(Piece)
    size(400,400)
    background(0)
    
def draw():
    background(0)
    stroke(255)
    global Pieces
    for i in range(len(Pieces)):
        Piece = Pieces[i]
        Piece.draw_it()
        Piece.move()  
