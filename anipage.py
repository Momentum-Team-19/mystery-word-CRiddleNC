from random import randint
from asciimatics.screen import Screen
import time


def title_screen(screen):
    start_time = time.time()
    center_x = screen.width //2
    center_y = screen.height //2

    while time.time() - start_time < 8:
        screen.print_at('Welcome to GUESS THAT WORD!', center_x - len('Welcome to Guess THAT WORD') // 2, center_y, colour=randint(0, screen.colours - 1), bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()
        time.sleep(0.1)


def win_screen(screen):
    start_time = time.time()
    while time.time() - start_time < 3:
        screen.print_at('VICTORY!', randint(0, screen.width), randint(0, screen.height), colour=randint(0, screen.colours - 1), bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()


def loss_screen(screen):
        start_time = time.time()
        x_position = 0
        y_position = 0 # setting to start at the top
        while time.time() - start_time < 3.5:
            while y_position < 60:
                screen.print_at('YOU LOST!  ' * (screen.width // len('YOU LOST!')),
                                x_position, y_position,
                                colour=Screen.COLOUR_RED,
                                bg=Screen.COLOUR_BLACK)
                # x_position += 1
                y_position += 1 # Adds one to the y_position variable, used in the screen print controls above
                ev = screen.get_key()
                if ev in (ord('Q'), ord('q')):
                    return
                screen.refresh()
                time.sleep(0.1) # slowing down my animation
            else:
                x_position = 0
                y_position = 0


def start_screen(results):
    if results == "":
        Screen.wrapper(title_screen)
    elif results == "win":
        Screen.wrapper(win_screen)
    else:
        Screen.wrapper(loss_screen)