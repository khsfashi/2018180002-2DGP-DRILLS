import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import ranking_state

import world_build_state
from zombie import Zombie

name = "MainState"


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None

ranking = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

def enter():
    # game world is prepared already in world_build_state
    global boy
    boy = world_build_state.get_boy()
    pass

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
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for o in game_world.all_objects():
        if isinstance(o, Zombie):
            if collide(boy, o):
                for i in range(10):
                    if ranking[str(i)] < (get_time() - boy.start_time):
                        for j in range(9, i-1, -1):
                            ranking[str(j)] = ranking[str(j - 1)]
                        ranking[str(i)] = get_time() - boy.start_time

                game_framework.change_state(ranking_state)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






