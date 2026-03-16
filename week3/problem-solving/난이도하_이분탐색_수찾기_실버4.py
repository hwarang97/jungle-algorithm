# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

n = int(input().rstrip())
n_numbers = set([int(str_int) for str_int in input().rstrip().split()])

m = int(input().rstrip())
m_numbers = [int(str_int) for str_int in input().rstrip().split()]

output = []
for number in m_numbers:
    if number in n_numbers:
        output.append("1\n")
    else:
        output.append("0\n")

sys.stdout.write("".join(output))
