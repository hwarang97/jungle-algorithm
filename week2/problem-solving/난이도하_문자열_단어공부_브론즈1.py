# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

input_str = input()
counter = dict()
for c in input_str:
    upper_c = c.upper()
    if upper_c in counter:
        counter[upper_c] += 1
    else:
        counter[upper_c] = 1

most_frequncy = 0
most_frequent_char = None
is_same_frequency = False
for key, value in counter.items():
    if value > most_frequncy:
        most_frequent_char = key
        most_frequncy = value
        is_same_frequency = False

    elif value == most_frequncy:
        is_same_frequency = True

print("?" if is_same_frequency else most_frequent_char)
