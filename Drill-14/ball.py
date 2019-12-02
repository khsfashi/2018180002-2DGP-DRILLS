import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y = random.randint(0, main_state.background.w), random.randint(30, main_state.background.h)


    def get_bb(self):
        self.cx, self.cy = self.x - main_state.background.window_left, self.y -main_state.background.window_bottom
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def draw(self):
        self.cx, self.cy = self.x - main_state.background.window_left, self.y - main_state.background.window_bottom
        self.image.clip_draw(0, 0, 21, 21, self.cx, self.cy)

        draw_rectangle(*self.get_bb())

    def update(self):
        pass
