# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

import sys

input = sys.stdin.readline
DIV = 15746

n = int(input().rstrip())

# 1,000,000 * 8바이트는 대략 800MB 이상이므로 메모리 초과.
# current_3 = current_1 + current_2
current_1 = 1
current_2 = 2
current_3 = -1

i = 3
while i <= n:
    current_3 = (current_1 + current_2) % DIV  # 2칸만 있어도 충분하다
    current_1 = current_2
    current_2 = current_3
    i += 1

output = -1
if n == 1:
    output = current_1

elif n == 2:
    output = current_2

else:
    output = current_3

sys.stdout.write(f"{output}")

# import sys

# input = sys.stdin.readline
# DIV = 15746
# M = [[1, 1], [1, 0]]


# def fibonacci(n):
#     if n == 1:
#         return M[0][0]

#     A = matrix_power(M, n)
#     return A[0][0]


# def matrix_power(A, n):  # O(log(n))
#     if n == 1:
#         return M

#     if n % 2 == 0:
#         B = matrix_power(A, n // 2)
#         return matrix_multiply(B, B)

#     else:
#         B = matrix_power(A, n - 1)
#         return matrix_multiply(M, B)


# def matrix_multiply(A, B):
#     a_11 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
#     a_12 = A[0][0] * B[1][0] + A[0][1] * B[1][1]
#     a_21 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
#     a_22 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

#     return [[a_11, a_12], [a_21, a_22]]


# n = int(input().rstrip())
# sys.stdout.write(f"{fibonacci(n) % DIV}")
