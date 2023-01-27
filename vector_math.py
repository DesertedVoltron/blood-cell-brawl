import os
from math import sqrt

def distance_between_two_vectors(vector1, vector2):
        distance = [vector1[0] - vector2[0], vector1[1] - vector2[1]]
        return sqrt(distance[0]**2 + distance[1]**2)

def unit_vector(origin, destination):
    distance = [destination[0] - origin[0], destination[1] - origin[1]]
    magnitude = sqrt(distance[0]**2 + distance[1]**2)
    return (round((distance[0] / magnitude), 2), round((distance[1] / magnitude), 2))

def round_to_nearest_half(num):
    return round(num * 2) / 2
