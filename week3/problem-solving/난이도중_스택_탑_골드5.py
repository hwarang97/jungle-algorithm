# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys

input = sys.stdin.readline
times = int(input().rstrip())
arr = [int(str_int) for str_int in input().rstrip().split()]
stack = []
output = []

for i, height in enumerate(arr):
    if not stack:
        output.append(0)
        stack.append((i + 1, height))

    else:
        while stack and stack[-1][1] <= height:
            stack.pop()

        if stack:
            output.append(stack[-1][0])
        else:
            output.append(0)
        stack.append((i + 1, height))


sys.stdout.write(f"{' '.join(map(str, output))}")
