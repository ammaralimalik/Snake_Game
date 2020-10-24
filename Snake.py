import random
import curses

def snake():
    s = curses.initscr()
    curses.curs_set(0)
    sw, sh = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    snakeX = sw / 4
    snakeY = sh / 2
    snake = [[snakeY, snakeX], [snakeY, snakeX - 1], [snakeY, snakeX - 2]]
    food = [sh / 2, sw / 2]
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        if next_key == -1:
            key = key
        else:
            key = next_key

        if snake[0][0] in [0, sh] or snake[0][1] in [0, sh] or snake[0] in snake[1:]:
            curses.endwin()
            quit()

        newHead = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            newHead[0] += 1
        elif key == curses.KEY_LEFT:
            newHead[1] -= 1
        elif key == curses.KEY_RIGHT:
            newHead[1] += 1
        elif key == curses.KEY_UP:
            newHead[0] += 1
        elif key == curses.KEY_ENTER:
            quit()

        snake.insert(0, newHead)

        if snake[0] == food:
            food = null
            while food is null:
                nf = [random.randint(1, sh - 1)], [random.randint(1, sw - 1)]
                if nf not in snake:
                    food = nf
                else:
                    food = null

                w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(int(tail[0]), int(tail[1]), ' ')

        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

snake()



