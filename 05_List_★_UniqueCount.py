x = list(range(30000))
d = []
for e in x:
    d.append(int(e))
unique = []
for e in d:
    if e not in unique:
        unique.append(e)
unique.sort()
print(len(unique))
print(unique[:10])