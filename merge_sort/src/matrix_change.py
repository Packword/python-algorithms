from input_data import input_data

def trace(arr):
    iter = 0
    matrix_sum = 0
    for i in arr:
        matrix_sum += i[iter]
        iter += 1
    return matrix_sum



def matrix_sums():
    n = int(input())
    sums = []
    for i in range(n):
        sums.append(trace(input_data()))
    return sums


def append_indexes(data):
    data = [[data[i], i] for i in range(len(data))]
    return data