n = int(input())
su = set([int(e) for e in input().split()])
si = set(su)
for k in range(n):
    s = set([int(e) for e in input().split()])
    su |= s
    si &= s
print(len(su))
print(len(si))