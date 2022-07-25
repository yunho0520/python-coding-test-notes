# Time Complexity: O(n)
# Accepted Answer
def search_range1(nums, target):
    first = -1
    last = -1
    for idx, n in enumerate(nums):
        if n == target:
            if first == -1:
                first = idx
                last = idx
            else:
                last = idx
    if first != -1:
        return [first, last]
    else:
        return [-1, -1]


# Time Complexity: O(n)
# Accepted Answer
def search_range2(nums, target):
    first = -1
    last = -1
    n = len(nums)
    for i in range(0, n):
        if target != nums[i]:
            continue
        if first == -1:
            first = i
        last = i

    if first != -1:
        return [first, last]
    else:
        return [-1, -1]


# Time Complexity: O(log n)
# Accepted Answer
from bisect import bisect_left, bisect_right


def search_range3(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    idx_left = bisect_left(nums, target)
    if idx_left >= len(nums):
        return [-1, -1]

    first = -1
    last = -1

    idx_right = bisect_right(nums, target)

    if nums[idx_left] == target:
        first = idx_left
        last = idx_left
    if nums[idx_right - 1] == target:
        last = idx_right - 1

    if first != -1:
        return [first, last]

    return [-1, -1]


# Time Complexity: O(log n)
# Accepted Answer
def search_range4(nums, target):
    def first(arr, x, num):
        low = 0
        high = num - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                res = mid
                high = mid - 1

        return res

    def last(arr, x, num):
        low = 0
        high = num - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                res = mid
                low = mid + 1

        return res

    n = len(nums)

    return [first(nums, target, n), last(nums, target, n)]
