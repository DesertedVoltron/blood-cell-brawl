import os, pyglet


class trail:
    def __init__(self, initial_position, image = pyglet.resource.image('sprites/enemy.png')):
        self.image = image
        self.pos = initial_position
        self.trails = []
    