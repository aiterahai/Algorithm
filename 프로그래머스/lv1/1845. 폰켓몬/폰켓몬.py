def solution(nums):
    N = len(nums) // 2
    nums = set(nums)
    return min(N, len(nums))