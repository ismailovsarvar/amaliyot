# def linear_search(array: list, target: int):
#     for arr in array:
#         if target == arr:
#             return array.index(arr)
#
#     return -1

arr = [10, 20, 30, 42, 11, 22, 56, 67, 89, 23, 44, 55, 66, 77]

arr.sort()
print(arr)


# print(linear_search(arr,23))
# O(n)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary_search(arr, 10))
