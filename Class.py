# Class, object.
class Cube():
    # Method init.
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    # Method - function inside class.
    def move(self, speedx, speedy):
        self.posx += speedx
        self.posy += speedy

# xyz is new object - Cube class.
x = Cube(9,30)

x.move(-4,20)
print(x.posx,x.posy)