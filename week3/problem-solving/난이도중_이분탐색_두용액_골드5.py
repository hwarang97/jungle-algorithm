# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

times = int(input().rstrip())
arr = [int(str_int) for str_int in input().rstrip().split()]
arr.sort()


left = 0
right = len(arr) - 1
smallest_diff = float("inf")
pair = None
while left < right:
    current_sum = arr[right] + arr[left]
    diff = abs(current_sum)
    if smallest_diff > diff:
        smallest_diff = diff
        pair = (arr[left], arr[right])
    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        pair = (arr[left], arr[right])
        break

sys.stdout.write(f"{pair[0]} {pair[1]}")
