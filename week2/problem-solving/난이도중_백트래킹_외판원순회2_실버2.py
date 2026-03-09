# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

n_city = int(input())
adj_matrix = [[int(str_num) for str_num in input().split()] for _ in range(n_city)]
mini = float("inf")
visited = [False for _ in range(n_city)]


def visit(c, acc):
    global mini

    if acc > mini:
        return

    if sum(visited) == n_city:
        if adj_matrix[c][0] != 0:
            acc += adj_matrix[c][0]
            mini = min(acc, mini)
        return

    for i in range(n_city):
        if not visited[i] and adj_matrix[c][i] != 0:
            visited[i] = True
            visit(i, acc + adj_matrix[c][i])
            visited[i] = False


visited[0] = True
visit(0, 0)

print(mini)
