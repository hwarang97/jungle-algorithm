# DP
# https://leetcode.com/problems/house-robber-ii/description/


class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max_money(arr):
            n = len(arr)

            if n == 0:
                return 0

            if n == 1:
                return arr[0]

            if n == 2:
                return max(arr[0], arr[1])

            memo = [-1 for i in range(n + 1)]

            i = 3
            memo[1] = arr[0]
            memo[2] = max(arr[0], arr[1])
            while i <= n:
                memo[i] = max(arr[i - 1] + memo[i - 2], memo[i - 1])
                i += 1

            return memo[n]

        if len(nums) == 1:
            return nums[0]

        return max(get_max_money(nums[:-1]), get_max_money(nums[1:]))
