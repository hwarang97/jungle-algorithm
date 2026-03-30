# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys

# sys.setrecursionlimit(10000)
input = sys.stdin.readline


def count_min_jump(current, move_amount, destination, memo):
    """
    최소 점프 횟수를 반환하는 함수
    args:
        - current: 현재 위치
        - move_amount: 이동할 칸수
        - destination: 목적지
        - memo: 현재위치에서 이동한 뒤에 N까지 최소 이동거리를 담은 배열
    """
    global flag

    if current > destination:
        return destination

    if memo[current].get(move_amount, -1) != -1:
        return memo[current][move_amount]

    if current == destination:
        flag = True
        return 0

    next_position = current + move_amount

    if next_position in small_rocks:
        return destination

    if move_amount == 1:
        memo[current][move_amount] = 1 + min(
            count_min_jump(next_position, 1, destination, memo),
            count_min_jump(next_position, 2, destination, memo),
        )
        return memo[current][move_amount]

    else:
        memo[current][move_amount] = 1 + min(
            count_min_jump(next_position, move_amount - 1, destination, memo),
            count_min_jump(next_position, move_amount, destination, memo),
            count_min_jump(next_position, move_amount + 1, destination, memo),
        )
        return memo[current][move_amount]


# def count_min_jump_iter(current, move_amount, destination, memo):
#     """
#     최소 점프 횟수를 반환하는 함수
#     args:
#         - current: 현재 위치
#         - move_amount: 이동할 칸수
#         - destination: 목적지
#         - memo: 현재위치에서 이동한 뒤에 N까지 최소 이동거리를 담은 배열
#     """
#     global flag
#     pass


n, k = list(map(int, input().split()))
small_rocks = set()
for _ in range(k):
    small_rocks.add(int(input()))

flag = False
memo = [dict() for _ in range(n + 1)]

# recursion version
num_jump = count_min_jump(1, 1, n, memo)

# iter version
# num_jump = count_min_jump_iter()
if flag:
    print(num_jump)
else:
    print("-1")
