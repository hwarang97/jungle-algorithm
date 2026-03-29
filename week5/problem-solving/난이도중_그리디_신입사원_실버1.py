# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys

input = sys.stdin.readline


def get_save_people():
    """
    입력받고 합격한 사람수를 반환하는 함수
    """

    # 입력받기
    n = int(input().rstrip())
    candidates = []
    for _ in range(n):
        candidates.append(list(map(int, input().rstrip().split())))

    candidates.sort()
    saved_people = 1
    min_interview = candidates[0][1]
    for i in range(1, len(candidates)):
        if candidates[i][1] < min_interview:
            min_interview = candidates[i][1]
            saved_people += 1

    return saved_people


n = int(input().rstrip())

output = []
for _ in range(n):
    output.append(str(get_save_people()))

sys.stdout.write(f"{"\n".join(output)}")
