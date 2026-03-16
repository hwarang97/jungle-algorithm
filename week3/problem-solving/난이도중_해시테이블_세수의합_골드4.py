# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(n)]
numbers.sort()

sum_set = set()
for i in range(len(numbers)):
    for j in range(len(numbers)):
        sum_set.add(numbers[i] + numbers[j])


def solution(numbers, sum_set):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            diff = numbers[i] - numbers[j]
            if diff in sum_set:
                return numbers[i]


sys.stdout.write(f"{solution(numbers, sum_set)}")
