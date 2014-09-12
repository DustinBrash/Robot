__name__ = "Projectile"
import math
import Vector

class Projectile(object):

    def __init__(self, velocity, theta, init_height):
        self.direction = theta
        self.magnitude = velocity
        rad = math.radians(theta)
        self.coord = Vector.Vector(math.cos(rad) * velocity, math.sin(rad) * velocity)
        self.y0 = init_height
        v0 = self.coord.y
        a = -9.81 #meters/second^2
        self.max_height = (-(self.coord.y ** 2)) / (2 * a) + self.y0
        self.max_dist = self.coord.x * -2 * self.coord.y / a
        
    def __repr__(self):
        s = "%f m/s @ %f degrees" % (float(self.magnitude), float(self.direction))
        return s

a = Projectile(10, 45, 1)


    
