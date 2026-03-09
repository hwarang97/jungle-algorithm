# 백트래킹 - Word Search
# 문제 링크: https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    """
    time: O(m * n * 4^n)
    space: O(n)
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def helper(row, col, i, visited):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in visited
            ):
                return

            if board[row][col] != word[i]:
                return

            visited.add((row, col))
            if i == len(word) - 1:
                return True

            for mov_x, mov_y in directions:
                if helper(row + mov_x, col + mov_y, i + 1, visited):
                    return True

            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited = set()
                    if helper(row, col, 0, visited):
                        return True

        return False
