import os, pyglet
from math import sqrt, sin, cos, tan, radians
from pyglet import shapes

camera_smoothing = 15


default_color1 = (155, 0, 0)
default_color2 = (50, 0, 0)
stripe_scrolling_multiplier = 0.5

filler_size = 50 # add to rectangles

batch = pyglet.graphics.Batch()

default_buffer = 100 

def is_point_in_view(bottom_left_camera, resolution, point):
    return (point[0] >= bottom_left_camera[0] and point[0] <= bottom_left_camera[0] + resolution[0] and point[1] >= bottom_left_camera[1] and point[1] <= bottom_left_camera[1] + resolution[1])

def all_points_in_view(bottom_left_camera, resolution, points):
    for point in points:
        if (not is_point_in_view(bottom_left_camera, resolution, point)):
            return False
    return True

def add_vectors(vector1, vector2):
    return [vector1[0] + vector2[0], vector1[1] + vector2[1]]


class camera:
    def __init__(self, resolution, pos = [0, 0]):

        self.size = resolution
        self.real_pos = [float(pos[0]), float(pos[1])]
        

        background = pyglet.resource.image('sprites/background.png')
        self.sprite = pyglet.sprite.Sprite(background, 0, 0)
        self.sprite.color = default_color1
        

        # STRIPE STUFF
        self.angle = 28 # ANGLE OF STRIPES
        self.rectWidth = 50 # WIDTH OF STRIPES
        reference_index = 1 if self.angle < 45 and self.angle > -45 else 0 # WHICH SIDE IS ADJACENT TO THE MAIN STRIPE
        self.stripe_height = resolution[reference_index] / cos(radians(self.angle)) + default_buffer # THE LENGTH OF THE STRIPE
        self.main_stripe = None
        self.main_stripe_position = None
        self.bottom_left_bound = []


        # THIS FUNCTION IS KIND OF CRINGE BUT IT WORKS FOR NOW
    def do_stripes(self, new_angle, new_width):
        self.angle = new_angle
        self.rectWidth = new_width
        reference_index = 1 if (self.angle % 90) < 45 and (self.angle % 90) > -45 else 0 # WHICH SIDE IS ADJACENT TO THE MAIN STRIPE
        self.stripe_height = self.size[reference_index] / cos(radians(self.angle)) + default_buffer # THE LENGTH OF THE STRIPE
        localRect = pyglet.shapes.Rectangle(self.size[0]/2, self.size[1]/2, self.rectWidth, self.stripe_height, default_color2, batch=batch)
        localPos = [0, 0]
        localRect.anchor_position = (self.rectWidth//2, self.stripe_height//2)
        localRect.rotation = self.angle
        self.main_stripe = localRect
        self.main_stripe_position = localPos
        self.bottom_left_bound = [int(self.real_pos[0]) - self.main_stripe_position[0], int(self.real_pos[1]) - self.main_stripe_position[1]]



    def render_background(self):
        self.sprite.draw()
        #local_stripe_pos = (self.main_stripe_position[0] - int(self.real_pos[0]), self.main_stripe_position[1] - int(self.real_pos[1]))
        #self.main_stripe.position = local_stripe_pos
        #batch.draw()
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
                travel_distance_x = distance[0]/camera_smoothing
                travel_distance_y = distance[1]/camera_smoothing
                self.real_pos[0] += travel_distance_x
                self.real_pos[1] += travel_distance_y