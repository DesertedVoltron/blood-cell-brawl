import os, pyglet
from pyglet.gl import *
import vector_math
from enemy import enemy

# (health, damage, sprite)

types = {
    "red": (10, 5, 'sprites/red.png'),
    "blue": (50, 5, 'sprites/blue.png'),
    "green": (100, 5, 'sprites/green.png'),
    "yellow": (200, 5, 'sprites/yellow.png'),
    "black": (200, 10, 'sprites/black.png'),
    "pink": (100, 10, 'sprites/pink.png')
}

class linearEnemy(enemy):
    def __init__(self, resolution, player, pos, enemyType):
        super().__init__(resolution, player, pos, pyglet.resource.image(types[enemyType][2]), types[enemyType][0], types[enemyType][1])