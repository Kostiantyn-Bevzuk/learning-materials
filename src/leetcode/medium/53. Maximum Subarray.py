# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         global_summ = -float("inf")
#         running_max_summ = -float("inf")
#         for num in nums:
#             running_max_summ = max(num, running_max_summ+num)
#             if running_max_summ > global_summ:
#                 global_summ = running_max_summ

#         return global_summ


# Follow-up: divide and conquer

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        start, end = 0, len(nums)-1
    
        def divide_and_conquer(left_idx, right_idx):
            if left_idx == right_idx:
                return nums[left_idx]
            mid_elem_index = (left_idx+right_idx) // 2
            left = divide_and_conquer(left_idx, mid_elem_index)
            right = divide_and_conquer(mid_elem_index+1, right_idx)
            mid_elem = find_crossing_sum(left_idx, right_idx, mid_elem_index)

            return max(left, right, mid_elem)


        def find_crossing_sum(left, right, mid_indx):
            best_summ_left = -float("inf")
            best_summ_right = -float("inf")
            running_max_summ = 0
            for indx in range(mid_indx-1, left-1, -1):
                running_max_summ = running_max_summ + nums[indx]
                best_summ_left = max(best_summ_left, running_max_summ)
            running_max_summ = 0
            for indx in range(mid_indx+1, right+1):
                running_max_summ = running_max_summ + nums[indx]
                best_summ_right = max(best_summ_right, running_max_summ)
            return best_summ_left + best_summ_right + nums[mid_indx]

        return divide_and_conquer(start, end)
    

nums = [-2,1,-3,4,-1,2,1,-5,4]

Solution().maxSubArray(nums)
