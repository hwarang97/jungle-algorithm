# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

# from collections import deque

# togological sort implementation
# graph = {
#     "A": ["C", "D"],
#     "B": ["D", "E"],
#     "C": ["F"],
#     "D": ["F", "G"],
#     "E": ["G"],
#     "F": ["H"],
#     "G": ["H"],
#     "H": [],
# }


# def get_topoligical_array_dfs(graph):
#     "위상정렬된 배열을 반환하는 함수"
#     visited = set()
#     output = []

#     for vertex in graph.keys():
#         if vertex not in visited:
#             dfs(graph, vertex, visited, output)

#     return output[::-1]


# def dfs(graph, current, visited, output):
#     "dfs 방식으로 진입한 순서를 stack에 저장하는 함수"

#     visited.add(current)

#     for adj_vertex in graph[current]:
#         if adj_vertex not in visited:
#             dfs(graph, adj_vertex, visited, output)

#     output.append(current)


# def get_topological_sort_array_bfs(graph):
#     """
#     위상정렬된 배열을 반환하는 함수
#     """

#     in_degree_dict = get_in_degree_dict(graph)
#     output = []
#     bfs(graph, in_degree_dict, output)

#     return output


# def get_in_degree_dict(graph):
#     """
#     진입 차수 딕셔너리를 반환하는 함수
#     """
#     in_degree_dict = {vertex: 0 for vertex in graph.keys()}
#     for adj_list in graph.values():
#         for adj_vertex in adj_list:
#             if adj_vertex in in_degree_dict:
#                 in_degree_dict[adj_vertex] += 1
#             else:
#                 in_degree_dict[adj_vertex] = 1

#     return in_degree_dict


# def bfs(graph, in_degree_dict, output):
#     """
#     진입차수가 0인 정점들을 순차적으로 접근하는 함수
#     """

#     queue = deque()
#     for vertex, in_degree in in_degree_dict.items():
#         if in_degree == 0:
#             queue.appendleft(vertex)

#     while queue:
#         current = queue.pop()
#         for adj_vertex in graph[current]:
#             in_degree_dict[
#                 adj_vertex
#             ] -= 1  # 여기를 어떻게 깔끔하게 만들까? 굳이 0이 아니게 만들려고 음수를 써야할까?

#             if in_degree_dict[adj_vertex] == 0:
#                 queue.appendleft(adj_vertex)

#         output.append(current)


# print(get_topoligical_array_dfs(graph))
# print(get_in_degree_dict(graph))
# print(get_topological_sort_array_bfs(graph))

import heapq
import sys

intput = sys.stdin.readline


def parse_input():
    """
    입력을 받아 graph와 in degree 정보를 반환하는 함수
    """
    n = int(input().rstrip())

    graph = {vertex: [] for vertex in range(1, n + 1)}
    in_degree = {vertex: 0 for vertex in range(1, n + 1)}
    vertex_to_time = {vertex: 0 for vertex in range(1, n + 1)}

    for i in range(n):
        input_arr = list(map(int, input().rstrip().split()))
        vertex_to_time[i + 1] = input_arr[0]
        in_degree[i + 1] += input_arr[1]
        for j in range(input_arr[1]):
            graph[input_arr[2 + j]].append(i + 1)

    return graph, in_degree, vertex_to_time


graph, in_degree, vertex_to_time = parse_input()
heap = []
time = 0

# 진입차수가 0인 정점들을 힙에 삽입 (종료시간, 번호)
for vertex, degree in in_degree.items():
    if degree == 0:
        heapq.heappush(heap, (vertex_to_time[vertex] + time, vertex))

while heap:
    while heap and heap[0][0] == time:
        current = heapq.heappop(heap)
        for adj_vertex in graph[current[1]]:
            in_degree[adj_vertex] -= 1
            if in_degree[adj_vertex] == 0:
                heapq.heappush(heap, (vertex_to_time[adj_vertex] + time, adj_vertex))

    if heap:
        time += 1

sys.stdout.write(f"{time}")
