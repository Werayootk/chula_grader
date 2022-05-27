cartoon = {}
atypes = []
while True:
    x = input()
    if x == 'q' : break
    name, atype = [e.strip() for e in x.split(',')]
    if atype not in cartoon:
        cartoon[atype] = []
        atypes.append(atype)
    cartoon[atype].append(name)

for atype in atypes:
    print(atype+': '+', '.join(cartoon[atype]))