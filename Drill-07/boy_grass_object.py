from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.kind = random.randint(0,1)
        if self.kind == 0:
            self.image = load_image('ball21x21.png')
        elif self.kind == 1:
            self.image = load_image('ball41x41.png')
        self.speed = random.randint(2, 10)

    def update(self):
        if self.y >= 70:
            self.y -= self.speed
        elif self.y < 70:
            self.y = 65

    def draw(self):
        if self.kind == 0:
            self.image.clip_draw(0, 0, 21, 21, self.x, self.y)
        elif self.kind == 1:
            self.image.clip_draw(0, 0, 42, 42, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
grass = Grass()

running = True

while running:
    handle_events()
    for ball in balls:
        ball.update()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()