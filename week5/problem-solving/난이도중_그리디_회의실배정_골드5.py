# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

prev = arr[0]
output = [prev]
for i in range(1, len(arr)):
    meeting = arr[i]
    if prev[1] <= meeting[0]:
        print(f"{prev=} {meeting=}")
        output.append(meeting)
        prev = meeting

sys.stdout.write(f"{len(output)}")
