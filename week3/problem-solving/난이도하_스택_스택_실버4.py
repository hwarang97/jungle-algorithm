# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys

input = sys.stdin.readline
times = int(input())
stack = []
output = []


def process_command(command, output):
    if command == "pop":
        pop(output)

    elif command == "size":
        size(output)

    elif command == "empty":
        empty(output)

    elif command == "top":
        top(output)

    else:
        # push
        push(command)


def pop(output):
    answer = ""
    if stack:
        answer = f"{stack.pop()}\n"
    else:
        answer = "-1\n"
    output.append(answer)


def size(output):
    output.append(f"{len(stack)}\n")


def empty(output):
    answer = 0 if stack else 1
    output.append(f"{answer}\n")


def top(output):
    answer = stack[-1] if stack else -1
    output.append(f"{answer}\n")


def push(command):
    _, str_int = command.split()
    stack.append(str_int)


for __ in range(times):
    command = input().rstrip()
    process_command(command, output)

sys.stdout.write("".join(output))
