d = []
for i in range(int(input())):
    d.append(int(input()))
x = input().split()
for e in x:
    d.append(int(e))
e = int(input())
while e != -1:
    d.append(e)
    e = int(input())
out = []
for i in range(len(d)):
    if i%2 == 0:
        out.append(d[i])
    else:
        out.insert(0,d[i])
print(out)