import _curses
from random import randint
#setup window
_curses.initscr()
win = _curses.newwin(20, 60, 0, 0) # y,x
win.keypad(1)
_curses.noecho()
_curses.curs_set(0)
win.border(0)
win.nodelay(1) 

#snake and food
snake =[(4,10), (4,9), (4,8)]
food = (10,20)

win.addch(food[0], food[1], '#')

ESC = 27
key = _curses.KEY_RIGHT
#game logic
score = 0
while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    
    if key not in [_curses.KEY_LEFT, _curses.KEY_RIGHT, _curses.KEY_UP, _curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate the next corrdinates
    y = snake[0][0]
    x = snake[0][1]
    if key == _curses.KEY_DOWN:
        y += 1
    if key == _curses.KEY_UP:
        y -= 1
    if key == _curses.KEY_LEFT:
        x -= 1
    if key == _curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    #if snake runs over itself
    if snake[0] in snake[1:]: break

    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    win.addch(snake[0][0], snake[0][1], '*')



_curses.endwin()
print(f" Final Score = {score}")