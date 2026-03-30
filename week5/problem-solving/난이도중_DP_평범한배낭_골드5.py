# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline

n, weight_limit = list(map(int, input().split()))
items = [list(map(int, input().split())) for _ in range(n)]
items.sort(key=lambda x: x[0], reverse=True)
dp = [0 for _ in range(weight_limit + 1)]

for weight, value in items:
    for num in range(weight_limit, 0, -1):
        if weight > num:
            break
        dp[num] = max(dp[num], value + dp[num - weight])

print(dp[-1])
