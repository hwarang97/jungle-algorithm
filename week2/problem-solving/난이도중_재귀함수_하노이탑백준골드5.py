# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914


n = int(input())


def get_hanoi(n):
    return 2**n - 1


def print_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"{source} {destination}")
        return

    print_hanoi(n - 1, source, auxiliary, destination)
    print(f"{source} {destination}")
    print_hanoi(n - 1, auxiliary, destination, source)
    return


print(get_hanoi(n))
if n <= 20:
    print_hanoi(n, 1, 3, 2)
