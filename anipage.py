from random import randint
from asciimatics.screen import Screen


def demo(screen):
    # start_time = time.time()

    while True:
        screen.print_at('VICTORY!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()


def start_screen():
    Screen.wrapper(demo)