def merge_sorted_arrays(input_):
    """ 
    :type input: Tuple[List[int], List[int]]
    :rtype: List[int] 
    """

    arr1 = input_[0]
    arr2 = input_[1]
    i = len(arr1) - 1
    j = len(arr2) - 1
    result = [0 for _ in range(len(arr1) + len(arr2))]
    while (i >= 0) and (j >= 0):
        if arr1[i] > arr2[j]:
            result[i+j+1] = arr1[i]
            i -= 1
        elif arr1[i] == arr2[j]:
            result[i+j+1] = arr1[i]
            i -= 1
            result[i+j+1] = arr2[j]
            j -= 1
        elif arr1[i] < arr2[j]:
            result[i+j+1] = arr2[j]
            j -= 1
    while i >= 0:
        result[i] = arr1[i]
        i -= 1
    while j >= 0:
        result[j] = arr2[j]
        j -= 1
    
    return result


inp = [[-10, 0, 3, 25], [-25, -5, 1, 14, 30]]

print(merge_sorted_arrays(inp))