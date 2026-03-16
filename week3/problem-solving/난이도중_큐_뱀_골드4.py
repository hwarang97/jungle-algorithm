# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

import sys
from collections import deque


def is_collision_with_wall(snake, n):
    x, y = snake[0]
    if x <= 0 or x > n or y <= 0 or y > n:
        return True
    else:
        return False


def is_collision_with_self(snake, body):
    if snake[0] in body:
        return True
    else:
        return False


def is_apple(snake, apples):
    if snake[0] in apples:
        apples.remove(snake[0])
        return True
    else:
        return False


def change_direction(time, turn, direction):
    command = turn[time]
    if command == "D":
        return (direction[1], -direction[0])

    elif command == "L":
        return (-direction[1], direction[0])

    else:
        return


def move_head(snake, body, direction):
    x, y = snake[0]
    body.add((x, y))
    delta_x, delta_y = direction
    new_head = (x + delta_x, y + delta_y)
    snake.appendleft(new_head)


def move_tail(snake, body):
    tail = snake.pop()
    body.remove(tail)


input = sys.stdin.readline
n = int(input().rstrip())
apples = set([tuple(map(int, input().split())) for _ in range(int(input().rstrip()))])

turn = dict()
for _ in range(int(input().rstrip())):
    time, ch = input().rstrip().split()
    turn[int(time)] = ch

snake = deque()
snake.appendleft((1, 1))
body = set()
direction = (0, 1)

time = 0
while True:
    time += 1
    move_head(snake, body, direction)
    # print(snake[0])
    if is_collision_with_wall(snake, n) or is_collision_with_self(snake, body):
        break

    if not is_apple(snake, apples):
        move_tail(snake, body)

    if time in turn:
        direction = change_direction(time, turn, direction)


sys.stdout.write(f"{time}")
