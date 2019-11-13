import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
        self.collided_Rect = [0, 0, 0, 0]
        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.delta_speed_brick = 0.0

    def get_bb(self):
       return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        self.x += self.delta_speed_brick

    def stop(self):
        self.fall_speed = 0
        self.delta_speed_brick = 0

    def intersected_brick(self):
        self.collided_Rect_Height = self.collided_Rect[3] - self.collided_Rect[1]
        self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]
        if self.collided_Rect_Width > self.collided_Rect_Height:
            if self.collided_Rect[3] == self.y + 10:
                self.y -= self.collided_Rect_Height
                self.fall_speed = 0
            elif self.collided_Rect[1] == self.y - 10:
                self.y += self.collided_Rect_Height
        else:
            if self.collided_Rect[0] == self.x - 10:
                self.x += self.collided_Rect_Width
            elif self.collided_Rect[2] == self.x + 10:
                self.x -= self.collided_Rect_Width

    def set_move_on_brick(self, speed):
        self.delta_speed_brick = speed


class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)
        self.collided_Rect = [0, 0, 0, 0]
        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.delta_speed_brick = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def intersected_brick(self):
        self.collided_Rect_Height = self.collided_Rect[3] - self.collided_Rect[1]
        self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]
        if self.collided_Rect_Width < self.collided_Rect_Height:
            if self.collided_Rect[3] == self.y + 20:
                self.y -= self.collided_Rect_Height
            elif self.collided_Rect[1] == self.y - 20:
                self.y += self.collided_Rect_Height
                self.fall_speed = 0
        else:
            if self.collided_Rect[2] == self.x - 20:
                self.x -= self.collided_Rect_Width
            elif self.collided_Rect[0] == self.x + 20:
                self.x += self.collided_Rect_Width

    def set_move_on_brick(self, speed):
        self.delta_speed_brick = speed