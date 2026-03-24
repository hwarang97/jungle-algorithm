# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948

import sys

from collections import deque

input = sys.stdin.readline


def get_graph():
    """
    그래프를 반환하는 함수
    return: tuple[dict, dict]
    """

    city_map = {city: [] for city in range(1, int(input().rstrip()) + 1)}
    city_to_cost = dict()
    for _ in range(int(input().rstrip())):
        input_arr = list(map(int, input().rstrip().split()))
        city_map[input_arr[0]].append(input_arr[1])
        city_to_cost[(input_arr[0], input_arr[1])] = input_arr[2]

    return city_map, city_to_cost


def get_biggest_time_array(current, destination, city_map, city_to_cost):
    """
    current 에서 destination 까지 최고 비용을 계산한 배열을 반환하는 함수
    """
    dp = [-1] * (len(city_map) + 1)
    dfs(current, destination, dp, city_map, city_to_cost)
    return dp


def dfs(current, destination, dp, city_map, city_to_cost):
    """
    dfs 방식으로 current에서 destination까지 걸리는 최장시간을 반환하는 함수
    """
    if current == destination:
        dp[destination] = 0
        return 0

    max_time = -1
    for next_city in city_map[current]:
        next_city_to_destination = -1
        if dp[next_city] == -1:
            next_city_to_destination = dfs(
                next_city, destination, dp, city_map, city_to_cost
            )
        else:
            next_city_to_destination = dp[next_city]
        time = city_to_cost[(current, next_city)] + next_city_to_destination
        if time > max_time:
            max_time = time

    dp[current] = max_time
    return dp[current]


def get_edge_in_longest_path(city_map, city_to_cost, dp, source):
    """
    최장 시간 경로 간선들을 포함한 집합을 반환하는 함수
    """
    longest_edge_set = set()
    queue = deque([source])
    visited = set()
    visited.add(source)
    while queue:
        current = queue.popleft()

        for next_city in city_map[current]:
            if city_to_cost[(current, next_city)] + dp[next_city] == dp[current]:
                longest_edge_set.add((current, next_city))

                if next_city not in visited:
                    queue.append(next_city)
                    visited.add(next_city)

    return longest_edge_set


city_map, city_to_cost = get_graph()
source, destination = list(map(int, input().rstrip().split()))

dp = get_biggest_time_array(source, destination, city_map, city_to_cost)
longest_edge_set = get_edge_in_longest_path(city_map, city_to_cost, dp, source)

sys.stdout.write(f"{dp[source]}\n{len(longest_edge_set)}")
