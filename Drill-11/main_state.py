import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from brick import Brick

name = "MainState"

boy = None
grass = None
brick = None
balls = []
big_balls = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def intersected_rectangle(collided_Rect, a, b):
    vertical = False
    horizontal = False
    rect1_left, rect1_bottom, rect1_right, rect1_top = a.get_bb()
    rect2_left, rect2_bottom, rect2_right, rect2_top = b.get_bb()

    if rect1_left > rect2_right: return False
    if rect1_right < rect2_left: return False
    if rect1_top < rect2_bottom: return False
    if rect1_bottom > rect2_top: return False

    if rect1_left <= rect2_right and rect1_right >= rect2_left:
        horizontal = True
        collided_Rect[0] = max(rect1_left, rect2_left)
        collided_Rect[2] = min(rect1_right, rect2_right)

    if rect1_top >= rect2_bottom and rect1_bottom <= rect2_top:
        vertical = True
        collided_Rect[3] = min(rect1_top, rect2_top)
        collided_Rect[1] = max(rect1_bottom, rect2_bottom)

    if vertical and horizontal:
        return True
    else:
        return False


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    for ball in balls:
        game_world.add_object(ball, 1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 0)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if intersected_rectangle(boy.collided_Rect, brick, boy):
        boy.intersected_brick()
        boy.set_move_on_brick(brick.get_speed())
    else:
        boy.delta_speed_brick = 0
        if not boy.check_on_brick:
            if not boy.jumping:
                boy.acceleration = 0
            boy.jumping = 1
        else:
            boy.check_on_brick = False

    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)
    for ball in balls:
        if collide(grass, ball):
            ball.stop()
        if collide(brick, ball):
            ball.stop()
            ball.set_move_on_brick(brick.get_speed())
    if collide(grass, boy):
        boy.stop_boy()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






