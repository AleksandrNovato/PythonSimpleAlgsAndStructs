import algs as a
import random

random.seed()
A=[random.randint(-9,9)for i in range(20)]
print(A)
a.merge_sort(A)
print(A)