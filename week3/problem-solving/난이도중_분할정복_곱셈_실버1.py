# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

# remain_dict = dict()
# user_input = input().split()
# a, b, c = int(user_input[0]), int(user_input[1]), int(user_input[2])

# period = -1
# val = 1
# for k in range(1, c + 1):
#     val *= a
#     remain = val % c
#     if remain in remain_dict:
#         period = k - remain_dict[remain]
#         break
#     remain_dict[remain] = k

# small_b = b % period
# for remain, expo in remain_dict.items():
#     if expo == small_b:
#         print(remain)
#         break

# print(period)
# print(remain_dict)


# def calulate_exponetial(b, expo):
#     if expo == 1:
#         return b

#     if expo % 2 == 0:
#         return calulate_exponetial(b, expo // 2) ** 2

#     else:
#         return b * calulate_exponetial(b, expo - 1)


# user_input = input().split()
# a, b, c = int(user_input[0]), int(user_input[1]), int(user_input[2])
# val = calulate_exponetial(a, b) % c
# print(val)


def exponetial(base, expo, div):
    if expo == 1:
        return base % div

    if expo % 2 == 0:
        return exponetial(base, expo // 2, div) ** 2 % div

    else:
        return (base * exponetial(base, expo - 1, div)) % div


user_input = input().split()
a, b, c = int(user_input[0]), int(user_input[1]), int(user_input[2])
result = exponetial(a, b, c)
print(result)
