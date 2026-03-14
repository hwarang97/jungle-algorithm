# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

# 직접 구현하는 방식
import sys


class Doubly_Linked_Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Editor:
    def __init__(self, s: str):
        # init dummy
        self.cursor = None
        self.left_dummy = Doubly_Linked_Node(None)
        self.right_dummy = Doubly_Linked_Node(None)

        self.left_dummy.next = self.right_dummy
        self.left_dummy.prev = self.left_dummy
        self.right_dummy.prev = self.left_dummy
        self.right_dummy.next = self.right_dummy
        self.cursor = self.right_dummy

        # add node
        for c in s:  # O(n)
            self.insert_left(c)

    def move_cursor_left(self):  # O(1)
        if self.cursor.prev != self.left_dummy:
            self.cursor = self.cursor.prev

    def move_cursor_right(self):  # O(1)
        if self.cursor.next:
            self.cursor = self.cursor.next

    def insert_left(self, x):  # O(1)
        new_node = Doubly_Linked_Node(x, self.cursor.prev, self.cursor)
        if self.cursor.prev:
            new_node.prev = self.cursor.prev
            new_node.next = self.cursor
            self.cursor.prev.next = new_node
            self.cursor.prev = new_node
        else:
            self.cursor.prev = new_node
            new_node.next = self.cursor

    def delete_left(self):  # O(1)
        if self.cursor.prev != self.left_dummy:
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor

    def print_content(self):  # O(n)
        current = self.left_dummy.next
        while current != self.right_dummy:
            print(current.data, end="")
            current = current.next


def parse_command(editor: Editor, command):
    if command[0] == "L":
        editor.move_cursor_left()

    elif command[0] == "D":
        editor.move_cursor_right()

    elif command[0] == "P":
        editor.insert_left(command[2])

    elif command[0] == "B":
        editor.delete_left()


# user_input = sys.stdin.read().splitlines()
# s = user_input[0]
# times = int(user_input[1])

s = input()
times = int(input())

editor = Editor(s)
# m = len(user_input)
# for i in range(2, m):
#     parse_command(editor, user_input[i])
for _ in range(times):
    command = input()
    parse_command(editor, command)
editor.print_content()

# ==============================================================================
# 스택 이용
# import sys


# def move_left(l_side, r_side):
#     if l_side:
#         pop_item = l_side.pop()
#         r_side.append(pop_item)


# def move_right(l_side, r_side):
#     if r_side:
#         pop_item = r_side.pop()
#         l_side.append(pop_item)


# def delete_left(l_side):
#     if l_side:
#         l_side.pop()


# def insert_left(l_side, x):
#     l_side.append(x)


# def print_content(l_side, r_side):
#     sys.stdout.write("".join(l_side) + "".join(r_side[::-1]) + "\n")


# def parse_command(command, l_side, r_side):
#     if not command:
#         return

#     if command[0] == "L":
#         move_left(l_side, r_side)

#     elif command[0] == "D":
#         move_right(l_side, r_side)

#     elif command[0] == "P":
#         insert_left(l_side, command.split()[1])

#     elif command[0] == "B":
#         delete_left(l_side)


# user_input = sys.stdin.read().splitlines()
# if not user_input:
#     sys.exit(0)

# s = user_input[0]
# times = int(user_input[1])

# l_side = list(s)
# r_side = []

# m = len(user_input)
# for i in range(2, 2 + times):
#     parse_command(user_input[i], l_side, r_side)
# print_content(l_side, r_side)
