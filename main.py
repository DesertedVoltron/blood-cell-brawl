import os, pyglet
from player import player
from camera import camera
from linear import linearEnemy
from projectile import projectile
from waves import waves
from random import randint

resolution = (800, 600)
window = pyglet.window.Window(resolution[0], resolution[1])
window.config.alpha_size = 8
clock = pyglet.clock

physics_framerate = 60

wave_text = pyglet.text.Label('Wave: 1', font_name='Arial', font_size=36, x=10, y=550)
health_text = pyglet.text.Label('Health: 1000', font_name='Arial', font_size=16, x=10, y=10)
background = pyglet.resource.image('sprites/background.png')


player = player(resolution, [0, 0])

enemies = []

camera = camera(resolution, [player.pos[0] - player.screen_middle_offset[0], player.pos[1] - player.screen_middle_offset[1]])
camera.do_stripes(150, 50)

player_projectiles = []
enemy_projectiles = []

current_wave = 1

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
        proj = projectile((player.pos[0] + player.middle_offset[0], player.pos[1] + player.middle_offset[1]), (x + camera.real_pos[0], y + camera.real_pos[1]), player.damage)
        player_projectiles.append(proj)

@window.event
def on_draw(): # draw stuff here
    window.clear() # clear window before drawing
    #background.blit(0, 0)
    camera.render_background()
    for projectile in player_projectiles:
        camera.render_projectile(projectile)
    for projectile in enemy_projectiles:
        camera.render_projectile(projectile)
    camera.render_player(player)
    for enemy in enemies:
        camera.render_enemy(enemy)
    # NOW GUI ELEMENTS
    wave_text.draw()
    health_text.draw()


def update(dt): # handle physics here
    delta = round(dt * physics_framerate, 3) # rounded for optimization purposes
    # first handle movement
    player.move(delta)
    camera.move((player.pos[0] - player.screen_middle_offset[0], player.pos[1] - player.screen_middle_offset[1]))
    global player_projectiles
    global enemy_projectiles
    poplist = []
    for i, projectile in enumerate(player_projectiles):
        projectile.move(poplist, i, delta)
    for index in reversed(poplist):
        player_projectiles.pop(index)
    poplist = []
    for i, projectile in enumerate(enemy_projectiles):
        projectile.move(poplist, i, delta)
    for index in reversed(poplist):
        enemy_projectiles.pop(index)
    # update sprites
    for enemy in enemies:
        enemy.main(player, enemy_projectiles)
        enemy.update_sprite_position(camera)
    # now collision
    poplist = []
    enemy_poplist = []
    for i, projectile in enumerate(player_projectiles):
        check = projectile.check_collision(enemies, player)
        if not check == -1:
            poplist.append(i)
            enemies[check].take_damage(projectile.damage, enemy_poplist, check)
    for index in reversed(poplist):
        player_projectiles.pop(index)
    for index in reversed(enemy_poplist):
        enemies.pop(index)
    
    poplist = []
    for i, projectile in enumerate(enemy_projectiles):
        check = projectile.check_collision_player(player)
        if check:
            poplist.append(i)
            player.take_damage(projectile.damage)
            health_text.text = 'Health: ' + str(player.health)
    for index in reversed(poplist):
        enemy_projectiles.pop(index)

def next_wave(dt):
    global current_wave
    current_wave += 1
    wave_text.text = 'Wave: ' + str(current_wave)

def spawn_enemy(dt, enemy_type):
    enemies.append(linearEnemy(resolution, player, [player.pos[0] + randint(-300, 300), player.pos[1] + randint(-300, 300)], enemy_type))


time_passed = 0
for i in range(1, len(waves) + 1):
    for spawn in waves[i]:
        time_passed += spawn[1]
        pyglet.clock.schedule_once(spawn_enemy, time_passed, enemy_type=spawn[0])
    clock.schedule_once(next_wave, time_passed)
    

clock.schedule_interval(update, 1/physics_framerate)

pyglet.app.run()