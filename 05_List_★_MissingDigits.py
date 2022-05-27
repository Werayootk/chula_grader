from string import digits


digits = list('0123456789')
x = input()
for c in x:
    if c in digits:
        digits.remove(c)
if len(digits) == 0:
    print('None')
else:
    print(''.join(digits))