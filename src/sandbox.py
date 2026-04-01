# gold = [1, 4, 3, 5]
# colors = [1, 1, 2, 2]

# def get_max_gold(gold, colors):
#     total = 0
#     before_prev = 0
#     prev = gold[len(gold)-1]
#     curr_max = gold[len(gold)-1]
#     for i in range(len(gold)-2, -1, -1):
#         if colors[i] == colors[i+1]:
#             # start_of_group
#             curr_max = max(curr_max, before_prev+gold[i], prev)
#             before_prev = prev
#             prev = curr_max
#         else:
#             # end of group update result
#             total += curr_max
#             before_prev = 0
#             prev = gold[i]
#             curr_max = gold[i]
#     total += curr_max
#     return total


# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         prefix = strs[0]
#         for i in range(1, len(strs)):
#             while strs[i].find(prefix) != 0:
#                 prefix = prefix[0 : len(prefix) - 1]
#                 if prefix == "":
#                     return ""
#         return prefix


# strs = ["flower","flow","flight"]
# Solution().longestCommonPrefix(strs)

# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = j = 0
#         while i < len(nums):
#             while j < len(nums) and nums[j] != 0:
#                 j += 1
#             # j pos of first zero = 0
#             while i < len(nums) and nums[i] == 0:
#                 i += 1
#             # i pos of first non zero = 1
#             if i > len(nums) - 1 or j > len(nums) - 1: # 0 > 1 or 1 > 1
#                 return
#             nums[i], nums[j] = nums[j], nums[i]
#             # [1, 0, 0, 3, 12]

# Solution().moveZeroes([1, 0])

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# #         4
# #        / \
# #       2   6
# #      / \ / \
# #     1  3 5  7
# root = TreeNode(4,
#     TreeNode(2,
#         TreeNode(1),
#         TreeNode(3)),
#     TreeNode(6,
#         TreeNode(5),
#         TreeNode(7)))

# class Solution:
#     def convertBST(self, root: [TreeNode]) -> [TreeNode]:
#         curr_sum = 0

#         def dfs(root):
#             nonlocal curr_sum
#             if not root:
#                 return None, 0

#             if root.right:
#                 dfs(root.right)
#             curr_sum += root.val
#             root.val = curr_sum
#             if root.left:
#                 dfs(root.left)

#             return root

#         return dfs(root)

# Solution().convertBST(root)


# class Solution:
#     def longestBalanced(self, s: str) -> int:
#         ans = 0
#         for c in range(1, 27):
#             l = r = 0
#             storage = {}
#             while r < len(s):
#                 if s[r] in storage:
#                     current_counter = storage[s[r]]
#                     if current_counter >= c:
#                         if len(set(storage.values())) == 1:
#                             ans = max(ans, r-l)
#                         l = r
#                         storage = {s[r]: 1}
#                     else:
#                         storage[s[r]] += 1
#                 else:
#                     storage[s[r]] = 1
#                 set_storage_vals = set(storage.values())
#                 if len(set_storage_vals) == 1 and set_storage_vals[0] == c:
#                     ans = max(ans, r-l+1)
#                 r += 1

#         return ans

# s = "abbac"

# Solution().longestBalanced(s)

# class Solution:
#     def totalFruit(self, fruits: list[int]) -> int:
#         ans = 0
#         if not fruits:
#             return ans
#         i = j = 0
#         fruits_storage = {}
#         while j < len(fruits):
#             fruits_storage[fruits[j]] = fruits_storage.get(fruits[j], 0) + 1

#             while len(fruits_storage) > 2:
#                 fruits_storage[fruits[i]] -= 1

#                 if fruits_storage[fruits[i]] == 0:
#                     del fruits_storage[fruits[i]]

#                 i += 1

#             ans = max(ans, j - i + 1)
#             j += 1
#         return ans


# f = [0,1,6,6,4,4,6]

# Solution().totalFruit(f)

# j = 2
# i = 0
# {1: 0, 2: 1}

# [0, 1, 2]

# class Solution:
#     def decodeString(self, s: str) -> str:
#         numbers = {str(j) for j in range(10)}
#         def decode(i, num_to_repeat) -> (str, int):
#             curr_str = []
#             k = []
#             while i < len(s):
#                 if s[i] == "]":
#                     out = "".join(curr_str)
#                     return num_to_repeat * "".join(curr_str), i
#                 elif s[i] in numbers:
#                     k.append(s[i])
#                 elif s[i] == "[":
#                     # recurse with i + 1
#                     k_to_send = int("".join(k))
#                     out, i = decode(i + 1, k_to_send)
#                     k = []
#                     curr_str.append(out)
#                 elif s[i] not in numbers and s[i] != "]":
#                     curr_str.append(s[i])

#                 i += 1

#             return num_to_repeat * "".join(curr_str), None

#         ans, _ = decode(0, 1)
#         return ans

# Solution().decodeString("3[a]2[bc]")

# from collections import defaultdict, deque


# class Solution:
#     def sequenceReconstruction(
#         self, nums: list[int], sequences: list[list[int]]
#     ) -> bool:
#         indegree = defaultdict(int)
#         adj_list = defaultdict(list)
#         seq_len = len(sequences[0])

#         topological_sorted = []

#         for seq in sequences:
#             for i in range(seq_len):
#                 src = seq[i]
#                 if i + 1 < seq_len:
#                     dst = seq[i+1]
#                     adj_list[src].append(dst)
#                     indegree[dst] += 1
                    
#                 else:
#                     adj_list[src].append(None)

#         queue = deque([v for v in adj_list if v not in indegree])

#         while queue:
#             if len(queue) > 1:
#                 return False

#             passed_vertex = queue.popleft()
#             topological_sorted.append(passed_vertex)
#             for neighbour in adj_list[passed_vertex]:
#                 indegree[neighbour] -= 1

#                 if indegree[neighbour] == 0:
#                     queue.append(neighbour)
#                     del indegree[neighbour]

#         return nums == topological_sorted


# Solution().sequenceReconstruction([1], [[1]])


# class Solution:
#     def permuteUnique(self, nums: list[int]) -> list[list[int]]:
#         ans = []
#         curr_comb = []
#         nums.sort()
#         used = [False for _ in range(len(nums))]

#         def backtrack():
#             if len(curr_comb) == len(nums):
#                 ans.append(curr_comb[:])
#                 return

#             for i in range(len(nums)):
#                 if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
#                     continue
#                 if used[i]:
#                     continue
#                 used[i] = True
#                 curr_comb.append(nums[i])
#                 backtrack()
#                 used[i] = False
#                 curr_comb.pop()
            

#         backtrack()
#         return ans

# Solution().permuteUnique([1, 1, 2])

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        ...
