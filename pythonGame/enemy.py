import os, pyglet
from pyglet.gl import *

class enemy:
    def __init__(self, resolution, pos = [0, 0]):
        self.image = pyglet.resource.image('sprites/enemy.png')
        self.pos = pos
        self.sprite = pyglet.sprite.Sprite(self.image, x=self.pos[0], y=self.pos[1])
        self.optimal_distance = 10
    def main(self, player):
        pass
    def update_sprite_position(self, camera):
        self.sprite.update(x=(self.pos[0] - int(camera.real_pos[0])), y=(self.pos[1] - int(camera.real_pos[1])))