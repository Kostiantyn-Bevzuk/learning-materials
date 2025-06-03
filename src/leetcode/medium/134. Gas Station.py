class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return - 1
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        summ = 0
        start = 0
        for i in range(len(diff)):
            summ += diff[i]
            if summ < 0:
                summ = 0
                start = i + 1
        return start


        

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas =[5,1,2,3,4]
cost=[4,4,1,5,1]

Solution().canCompleteCircuit(gas, cost)

[-2, -2, -2, 3, 3]
[-2, -4, -6, -3, 0, -2]

[5,1,2,3,4]
[4,4,1,5,1]

[1, -3, 1, -2, 3]
[1, -2, -1, -3, 0]