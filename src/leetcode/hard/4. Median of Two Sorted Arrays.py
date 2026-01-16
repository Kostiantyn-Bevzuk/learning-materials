class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1

        while True:
            i = l + (r-l) // 2
            j = half - i - 2 # why we substract 2 here

            A_right = A[i+1] if i+1 <= len(A) - 1 else float("inf")
            B_right = B[j+1] if j+1 <= len(B) - 1 else float("inf")
            A_left = A[i] if i >= 0 else -float("inf")
            B_left = B[j] if j >= 0 else -float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2: # more then 0 -> odd
                    return min(B_right, A_right)
                else: # odd
                    return (min(B_right, A_right) + max(A_left, B_left)) / 2
            
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1

