class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        l, r = 0, len(nums)-1
        self.reverse(l, r, nums)
        l, r = 0, k-1
        self.reverse(l, r, nums)
        l, r = k, len(nums)-1
        self.reverse(l, r, nums)

    @staticmethod
    def reverse(l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1



print(Solution().rotate(nums=[1,2,3,4,5,6,7], k=3))

# [7, 6, 5, 4, 3, 2, 1] -> [5, 6, 7, 1, 2, 3, 4]