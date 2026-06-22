def find_min_max(arr):

    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return min(arr[0], arr[1]), max(arr[0], arr[1])
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)


test_arrays = [
    [4, 2, 7, 1, 9, 3, 6, 8],
    [1],
    [5, 3],
    [10, 20, 30, 40, 50],
    [-1, -5, 3, -8, 2]
]

for arr in test_arrays:
    min_val, max_val = find_min_max(arr)
    print(f"Array: {arr}")
    print(f"Min: {min_val}, Max: {max_val}\n")