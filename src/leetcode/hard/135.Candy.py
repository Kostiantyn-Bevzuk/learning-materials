class Solution:
    def candy(self, ratings: list[int]) -> int:
        size = len(ratings)
        candies = [1] * size
        # forward pass
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # backward pass
        for i in range(size-2, -1, -1):
            print(i)
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])

        return sum(candies)


print(Solution().candy([1,2,87,87,87,2,1]))

[1, 0, 2]
[1, 1, 2]
# [1,2,87,87,87,2,1] - > [1, 2, 3, 1, 1 , 2, 1]
[1,1, 1,1, 1, 1,1]

[1,2,3,1,1,1,1]
[1,2,3,1,3,2,1]


[5, 4, 3, 5, 6, 2]
[1, 1, 1, 2, 3, 1]

[1, 2, 3, 4, 5]
1, 2, 3, 4, 5
0, 1, 2, 3, 4
[1, 2, 3, 3]
1, 2, 3, 1
[1, 2, 3, 3, 2]
1, 2, 3, 2, 1
[1, 2, 2, 3, 3]
1, 2, 1, 2, 1
[1, 2, 2, 3, 4]
1, 2, 1, 2, 3



[3, 2, 1, 3]
3, 2, 1, 2