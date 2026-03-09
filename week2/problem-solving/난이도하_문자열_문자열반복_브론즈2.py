# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

n_test = int(input())

# input_line_arr = []
# for _ in range(n_test):
#     input_arr = input().split(" ")
#     r, s = int(input_arr[0]), input_arr[1]
#     input_line_arr.append((r, s))

# for i in range(n_test):
#     r, s = input_line_arr[i]
#     for c in s:
#         print(c * r, end="")

#     if i < n_test - 1:
#         print()

for _ in range(n_test):
    input_arr = input().split(" ")
    r, s = int(input_arr[0]), input_arr[1]
    for c in s:
        print(c * r, end="")
    print()
