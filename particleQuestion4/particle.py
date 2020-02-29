class Particle:
    def __init__(self):
        self.pos_x = random(0, width)
        self.pos_y = random(0, height)
        self.speed_x = random(-5, 5)
        self.speed_y = random(-5, 5)
        
    def move(self):
        self.pos_x = self.pos_x + self.speed_x
        self.pos_y = self.pos_y + self.speed_y
        if self.pos_x < 0:
            self.pos_x = width
        if self.pos_x > width:
            self.pos_x = 0
        if self.pos_y < 0:
            self.pos_y = height
        if self.pos_y > height:
            self.pos_y = 0  
            
    def draw_it(self):
        fill(125,185,30)
        circle(self.pos_x, self.pos_y, 10)
                  
        
