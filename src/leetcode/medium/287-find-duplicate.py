class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow_second = 0
        while True:
            slow = nums[slow]
            slow_second = nums[slow_second]
            if slow == slow_second:
                return slow



Solution().findDuplicate([1,3,4,2,2])
