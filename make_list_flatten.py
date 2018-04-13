# make list flatten
# lst = [1, [2, 3], 4, [[6, 7]]]
# to
# lst = [1, 2, 3, 4, 6, 7]

list = [1, [2, 3], 4, [[6, 7]]]
list_flatten = []
list2 = []
list3 = []
list4 = []

for i in list:
    if type(i) == int:
        list_flatten.append(i)
    else:
            list2 += tuple(i)
list_flatten = sorted(list_flatten + list2)
for i in list_flatten:
    if type(i) == int:
        list3.append(i)
    else:
        list4 += i
list_flatten = sorted(list3 + list4)
print(list_flatten)




