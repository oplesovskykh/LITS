# make list flatten
# lst = [1, [2, 3], 4, [[6, 7]]]
# to
# lst = [1, 2, 3, 4, 6, 7]

list = [1, [2, 3], 4, [6, 7]]
lis = tuple(list[1]) + tuple(list[3])
list.pop(1)
list.pop(2)
list.extend(lis)
list.sort()
print(list)

