from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def moving_curve_3_points(p1, p2, p3):
    global x, y
    global i
    t = i / 100
    x = (2*t**2-3*t+1) * p1[0] + (-4*t**2+4*t)*p2[0] + (2*t**2-t)*p3[0]
    y = (2*t**2-3*t+1) * p1[1] + (-4*t**2+4*t)*p2[1] + (2*t**2-t)*p3[1]

    if i>= 100:
        i = 0
    delay(0.01)
    pass


def moving_curve_4_points(p1, p2, p3, p4):
    global x, y
    global i
    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]


    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2



    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]


def moving_curve_10_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global x,y
    global i
    global turn
    # draw p1-p2
    if turn == 0:
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        if i >= 50:
            i = 0
            turn = 1

    # draw p2-p3
    if turn == 1:
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        if i >= 100:
            i = 50
            turn = 2

    # draw p3-p4
    if turn == 2:
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        if i >= 100:
            i = 0
            turn = 3

    # draw p4-p5
    if turn == 3:
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p4[0] + (-4 * t ** 2 + 4 * t) * p5[0] + (2 * t ** 2 - t) * p6[0]
        y = (2 * t ** 2 - 3 * t + 1) * p4[1] + (-4 * t ** 2 + 4 * t) * p5[1] + (2 * t ** 2 - t) * p6[1]
        if i >= 50:
            i = 0
            turn = 4

    # draw p5-p6
    if turn == 4:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        if i >= 100:
            i = 50
            turn = 5

    # draw p6-p7
    if turn == 5:
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p5[0] + (-4 * t ** 2 + 4 * t) * p6[0] + (2 * t ** 2 - t) * p7[0]
        y = (2 * t ** 2 - 3 * t + 1) * p5[1] + (-4 * t ** 2 + 4 * t) * p6[1] + (2 * t ** 2 - t) * p7[1]
        if i >= 100:
            i = 0
            turn = 6

    # draw p7-p8
    if turn == 6:
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p7[0] + (-4 * t ** 2 + 4 * t) * p8[0] + (2 * t ** 2 - t) * p9[0]
        y = (2 * t ** 2 - 3 * t + 1) * p7[1] + (-4 * t ** 2 + 4 * t) * p8[1] + (2 * t ** 2 - t) * p9[1]
        if i >= 50:
            i = 0
            turn = 7

    # draw p8-p9
    if turn == 7:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        if i >= 100:
            i = 50
            turn = 8

    # draw p9-p10
    if turn == 8:
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p8[0] + (-4 * t ** 2 + 4 * t) * p9[0] + (2 * t ** 2 - t) * p10[0]
        y = (2 * t ** 2 - 3 * t + 1) * p8[1] + (-4 * t ** 2 + 4 * t) * p9[1] + (2 * t ** 2 - t) * p10[1]
        if i >= 100:
            i = 0
            turn = 9

    # draw p10-p1
    if turn == 9:
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p10[0] + (-4 * t ** 2 + 4 * t) * p1[0] + (2 * t ** 2 - t) * p2[0]
        y = (2 * t ** 2 - 3 * t + 1) * p10[1] + (-4 * t ** 2 + 4 * t) * p1[1] + (2 * t ** 2 - t) * p2[1]
        if i >= 50:
            i = 0
            turn = 0



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
i = 0
turn = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    i += 1
    moving_curve_10_points((random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)),
                           (random.randint(0, 1000 + 1), random.randint(0, 800 + 1)))
    delay(0.01)




close_canvas()