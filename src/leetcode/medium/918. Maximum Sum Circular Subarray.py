class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        global_max = float("-inf")
        global_min = float("inf")
        curr_local_max = float("-inf")
        curr_local_min = float("inf")
        total = 0
        for num in nums:
            total += num
            curr_local_max = max(num, curr_local_max+num)
            curr_local_min = min(num, curr_local_min+num)
            if curr_local_max > global_max:
                global_max = curr_local_max
            if curr_local_min < global_min:
                global_min = curr_local_min
        if global_max < 0:
            return global_max
        return max(global_max, total - global_min)
