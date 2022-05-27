n = int(input())
p = []
for i in range(n):
    x, y = input().split()
    x = float(x)
    y = float(y)
    d = (x*x + y*y)**0.5
    p.append([d, i+1, x, y])
p.sort()
d, k, x, y = p[2]
print('#'+ str(k)+':('+ str(x) + ',' + str(y) + ')')

"""
4
0.1 0.1
0.2 0.2
10.0 10.0
3.0 3.0
"""