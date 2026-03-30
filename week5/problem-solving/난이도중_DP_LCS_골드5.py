# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

import sys

input = sys.stdin.readline


def lcs(a, b, i, j, dp):
    if i >= len(a) or j >= len(b):
        return 0

    elif a[i] == b[j]:
        if dp[i + 1][j + 1] == -1:
            dp[i + 1][j + 1] = lcs(a, b, i + 1, j + 1, dp)
        return 1 + dp[i + 1][j + 1]

    else:
        if dp[i][j + 1] == -1:
            dp[i][j + 1] = lcs(a, b, i + 1, j, dp)

        if dp[i + 1][j] == -1:
            dp[i + 1][j] = lcs(a, b, i, j + 1, dp)

        return max(dp[i][j + 1], dp[i + 1][j])


def lcs_iter(a, b, dp):
    for row in range(1, len(a) + 1):
        for col in range(1, len(b) + 1):
            if a[row - 1] == b[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp[len(a)][len(b)]


a = input().rstrip()
b = input().rstrip()

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

print(lcs_iter(a, b, dp))
