def find_rotation_point(arr: list) -> int:
    if len(arr) == 1:
        return 0
    left = 0
    right = len(arr) - 1
    if arr[left] < arr[right]:
        return 0
    while left < right:
        mid = (left + right) // 2
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > 0 and arr[mid] < arr[mid - 1]:
            return mid
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left
