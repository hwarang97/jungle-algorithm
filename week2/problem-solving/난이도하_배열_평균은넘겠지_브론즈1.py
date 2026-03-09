# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344


def get_average(arr):
    n = len(arr)
    return sum(arr) // n


def print_percentage(count, n):
    print(f"{count / n * 100:.3f}%")


n_case = int(input())
for _ in range(n_case):
    case_input = [int(str_num) for str_num in input().split(" ")]
    n_fresher = case_input[0]
    score_array = case_input[1:]
    score_average = get_average(score_array)

    count = 0
    for score in score_array:
        if score > score_average:
            count += 1

    print_percentage(count, n_fresher)
