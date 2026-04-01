test = [2, 1, 3, 3, 5, 2]
# test = [4, 3, 2]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # i = 1; j = 0
        while j >= 0 and arr[j] > key:  # arr[0] = 2, key = 1
            arr[j + 1] = arr[j]  # arr[0+1] = arr[0] -> []
            j -= 1
        arr[j + 1] = key  # arr[0]
    return arr


# print(insertion_sort(test))


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
        if l[i] > r[j]:
            result.append(r[j])
            j += 1
        else:
            result.append(l[i])
            i += 1
    while i < len(l):
        result.append(l[i])
        i += 1
    while j < len(r):
        result.append(r[j])
        j += 1
    return result


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        temp_arr = [0] * len(nums)

        # Function to merge two sub-arrays in sorted order.
        def merge(left: int, mid: int, right: int):
            # Calculate the start and sizes of two halves.
            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            # Copy elements of both halves into a temporary array.
            for i in range(n1):
                temp_arr[start1 + i] = nums[start1 + i]
            for i in range(n2):
                temp_arr[start2 + i] = nums[start2 + i]

            # Merge the sub-arrays 'in tempArray' back into the original array 'arr' in sorted order.
            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else:
                    nums[k] = temp_arr[start2 + j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < n1:
                nums[k] = temp_arr[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1

        # Recursive function to sort an array using merge sort
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            # Sort first and second halves recursively.
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            # Merge the sorted halves.
            merge(left, mid, right)

        merge_sort(0, len(nums) - 1)
        return nums


# print(merge_sort(test))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    left_part = []
    right_part = []
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left_part.append(arr[i])
        else:
            right_part.append(arr[i])

    return quick_sort(left_part) + [pivot] + quick_sort(right_part)


print(quick_sort(test))


# Counting sort!


# Heap sort with minimal space:
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Function to heapify a subtree (in top-down order) rooted at index i.
        def heapify(n: int, i: int):
            # Initialize largest as root 'i'.
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            # If left child is larger than root.
            if left < n and nums[left] > nums[largest]:
                largest = left
            # If right child is larger than largest so far.
            if right < n and nums[right] > nums[largest]:
                largest = right
            # If largest is not root swap root with largest element
            # Recursively heapify the affected sub-tree (i.e. move down).
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest) 

        def heap_sort():
            n = len(nums)
            # Build heap; heapify (top-down) all elements except leaf nodes.
            for i in range(n // 2 - 1, -1, -1):
                heapify(n, i)
            # Traverse elements one by one, to move current root to end, and
            for i in range(n - 1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                # call max heapify on the reduced heap.
                heapify(i, 0)

        heap_sort()
        return nums


# Using iterative approach -> can be done without stack as you store there only one variable

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)

        def heapify(size: int, pos: int):
            stack = [pos]
            while stack:
                pos = stack.pop()
                largest = pos
                left_child = 2 * pos + 1
                right_child = 2 * pos + 2
                if left_child < size and nums[largest] < nums[left_child]:
                    largest = left_child
                if right_child < size and nums[largest] < nums[right_child]:
                    largest = right_child
                
                if largest != pos:
                    stack.append(largest)
                    # go fix parent nodes
                    nums[largest], nums[pos] = nums[pos], nums[largest]
                    # heapify(size, largest)

        for i in range(len_nums // 2 - 1, -1, -1):
            # build max heap
            heapify(len_nums, i)
        
        for i in range(len_nums-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            # heapify(i, 0)
            len_nums -= 1
            heapify(len_nums, 0)

        return nums
        

Solution().sortArray([2, 1, 3, 3, 5, 2])
