# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys

input = sys.stdin.readline
MAX_N = 90


def fibonacci(n, dp):
    if n == 0:
        dp[0] = 0
        return 0

    if n == 1:
        dp[1] = 1
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci(n - 2, dp) + fibonacci(n - 1, dp)
    return dp[n]


n = int(input().rstrip())
dp = [-1] * (MAX_N + 1)
sys.stdout.write(f"{fibonacci(n, dp)}")
