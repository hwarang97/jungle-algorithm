# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

n = int(input())
arr = [int(str_int) for str_int in input().split()]
visited = [False for _ in range(n)]
maxima = 0


def calculate(arr):  # O(n)
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])

    return total


def dfs(current, c):  # O(n! * n)
    global maxima

    if c == n:
        maxima = max(calculate(current), maxima)
        return

    for i in range(n):
        if not visited[i]:
            current.append(arr[i])
            visited[i] = True
            dfs(current, c + 1)
            current.pop()
            visited[i] = False


dfs([], 0)
print(maxima)
