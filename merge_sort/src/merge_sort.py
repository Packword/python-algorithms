def merge(arr):
    if len(arr) == 1 or len(arr) == 0:
        return
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    merge(left)
    merge(right)
    index_left = index_right = index = 0
    result = [[0, i] for i in range(len(left) + len(right))]
    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            result[index][0] = left[index_left][0]
            result[index][1] = left[index_left][1]
            index_left += 1
        else:
            result[index][0] = right[index_right][0]
            result[index][1] = right[index_right][1]
            index_right += 1
        index += 1
    while index_left < len(left):
        result[index][0] = left[index_left][0]
        result[index][1] = left[index_left][1]
        index_left += 1
        index += 1
    while index_right < len(right):
        result[index][0] = right[index_right][0]
        result[index][1] = right[index_right][1]
        index_right += 1
        index += 1
    for i in range(len(arr)):
        print(result[i][1], end=" ")
        arr[i] = result[i]
    print()
    return arr