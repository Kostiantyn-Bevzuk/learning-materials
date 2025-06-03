class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0  and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[n+m-1] = nums1[m-1]
                m -= 1
            elif nums1[m-1] <= nums2[n-1]:
                nums1[n+m-1] = nums2[n-1]
                n -= 1

        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1
        return nums1

nums1 = [1]
m = 1
nums2 = [0]
n = 0

print(Solution().merge(nums1, m, nums2, n))

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3