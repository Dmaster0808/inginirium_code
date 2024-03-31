import numpy

arr1 = numpy.arange(10)
arr2 = numpy.array([30, 30, 30, 30, 30, 5, 4, 3, 2, 1])
print(arr1)
print(arr2)

inner = True

for i, v in enumerate(arr1):
    if (v in arr2) == False:
        inner = False
        break
print(inner)
