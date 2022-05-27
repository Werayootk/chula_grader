time = {}
for k in range(int(input())):
    _, _, genre, t = [e.strip() for e in input().split()]
    m, s = [int(e) for e in t.split(':')]
    if genre not in time:
        time[genre] = 0
    time[genre] += m * 60 + s
x = [() for g,t in time.items()]
x.sort()
for t,g in x[-3:][::-1]:
    m = str(t//60)
    s = str(t%60)
    print(g, '-->'+m+' : '+s)   