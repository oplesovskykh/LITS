# check if parenthesis are balanced
# str = '((((((((((((((2, 3)))))))))))))'

str = '((((((((((((((2, 3)))))))))))))'
if str.count('(', 0, (len(str) / 2)) > str.count(')', ((len(str) / 2)+1), (len(str))):
    print('Parenthesis is overbalance to the left')
elif str.count('(', 0, (len(str) / 2)) < str.count(')', ((len(str) / 2)+1), (len(str))):
    print('Parenthesis is overbalance to the right')
else:
    print('Parenthesis is balanced')













