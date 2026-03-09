# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []
times = 9
for _ in range(times):
    nums.append(int(input()))

maxi = nums[0]
maxi_idx = 0
for i, num in enumerate(nums):
    if num > maxi:
        maxi = num
        maxi_idx = i

print(maxi)
print(maxi_idx + 1)
