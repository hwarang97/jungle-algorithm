# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys


def make_wallet(n):
    """
    동전 10개를 가진 지갑을 만들어 반환하는 함수
    """
    wallet = [int(input().rstrip()) for _ in range(n)]
    return wallet


n, change = list(map(int, input().rstrip().split()))
wallet = make_wallet(n)
total = 0

for i in range(n - 1, -1, -1):
    if change == 0:
        break

    div, remain = divmod(change, wallet[i])
    total += div
    change = remain

sys.stdout.write(f"{total}")
