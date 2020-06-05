def linear_search(arr, target):
    for i in range(len(arr)):
        print('\nLinear Search')
        print(arr)
        print(arr[i], 'at position', [i])
        if arr[i] == target:
            print('TARGET:', target, 'at position:', i)
            return i

    return -1   # not found


# print('Linear Search target is at index: ', linear_search(
#     ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'f'))

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        print('\nBinary Search')
        print('TARGET:', target)
        print(arr)
        print('low:', arr[low], ' mid:', arr[mid], ' high:', arr[high])
        if mid_val == target:
            print('Target:', target, 'at position:', mid)
            return mid
        elif mid_val > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


# print('Binary Search target is at index: ', binary_search(
#     [11, 22, 33, 44, 55, 66, 77, 88, 99], 33))
