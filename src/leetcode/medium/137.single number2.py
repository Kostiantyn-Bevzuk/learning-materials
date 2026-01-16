class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                bit_counts[i] += (num >> i) & 1 # take rightmost bit

        for i in range(32):
            bit_counts[i] = bit_counts[i] % 3 # get mod division to get only one number

        # reconstruct digit
        result = 0
        for i in range(32):
            if bit_counts[i] == 1:
                result |= (1 << i)

        # check if negative
        if result >= (1 << 31):
            result -= (1 << 32)

        return result
