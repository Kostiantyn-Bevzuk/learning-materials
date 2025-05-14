class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        counter = 0
        plus = True
        if dividend < 0 or divisor < 0:
            plus = False
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            counter += 1

        if not plus:
            if -counter < INT_MIN:
                return INT_MIN
            return -counter
        if counter > INT_MAX:
            return INT_MAX
        return counter


## DO not pass corner cases
