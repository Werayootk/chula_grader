t1 = input().lower()
t2 = input().lower()
s1 = []
for c in t1:
    if '0'<=c<='9' or 'a'<=c<='z':
        s1.append(c)
s2 = []
for c in t2:
    if '0'<=c<='9' or 'a'<=c<='z':
        s2.append(c)

s1.sort()
s2.sort()

if s1 == s2:
    print('Anagram')
else:
    print('Not Anagram')
