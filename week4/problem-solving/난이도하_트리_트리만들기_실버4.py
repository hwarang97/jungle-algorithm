# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

import sys


def print_edge(n, m, output):
    """
    노드2, 리프3인 그래프로부터 노드 n, 리프 m을 갖는 그래프까지 간선을 출력하는 함수

    args:
        n: 노드 개수
        m: 리프 개수
        output: 결과를 담을 리스트
    """
    # 첫번째 시도
    # if n == 3 and m == 2:
    #     output.append("0 1")
    #     output.append("1 2")
    #     return

    # if n - m > 1:
    #     recursive(n - 1, m, output)
    #     output.append(f"{n - 2} {n - 1}")

    # elif n - m == 1:
    #     recursive(n - 1, m - 1, output)
    #     output.append(f"{n - 3} {n - 1}")

    # 두번쨰 시도
    output.append("0 1")
    output.append("1 2")

    source = 1
    destination = 2
    while destination < m:
        output.append(f"{source} {destination + 1}")
        destination += 1

    source = destination
    while source < n - 1:
        output.append(f"{source} {source + 1}")
        source += 1


input = sys.stdin.readline
n, m = map(int, input().split())
output = []
print_edge(n, m, output)

sys.stdout.write("\n".join(output))
