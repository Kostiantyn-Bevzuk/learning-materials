[2, 2, 1, 3, 4]

[2, 4, 4, 12, 48]

[48, 24, 12, 12, 4]

[24, 24, 48, 16, 12]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        postfix = []
        product = 1
        for elem in nums:
            product *= elem
            prefix.append(product)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix.append(product)
        postfix.reverse()
        result = []
        for i in range(len(nums)):
            if i - 1 < 0:
                value = postfix[i+1]
            elif i + 1 > len(nums)-1:
                value = prefix[i-1]
            elif i - 1 >= 0 and i+1 <= len(nums):
                value = prefix[i-1] * postfix[i+1]
            result.append(value)
        return result

# O(4n) time complexity

# More optimized approach
[2, 2, 1, 3, 4]

[2, 2, 1, 3, 4, 1]

[1, 2, 4, 4, 12, 48]

[24, 24, 48, 16, 12]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums)+1)
        for i in range(len(nums)):
            result[i+1] = result[i] * nums[i]
        nums.append(1)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            result[i] = result[i-1] * product
        return result[1:]


nums = [2, 2, 1, 3, 4]

print(Solution().productExceptSelf(nums))

# Alternative to previous

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfix *= result[i]
            result[i] = postfix
        return result