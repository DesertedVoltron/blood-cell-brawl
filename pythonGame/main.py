import os, pyglet
from player import player
from camera import camera
from enemy import enemy
from projectile import projectile

resolution = (800, 600)
window = pyglet.window.Window(resolution[0], resolution[1])
window.config.alpha_size = 8

physics_framerate = 60

background = pyglet.resource.image('sprites/background.png')

enemy1 = enemy(resolution, [-100, 100])
enemy2 = enemy(resolution, [100, 200])
enemies = [enemy1, enemy2]

player = player(resolution, [0, 0])
camera = camera(resolution, [player.pos[0] - player.screen_middle_offset[0], player.pos[1] - player.screen_middle_offset[1]])

projectiles = []

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        player.vel[1] += player.speed
    elif symbol == pyglet.window.key.S:
        player.vel[1] -= player.speed
    elif symbol == pyglet.window.key.D:
        player.vel[0] += player.speed
    elif symbol == pyglet.window.key.A:
        player.vel[0] -= player.speed

@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        player.vel[1] -= player.speed
    elif symbol == pyglet.window.key.S:
        player.vel[1] += player.speed
    elif symbol == pyglet.window.key.D:
        player.vel[0] -= player.speed
    elif symbol == pyglet.window.key.A:
        player.vel[0] += player.speed

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        proj = projectile((player.pos[0] + player.middle_offset[0], player.pos[1] + player.middle_offset[1]), (x + camera.real_pos[0], y + camera.real_pos[1]))
        projectiles.append(proj)

@window.event
def on_draw(): # draw stuff here
    window.clear() # clear window before drawing
    background.blit(0, 0)
    for projectile in projectiles:
        camera.render_projectile(projectile)
    camera.render_player(player)
    for enemy in enemies:
        camera.render_enemy(enemy)

def update(dt): # handle physics here
    delta = round(dt * physics_framerate, 3) # rounded for optimization purposes
    # first handle movement
    player.move(delta)
    camera.move((player.pos[0] - player.screen_middle_offset[0], player.pos[1] - player.screen_middle_offset[1]))
    global projectiles
    poplist = []
    for i, projectile in enumerate(projectiles):
        poplist = projectile.move(poplist, i, delta)
    for index in poplist:
        projectiles.pop(index)
    # update sprites
    for enemy in enemies:
        enemy.update_sprite_position(camera)
    # now collision

pyglet.clock.schedule_interval(update, 1/physics_framerate)

pyglet.app.run()