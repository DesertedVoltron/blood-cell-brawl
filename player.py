import pyglet

class player:
    def __init__(self, resolution, pos = [0, 0]):
        self.image = pyglet.resource.image('sprites/playerBlip.png')
        self.pos = pos
        self.speed = 3
        self.health = 1000
        self.damage = 10
        self.vel = [0, 0]

        # CALCULATE MIDDLE OFFSET
        width, height = self.image.width, self.image.height
        self.screen_middle_offset = (resolution[0] // 2 - width // 2, resolution[1] // 2 - height // 2)
        self.middle_offset = (self.image.width/2, self.image.height/2)
        

    
    def move(self, deltaTime):
        self.pos[0] += self.vel[0] * deltaTime
        self.pos[1] += self.vel[1] * deltaTime
    def take_damage(self, amount):
        self.health -= amount
        print('took ' + str(amount) + ' amount of damage.')