# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

import math


def is_prime(n):  # O(n)
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    n_sqrt = math.sqrt(n)
    limit = int(n_sqrt) + 1
    for num in range(3, limit, 2):
        if n % num == 0:
            return False

    return True


def get_primes(n):  # O(n * root(n))
    num_array = [num for num in range(1, n + 1)]
    bool_array = [True for _ in range(n)]
    primes = []
    limit = int(math.sqrt(n)) + 1
    for num in range(1, limit):
        if bool_array[num - 1]:
            if is_prime(num):
                k = 2
                while k * num - 1 < n:
                    bool_array[k * num - 1] = False
                    k += 1
            else:
                bool_array[num - 1] = False

    half = n // 2
    half_index = 0
    is_sqrt = False
    for i in range(n):
        if bool_array[i]:
            if num_array[i] < half:
                half_index += 1
                primes.append(num_array[i])
            elif num_array[i] == half:
                half_index += 1
                primes.append(num_array[i])
                is_sqrt = True
            else:
                primes.append(num_array[i])

    head_list = primes[:half_index]
    if is_sqrt:
        tail_set = set(primes[half_index - 1 :])
    else:
        tail_set = set(primes[half_index:])

    return head_list, tail_set


def print_smallest_pair(n):  # O(n^2)
    small_primes, big_primes = get_primes(n)
    smallest_diff = n
    smallest_pair = None

    for small_prime in reversed(small_primes):
        pair_prime = n - small_prime
        if pair_prime in big_primes:
            diff = pair_prime - small_prime
            if diff < smallest_diff:
                # smallest_diff = diff
                smallest_pair = (small_prime, pair_prime)
                break

    print(f"{smallest_pair[0]} {smallest_pair[1]}")


times = int(input())
for _ in range(times):
    n = int(input())
    print_smallest_pair(n)
