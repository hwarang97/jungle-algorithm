# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

import sys
from collections import deque


def make_adj_dict(arr, num_com):
    "인접 리스트를 반화하는 함수"
    adj_dict = {com: [] for com in range(num_com + 1)}
    for source, destination in arr:
        adj_dict[source].append(destination)
        adj_dict[destination].append(source)

    return adj_dict


def count_virus_com():
    "감염된 컴퓨터 수를 반환하는 함수"
    queue = deque()
    visited = [False] * (num_com + 1)

    # 1번 컴퓨터는 반드시 감염, 1번은 카운트 제외, 1번부터 인접 컴퓨터 방문
    queue.appendleft(1)
    num_virus_com = 0
    visited[1] = True

    while queue:
        current_com = queue.pop()

        for adj_com in adj_dict[current_com]:
            if not visited[adj_com]:
                num_virus_com += 1
                visited[adj_com] = True
                queue.appendleft(adj_com)

    return num_virus_com


input = sys.stdin.readline

num_com = int(input().rstrip())
adj_pair = [
    [com for com in map(int, input().rstrip().split())]
    for _ in range(int(input().rstrip()))
]
adj_dict = make_adj_dict(adj_pair, num_com)
num_virus_com = count_virus_com()

sys.stdout.write(f"{num_virus_com}")
