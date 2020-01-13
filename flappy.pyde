import random
posX = 50
posY = 0
speed= 2
gap_height= 0
def setup():
    size(800,500)
    background(173, 216, 250)

def bird():
    circ()
    triang()
    triang1()
     
def circ():
    fill(255,255,0) 
    circle(50,100,40)
      
def triang():
    fill(255,0,0)
    triangle(50,120,60,100,40 ,100)
  
def triang1():
    fill(255,255,0)
    triangle(65, 102, 87, 92, 64, 84)

def pipe():
    fill(162,143,143)
    rect(800, 0,150+speed, 500)
    
def gap():
    fill(173, 216, 250)
    rect(800,0,150+speed,150)
    stroke(173, 216, 250)      
    
                 
        
def draw():
    global gap_height
    global posY
    global posX
    global speed
    pipe()
    gap()
    posX=posX-speed

     
   
    posY += 1
     #print(mouseX, mouseY)
    bird()
     
    if keyPressed:
        if key == " ":
           posY = posY -  10
             
    if posY > 380:
        posY = 380
        print("game over")
    print(posY)
    pushMatrix()
    translate(0,posY)
    background(173, 216, 250)
    bird()
   
    popMatrix() 
     
    pushMatrix()
    translate(posX,0)
    pipe()
    popMatrix()
    
    pushMatrix()
    translate(posX,gap_height)
    gap()
    popMatrix()
     
