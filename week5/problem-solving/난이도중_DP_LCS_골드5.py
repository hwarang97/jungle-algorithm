# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

import sys

input = sys.stdin.readline


def digit_to_int(num_str):
    """
    5자리 10진수를 정수로 변환하는 함수
    args:
        x: 0으로 시작할 수 있는 5자리 문자열
    return:
        x와 같은 값을 갖는 정수
    """
    return int(num_str)


expression = input().strip()
total = 0
sign = 1
minus_position = -1
for i in range(len(expression)):
    if expression[i] == "-":
        total += sign * sum(
            map(digit_to_int, expression[minus_position + 1 : i].split("+"))
        )
        sign = -1
        minus_position = i

total += sign * sum(map(digit_to_int, expression[minus_position + 1 :].split("+")))
print(total)
