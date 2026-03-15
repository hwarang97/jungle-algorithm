# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

import sys


def get_reversed_word(word):
    char_list = []
    for i in range(len(word) - 1, -1, -1):
        char_list.append(word[i])
    return "".join(char_list)


input = sys.stdin.readline
times = int(input())
words = [input().rstrip() for _ in range(times)]
word_set = set(words)

password = ""
for word in words:
    reversed_word = get_reversed_word(word)
    if reversed_word == word or reversed_word in word_set:
        password = word
        break

print(f"{len(password)} {password[len(password)//2]}")
