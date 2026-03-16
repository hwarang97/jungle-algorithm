# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

import sys

input = sys.stdin.readline

n = int(input().rstrip())
matrix = [[int(str_int) for str_int in input().rstrip().split()] for _ in range(n)]
white = 0
blue = 0


def dfs(matrix, row_s, row_e, col_s, col_e):
    global white
    global blue

    matrix_sum = get_sum(matrix, row_s, row_e, col_s, col_e)
    if matrix_sum == (row_e - row_s) ** 2:
        blue += 1
        return

    if matrix_sum == 0:
        white += 1
        return

    row_half = row_s + (row_e - row_s) // 2
    col_half = col_s + (col_e - col_s) // 2
    dfs(matrix, row_s, row_half, col_s, col_half)
    dfs(matrix, row_s, row_half, col_half, col_e)
    dfs(matrix, row_half, row_e, col_s, col_half)
    dfs(matrix, row_half, row_e, col_half, col_e)


def get_sum(matrix, row_s, row_e, col_s, col_e):  # O(n^2)
    acc = 0
    for row in range(row_s, row_e):
        for col in range(col_s, col_e):
            acc += matrix[row][col]

    return acc


dfs(matrix, 0, n, 0, n)
sys.stdout.write(f"{white}\n{blue}")
