from pico2d import *
import game_world
import game_framework

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.brick_speed = 300, 180, 200
        self.dir = 1

    def get_bb(self):
       return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.dir * self.brick_speed * game_framework.frame_time
        if self.x > 1600 - 90:
            self.dir = -1
        elif self.x < 0 + 90:
            self.dir = 1

    def stop(self):
        self.fall_speed = 0

    def get_speed(self):
        return self.dir * self.brick_speed * game_framework.frame_time