class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = list(map(str, nums))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left_part = merge_sort(arr[:mid])
            right_part = merge_sort(arr[mid:])

            return merge(left_part, right_part)

        def merge(l, r):
            result = []
            i = j = 0
            while i < len(l) and j < len(r):
                if l[i] + r[j] >= r[j] + l[i]:
                    result.append(l[i])
                    i += 1
                else:
                    result.append(r[j])
                    j += 1

            while i < len(l):
                result.append(l[i])
                i += 1
            while j < len(r):
                result.append(r[j])
                j += 1

            return result


        sorted_nums = merge_sort(nums_str)

        if sorted_nums[0] == "0":
            return "0"

        return "".join(sorted_nums)
