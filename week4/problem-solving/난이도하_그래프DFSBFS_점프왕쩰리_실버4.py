# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

import sys


def is_attachable(x, y, n, matrix):
    if x >= n or y >= n or matrix[x][y] == 0:
        return False

    if matrix[x][y] == -1:
        return True

    move_delta = matrix[x][y]
    is_left_attachable = is_attachable(x, y + move_delta, n, matrix)
    is_right_attachable = is_attachable(x + move_delta, y, n, matrix)
    return is_left_attachable or is_right_attachable


input = sys.stdin.readline
n = int(input().rstrip())
matrix = [
    [move_amount for move_amount in map(int, input().rstrip().split())]
    for _ in range(n)
]

output = ""
if is_attachable(0, 0, n, matrix):
    output = "HaruHaru"
else:
    output = "Hing"

sys.stdout.write(output)
