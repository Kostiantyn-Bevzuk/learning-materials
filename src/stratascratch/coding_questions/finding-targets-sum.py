# def find_intervals(input):
#     """
#     :type input: Dict[str, Any]
#     :rtype: List[List[int]]
#     """

#     nums = input["nums"]
#     target_sum = input["target_sum"]
#     n = input["n"]
#     tmp_scan_obj = [target_sum for i in range(len(nums))]
#     i = j = 0
#     result = []
#     while i < len(nums):
#         curr_result = []
#         for index in range(j, i+1):
#             if nums[i] == tmp_scan_obj[index]:
#                 while index <= i:
#                     curr_result.append(nums[index])
#                     index += 1
#                 result.append(curr_result)
#                 j = i + 1
#                 break
#             else:
#                 tmp_scan_obj[index] = tmp_scan_obj[index] - nums[i]
#         i += 1
#     result.sort(key=lambda x: len(x))
#     return result[:n+1]

def find_intervals(input):
    """
    :type input: Dict[str, Any]
    :rtype: List[List[int]]
    """
    nums = input["nums"]
    target_sum = input["target_sum"]
    n = input["n"]
    if not nums:
        return
    result = []
    prefix_sum = [0 for _ in range(len(nums)+1)]
    for i in range(len(nums)):
        prefix_sum[i+1] = nums[i] + prefix_sum[i]
    for i in range(len(prefix_sum)):
        for j in range(i+1, len(prefix_sum)):
            if prefix_sum[j] - prefix_sum[i] == target_sum:
                result.append(nums[i:j])
                
    result.sort(key=lambda x: len(x))
    
    return result[:n]

    
input_ = {"n": 2, "nums": [1, 2, 3, 4, 5], "target_sum": 5}
input_ = {"n": 3, "nums": [1, -1, 2, -2, 3, -3, 4], "target_sum": 0}

find_intervals(input_)

"""
[1, 3, 6, 10, 15] target: 5
[]
"""