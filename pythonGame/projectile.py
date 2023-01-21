import os, pyglet
from math import sqrt

speed = 5
default_fadeout = 180

class projectile:
    def __init__(self, origin, endPoint, from_player = True):
        self.image = pyglet.resource.image('sprites/projectile1.png')


        ## MATH STUFF
        width, height = self.image.width, self.image.height
        halfWidth = width/2 # get half of the size of the sprite
        halfHeight = height/2

        self.real_pos = [float(origin[0]) - halfWidth, float(origin[1]) - halfHeight]
        line = [endPoint[0] - halfWidth - self.real_pos[0], endPoint[1] - halfHeight - self.real_pos[1]]
        magnitude = sqrt(line[0]**2 + line[1]**2)
        self.unit_vector = (round((line[0] / magnitude), 2) * speed, round((line[1] / magnitude), 2) * speed)
        # ROUNDED OFF TO NEAREST HUNDREDTH TO PREVENT LAG

        self.is_player_target = not from_player

        self.life = default_fadeout

    def move(self, poplist, index, deltaTime):
        self.real_pos[0] += self.unit_vector[0] * deltaTime
        self.real_pos[1] += self.unit_vector[1] * deltaTime
        self.life -= 1
        if self.life == 0:
            poplist.append(index)
        return poplist