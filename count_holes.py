def count_holes(n):
    for char in n:
        if char.isalpha():
            print("ERROR")
            quit()
    if '.' in n:
        print('ERROR')
        quit()
    l = n.lstrip("0")
    l = l.lstrip("-")
    d = {'0':1,'1':0,'2':0,'3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1}
    s = 0
    l2 = list(l)
    for key in l2:
        if key in d:
            s += d[key]
    return s


print(count_holes('123'))
print(count_holes('906'))
print(count_holes('001'))
print(count_holes('-8'))
print(count_holes('-8.0'))