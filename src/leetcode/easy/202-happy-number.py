class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.calculate_sum_square(n)
        fast = self.calculate_sum_square(self.calculate_sum_square(n))
        while slow != fast:
            if fast == 1:
                return True
            slow = self.calculate_sum_square(slow)
            fast = self.calculate_sum_square(self.calculate_sum_square(fast))
        return slow == 1

    @staticmethod
    def calculate_sum_square(value: int) -> int:
        output = 0
        while value:
            last_digit = value % 10
            output += last_digit**2
            value = value // 10
        return output



# print(Solution().isHappy(10))


class Solution:
    def isHappy(self, n: int) -> bool:
        variants = set()
        n_str = str(n)
        while n != 1:
            if n_str in variants:
                return False
            variants.add(n_str)
            value = 0
            for char in n_str:
                value += int(char) ** 2
            n_str = str(value)
        return True
    
print(Solution().isHappy(19))