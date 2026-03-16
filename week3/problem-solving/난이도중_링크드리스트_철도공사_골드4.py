# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

# 객체를 생성해 푸는 방법 (시긴초과)
# import sys


# class Node:
#     def __init__(self, x):
#         self.id = x
#         self.prev = None
#         self.next = None


# def process_instructor(instructor, display, id_dict):
#     if not instructor:
#         return

#     commands = instructor.split()
#     if commands[0] == "BN":
#         bn(commands[1], commands[2], display, id_dict)

#     elif commands[0] == "BP":
#         bp(commands[1], commands[2], display, id_dict)

#     elif commands[0] == "CP":
#         cp(commands[1], display, id_dict)

#     elif commands[0] == "CN":
#         cn(commands[1], display, id_dict)


# def bn(id1, id2, display, id_dict):
#     current_node = id_dict[id1]
#     display.append(f"{current_node.next.id}\n")

#     new_node = Node(id2)
#     id_dict[id2] = new_node
#     new_node.next = current_node.next
#     current_node.next.prev = new_node
#     current_node.next = new_node
#     new_node.prev = current_node


# def bp(id1, id2, display, id_dict):
#     current_node = id_dict[id1]
#     display.append(f"{current_node.prev.id}\n")

#     new_node = Node(id2)
#     id_dict[id2] = new_node
#     new_node.prev = current_node.prev
#     current_node.prev.next = new_node
#     current_node.prev = new_node
#     new_node.next = current_node


# def cp(id, display, id_dict):
#     current_node = id_dict[id]
#     display.append(f"{current_node.prev.id}\n")
#     del id_dict[current_node.prev.id]

#     current_node.prev.prev.next = current_node
#     current_node.prev = current_node.prev.prev


# def cn(id, display, id_dict):
#     current_node = id_dict[id]
#     display.append(f"{current_node.next.id}\n")
#     del id_dict[current_node.next.id]

#     current_node.next = current_node.next.next
#     current_node.next.prev = current_node


# # read user input
# user_input = sys.stdin.read().splitlines()
# times = int(user_input[0].split()[1])
# ids = user_input[1].split()

# # init nodes
# current = None
# first = None
# id_dict = dict()
# for id in ids: # O(n)
#     new_node = Node(id)
#     id_dict[id] = new_node
#     if not current:
#         current = new_node
#         first = new_node
#     else:
#         current.next = new_node
#         new_node.prev = current
#         current = current.next

# current.next = first
# first.prev = current


# display = []
# for i in range(2, 2 + times): # O(m)
#     instructor = user_input[i]
#     process_instructor(instructor, display, id_dict) # O(1)

# # 출력문을 미리 작성한 후, 한번만 출력
# sys.stdout.write("".join(display))

# (배열을 이용해 관계 표현, Direct Access Array)
import sys


def process_instructor(instructor, prev, next, display):
    if not instructor:
        return

    commands = instructor.split()
    if commands[0] == "BN":
        bn(int(commands[1]), int(commands[2]), next, display)

    elif commands[0] == "BP":
        bp(int(commands[1]), int(commands[2]), prev, display)

    elif commands[0] == "CP":
        cp(int(commands[1]), prev, display)

    elif commands[0] == "CN":
        cn(int(commands[1]), next, display)


def bn(id1, id2, next, display):
    display.append(f"{next[id1]}\n")

    next[id2] = next[id1]
    prev[next[id1]] = id2
    next[id1] = id2
    prev[id2] = id1


def bp(id1, id2, prev, display):
    display.append(f"{prev[id1]}\n")

    prev[id2] = prev[id1]
    next[prev[id2]] = id2
    prev[id1] = id2
    next[id2] = id1


def cp(id, prev, next, display):
    display.append(f"{prev[id]}\n")
    prev[id] = prev[prev[id]]
    next[prev[id]] = id


def cn(id, prev, next, display):
    display.append(f"{next[id]}\n")
    next[id] = next[next[id]]
    prev[next[id]] = id


next = [None] * (1000000 + 1)
prev = [None] * (1000000 + 1)

# read input
user_input = sys.stdin.read().splitlines()
times = int(user_input[0].split()[1])
ids = [int(str_int) for str_int in user_input[1].split()]

# init
for i in range(len(ids) - 1):
    next[ids[i]] = ids[i + 1]
next[ids[-1]] = ids[0]

for j in range(1, len(ids)):
    prev[ids[j]] = ids[j - 1]
prev[ids[0]] = ids[-1]

display = []
for i in range(2, 2 + times):  # O(m)
    instructor = user_input[i]
    process_instructor(instructor, prev, next, display)  # O(1)

sys.stdout.write("".join(display))
