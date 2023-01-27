import os, pyglet
from math import sqrt, atan2, degrees, acos

speed = 5
default_fadeout = 180




class projectile:
    def __init__(self, origin, endPoint, damage = 45):
        self.image = pyglet.resource.image('sprites/projectile1.png')
        self.damage = damage

        ## MATH STUFF
        width, height = self.image.width, self.image.height
        halfWidth = width/2 # get half of the size of the sprite
        halfHeight = height/2

        self.real_pos = [float(origin[0]) - halfWidth, float(origin[1]) - halfHeight]
        line = [endPoint[0] - halfWidth - self.real_pos[0], endPoint[1] - halfHeight - self.real_pos[1]]

        magnitude = sqrt(line[0]**2 + line[1]**2)
        self.unit_vector = (round((line[0] / magnitude), 2) * speed, round((line[1] / magnitude), 2) * speed)
        # ROUNDED OFF TO NEAREST HUNDREDTH TO PREVENT LAG

        self.life = default_fadeout

    def move(self, poplist, index, deltaTime):
        self.real_pos[0] += self.unit_vector[0] * deltaTime
        self.real_pos[1] += self.unit_vector[1] * deltaTime
        self.life -= 1
        if self.life == 0:
            poplist.append(index)
    
    def check_collision(self, enemies, player):
        for i, enemy in enumerate(enemies):
            distance = [enemy.pos[0] + enemy.middle_offset[0] - int(self.real_pos[0]), enemy.pos[1] + enemy.middle_offset[1] - int(self.real_pos[1])]
            magnitude = sqrt(distance[0]**2 + distance[1]**2)
            if magnitude < enemy.middle_offset[0]:
                return i
        return -1
    def check_collision_player(self, player):
        distance = [player.pos[0] + player.middle_offset[0] - int(self.real_pos[0]), player.pos[1] + player.middle_offset[1] - int(self.real_pos[1])]
        magnitude = sqrt(distance[0]**2 + distance[1]**2)
        if magnitude < player.middle_offset[0]:
            return True
        return False