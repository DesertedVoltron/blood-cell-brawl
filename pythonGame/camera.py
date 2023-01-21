import os, pyglet
from math import sqrt

camera_smoothing = 15

class camera:
    def __init__(self, resolution, pos = [0, 0]):
        self.size = resolution
        self.real_pos = [float(pos[0]), float(pos[1])]
    def render_player(self, player):
        player.image.blit(player.pos[0] - int(self.real_pos[0]), player.pos[1] - int(self.real_pos[1]))
    def render_enemy(self, enemy):
        enemy.sprite.draw()
    def render_projectile(self, projectile):
        projectile.image.blit(int(projectile.real_pos[0]) - int(self.real_pos[0]), int(projectile.real_pos[1]) - int(self.real_pos[1]))
    def move(self, focus = [0, 0]):
        # OPTIMIZATION
        # since the real_pos is converted to int when its being drawn
        # check if its the same as focus
        # if it is, then save the program from doing precise math
        if not (int(self.real_pos[0]) == focus[0] and int(self.real_pos[1]) == focus[1]):
            distance = [focus[0] - self.real_pos[0], focus[1] - self.real_pos[1]]
            magnitude = sqrt(distance[0]**2 + distance[1]**2)
            if (magnitude > 0.05):
                self.real_pos[0] += distance[0]/camera_smoothing
                self.real_pos[1] += distance[1]/camera_smoothing