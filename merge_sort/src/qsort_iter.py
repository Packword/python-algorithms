def part_sort(arr, l, h):
    i = l - 1
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    #print(l, h, i+1, arr)
    return i + 1


def quickSortIter(arr, l, h):
    stack = [0] * (h - l + 1)
    top = 0
    stack[top] = l
    top = 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = part_sort(arr, l, h)
        #print(p)
        #print(stack)
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h



arr = [4, 2, 6, 1, 8, 7, 11, -1]
n = len(arr)
quickSortIter(arr, 0, n - 1)
print("Отсортированный массив:")
for i in range(n):
    print("% d" % arr[i]),
