from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global ch_x, ch_y
    global turn
    global start
    global i
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            start = 0
            i = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        if event.type == SDL_MOUSEBUTTONDOWN:
            start = 0
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            if ch_x > x:
                turn = 0
            elif ch_x < x:
                turn = 1
            start = 1
    pass

def character_moving(p1, p2):
    global ch_x, ch_y
    global i
    global start

    t = i / 100
    ch_x = (1 - t) * p1[0] + t * p2[0]
    ch_y = (1 - t) * p1[1] + t * p2[1]
    delay(0.01)
    if i >= 100:
        start = 0
        i = 0
pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ch_x, ch_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
turn = 1
i = 0
start = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(x + 17, y - 25)
    character.clip_draw(frame * 100, 100 * turn, 100, 100, ch_x, ch_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    if start == 1:
        i += 1
        character_moving((ch_x, ch_y), (x, y))


close_canvas()