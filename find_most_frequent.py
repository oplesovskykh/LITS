import string

def find_most_frequent(s):
    for char in string.punctuation:
        s = s.replace(char, ' ')
    s = s.split()
    a = list(set(s))
    d = {}
    for i in a:
        d[i] = s.count(i)
    frequent = [key for key, val in d.items() if val == max(d.values())]
    return frequent

print(find_most_frequent('Hello,Hello, my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))




