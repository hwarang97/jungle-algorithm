# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

import math

n = int(input())
arr = [int(str_num) for str_num in input().split(" ")]


def is_prime(n: int):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for num in range(3, limit, 2):
        if n % num == 0:
            return False

    return True


count = 0
for num in arr:
    count += is_prime(num)

print(count)
