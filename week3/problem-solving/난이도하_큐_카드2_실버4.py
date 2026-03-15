# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
queue = deque([num for num in range(1, n + 1)])

flag = 1
while len(queue) != 1:
    if flag:
        queue.popleft()
        flag = 0

    else:
        queue.append(queue.popleft())
        flag = 1

print(queue[0])
