import game_framework
from pico2d import *
import world_build_state
import main_state


name = "RankingState"
# font = load_font('ENCR10B.TTF', 20)

def enter():
    with open('ranking.json', 'wb') as f:
        json.dumps(main_state.ranking, f)



def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(world_build_state)


def draw():
    clear_canvas()
    for i in range(10):
        print(main_state.ranking[str(i)])
        # font.draw(200, 50 + 50*i, '(Time: %3.2f)' % main_state.ranking[str(i)], (0, 0, 0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

