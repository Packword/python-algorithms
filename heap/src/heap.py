def heapify(heap, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(heap) and heap[left] > heap[largest]:
        largest = left
    if right < len(heap) and heap[right] > heap[largest]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest)


def delete(heap, value):
    heap.pop(value)
    heapify(heap, 0)


test = list(map(int, input().split()))
to_delete = list(map(int, input().split()))
for i in to_delete:
    delete(test, i)
    print(test)