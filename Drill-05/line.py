from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global ch_x, ch_y
    global turn
    global start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            if ch_x > x:
                turn = 0
            elif ch_x < x:
                turn = 1
            for i in range(0, 100 + 1, 2):
                t = 1 / 100
                ch_x = (1-t) * ch_x + t * x
                ch_y = (1-t) * ch_y + t * y
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
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(x, y)
    character.clip_draw(frame * 100, 100 * turn, 100, 100, ch_x, ch_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()