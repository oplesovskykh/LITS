import string

def alphabet():
    alph = {}
    d = list(string.ascii_uppercase)
    for i in d:
        alph[i] = 10 + d.index(i)
    return alph

def convert_to_dec(x, n):
    x = str(x)[::-1]
    res = 0
    if n > 10:
        alph = alphabet()
        for i in range(len(x)):
            num = x[i]
            if x[i] in alph.keys():
                num = alph[x[i]]
            res += int(num) * n**i
    else:
        for i in range(len(x)):
            res += int(x[i]) * n ** i
    return res


def convert_to_m(k, m):
    if m > 10:
        alph = alphabet()
        res = str(k % m)
        if res > 9:
            for i in alph.keys():
                if alph[i] == res:
                    res = i
        while k // m > 1:
            k = k // m
            res1 = k % m
            if res1 > 9:
                for i in alph.keys():
                    if alph[i] == res1:
                        res1 = i
            res = res + str(res1)
    else:
        res = str(k%m)
        while k // m > 1:
            k = k // m
            res = res + str(k % m)
        res = res +'1'
    return res[::-1]


def convert_n_to_m(x, n, m):
    if isinstance(n, int) and isinstance(m, int):
        if n < 1 or m > 36:
            return False
    if str(n) in str(x):
        return False
    if isinstance(x, int):
        x = convert_to_dec(x, n)
    if isinstance(x, str):
        x = convert_to_dec(x, n)
    else:
        return False
    result = convert_to_m(x, m)
    return result


print convert_n_to_m([123], 4, 3)  #False
print convert_n_to_m("0123", 5, 6) #102
print convert_n_to_m("123", 3, 5) #False
print convert_n_to_m(123, 4, 1) #000000000000000000000000000
print convert_n_to_m(-123.0, 11, 16) #False
print convert_n_to_m("A1Z", 36, 16) #32E7





