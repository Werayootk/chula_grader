# t1 = input().lower()
# t2 = input().lower()
# s1 = []
# for c in t1:
#     if '0'<=c<='9' or 'a'<=c<='z':
#         s1.append(c)
# s2 = []
# for c in t2:
#     if '0'<=c<='9' or 'a'<=c<='z':
#         s2.append(c)

# s1.sort()
# s2.sort()

# if s1 == s2:
#     print('Anagram')
# else:
#     print('Not Anagram')

text1 = input().lower()
text2 = input().lower()
sentence1 = []
sentence2 = []

for char in text1:
    if '0' <= char <= '9' or 'a' <= char <= 'z':
        sentence1.append(char)
for char in text2:
    if '0' <= char <= '9' or 'a' <= char <= 'z':
        sentence2.append(char)
sentence1.sort()
sentence2.sort()

if sentence1 == sentence2:
    print('YES')
else:
    print('NO')