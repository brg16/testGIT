import math
import random

import pgzrun
from Player import *
from Enemy import *
from Bullet import *

# Fenstereigenschaften
WIDTH = 1000
HEIGHT = 800
TITLE = "Dead in 16"

# Aktoren
raumschiff = Player(image="raumschiff_gruen.png")
alle_gegner = []
bullets = []


def create_gegner():
    gegner = Enemy(max_x=WIDTH, max_y=HEIGHT)
    alle_gegner.append(gegner)


def move_all():
    raumschiff.move(screen.surface)
    for g in alle_gegner:
        g.move(raumschiff.x, raumschiff.y)
    for b in bullets:
        b.move()


def update():
    move_all()
    for b in bullets[:]:
        if not screen.surface.get_rect().collidepoint(b.x, b.y):
            bullets.remove(b)
    for b in bullets[:]:
        for g in alle_gegner[:]:
            if b.colliderect(g):
                bullets.remove(b)
                alle_gegner.remove(g)
                break
    for g in alle_gegner[:]:
        if g.collidepoint(raumschiff.x, raumschiff.y):
            raumschiff.HP -= 1
            alle_gegner.remove(g)


def draw():
    screen.clear()
    raumschiff.draw(screen)
    for g in alle_gegner:
        g.draw()
    for b in bullets:
        b.draw()


def on_key_down(key):
    if key == keys.D:
        raumschiff.dir_x += 1
    elif key == keys.A:
        raumschiff.dir_x -= 1
    elif key == keys.W:
        raumschiff.dir_y -= 1
    elif key == keys.S:
        raumschiff.dir_y += 1


def on_key_up(key):
    if key == keys.D:
        raumschiff.dir_x -= 1
    elif key == keys.A:
        raumschiff.dir_x += 1
    elif key == keys.W:
        raumschiff.dir_y += 1
    elif key == keys.S:
        raumschiff.dir_y -= 1


def on_mouse_move(pos):
    raumschiff.angle = raumschiff.angle_to(pos)


def on_mouse_down():
    bullet = Bullet(image='laser_fire.png', x=raumschiff.x, y=raumschiff.y, angle=raumschiff.angle)
    bullets.append(bullet)


clock.schedule_interval(create_gegner, 1)

pgzrun.go()
