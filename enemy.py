import os, pyglet
from pyglet.gl import *
import vector_math
from projectile import projectile

class enemy:
    def __init__(self, resolution, player, pos = [0, 0], image = pyglet.resource.image('sprites/green.png'), health = 100, damage = 45, optimal_distance = 100, cooldown = 60):
        self.image = image
        self.real_pos = pos[:]
        self.pos = pos[:]
        self.sprite = pyglet.sprite.Sprite(self.image, x=self.pos[0], y=self.pos[1])
        self.damage = damage

        self.default_cooldown = cooldown
        self.cooldown = self.default_cooldown
        self.health = health
        self.optimal_distance = optimal_distance

        self.target = player.pos[:]
        self.velocity = vector_math.unit_vector(self.pos, self.target)
        
        width, height = self.image.width, self.image.height
        self.middle_offset = (self.image.width/2, self.image.height/2)
    def main(self, player, enemy_projectiles):
        if (not vector_math.distance_between_two_vectors(self.pos, player.pos) <= self.optimal_distance):
            if (not vector_math.distance_between_two_vectors(self.target, player.pos) <= 1):
                self.target = player.pos[:]
                self.velocity = vector_math.unit_vector(self.pos, self.target)
            self.real_pos[0] += vector_math.round_to_nearest_half(self.velocity[0])
            self.real_pos[1] += vector_math.round_to_nearest_half(self.velocity[1])
            self.pos[0] = int(self.real_pos[0])
            self.pos[1] = int(self.real_pos[1])

        self.cooldown -= 1
        if self.cooldown == 0:
            self.cooldown = self.default_cooldown
            proj = projectile([self.real_pos[0] + self.middle_offset[0], self.real_pos[1] + self.middle_offset[1]], [player.pos[0] + player.vel[0] + player.middle_offset[0], player.pos[1] + player.vel[1] + player.middle_offset[1]], self.damage)
            enemy_projectiles.append(proj)

    def update_sprite_position(self, camera):
        self.sprite.update(x=(self.pos[0] - int(camera.real_pos[0])), y=(self.pos[1] - int(camera.real_pos[1])))
    def take_damage(self, num_damage, pop_list, index):
        self.health -= num_damage
        if self.health <= 0:
            pop_list.append(index)