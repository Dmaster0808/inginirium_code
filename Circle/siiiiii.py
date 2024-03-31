def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break

lst = [2, 3, 4, 5, 5, 3, 9, 3, 0, 1, 8, 7, 5, 4, 3, 21, 45, 68, 79, 67, 58, 67, 47, 567, 4546, 346]

insertion_sort(lst)
for i in range(len(lst)):
    print(lst[i])