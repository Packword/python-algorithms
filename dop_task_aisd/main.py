class Heap:
    def __init__(self, max_size):
        self.MAX_SIZE = max_size
        self.heap = [None] * max_size
        self.size = 0

    @staticmethod
    def get_parent(index):
        return (index - 1) // 2

    @staticmethod
    def get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child(index):
        return 2 * index + 2

    def insert(self, element):
        if self.size == self.MAX_SIZE:
            return -1
        self.heap[self.size] = element
        self.shift_up(self.size)
        self.size += 1

    def shift_up(self, index):
        parent = self.get_parent(index)
        while index > 0 and self.heap[parent][1] < self.heap[index][1]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.get_parent(index)

    def shift_down(self, index):
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        if left >= self.size and right >= self.size:
            return
        if right >= self.size:
            max_index = left if self.heap[left][1] < self.heap[index][1] else index
        else:
            max_index = left if self.heap[left][1] < self.heap[index][1] else right
            max_index = max_index if self.heap[max_index][1] < self.heap[index][1] else index
        if max_index != index:
            self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
            self.shift_down(index)


procs = 2
q = int(input("Максимальное время работы над задачей: "))
ktx = int(input("Время на переход: "))
heap = Heap(procs)
all_time = 0
times = []
for i in range(procs):
    heap.insert([i, 0])
for i in list(map(int, input("Введите времена задач: ").split())):
    times.append(i)
    all_time += i
while all_time:
    for i in range(len(times)):
        if times[i]:
            if times[i] > q:
                heap.heap[0][1] += (q + ktx)
                times[i] -= q
                all_time -= q
            else:
                heap.heap[0][1] += times[i] + ktx
                all_time -= times[i]
                times[i] = 0
                print("Время окончания задачи №", i, " = ", heap.heap[0][1] - ktx)
            heap.shift_down(0)
