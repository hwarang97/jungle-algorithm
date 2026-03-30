# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys

input = sys.stdin.readline


def count_combination():
    """
    주어진 동전들로 잔액을 처리하는 경우수를 반환하는 함수
    """
    num_coins = int(input())
    coins = list(map(int, input().split()))
    change = int(input())
    memo = [dict() for _ in range(num_coins)]

    return helper(num_coins - 1, coins, change, memo)


def helper(i, coins, change, memo):
    """
    i번째 이하 동전들만 사용해 잔액을 처리하는 경우수를 반환하는 함수
    """
    if change in memo[i]:
        return memo[i][change]

    if i == 0:
        if change % coins[i] == 0:
            memo[i][change] = 1
        else:
            memo[i][change] = 0
        return memo[i][change]

    k = change // coins[i]
    memo[i][change] = 0
    for j in range(k + 1):
        memo[i][change] += helper(i - 1, coins, change - (j * coins[i]), memo)

    return memo[i][change]


test_time = int(input())
output = []
for _ in range(test_time):
    output.append(str(count_combination()))

print("\n".join(output))
