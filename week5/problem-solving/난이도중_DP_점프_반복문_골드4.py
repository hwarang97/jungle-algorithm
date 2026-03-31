# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys

from math import sqrt
from math import ceil

input = sys.stdin.readline


def count_min_jump(start, destination, memo, small_rocks):
    """
    최소 점프 횟수를 반환하는 함수
    args:
        - start: 출발 위치
        - destination: 목적지
        - memo: 시작점부터 현재위치까지 최소 이동거리를 저장한 배열
    """

    for current in range(start, destination + 1):
        amount = ceil((sqrt(1 + 8 * current) - 1) / 2)
        for jump_amount in range(1, amount + 1):
            next_position = current + jump_amount
            if next_position <= destination and next_position not in small_rocks:
                memo[next_position] = min(memo[next_position], 1 + memo[current])


n, k = list(map(int, input().split()))
small_rocks = set()
for _ in range(k):
    small_rocks.add(int(input()))

memo = [i - 1 for i in range(n + 1)]

count_min_jump(1, n, memo, small_rocks)
if memo[n] == 0:
    print("-1")
else:
    print(memo[n])
