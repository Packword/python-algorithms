from matrix_change import matrix_sums, append_indexes
from merge_sort import merge
data = matrix_sums()
data = append_indexes(data)
merge(data)
for i in range(len(data)):
    print(data[i][1], end=" ")
