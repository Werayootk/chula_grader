def make_int_list(x):
    d = []
    for e in x.split():
        d.append(int(e))
    return d

def is_odd(e):
    return e%2 == 1

def odd_list(alist):
    odds = []
    for e in alist:
        if e%2 == 1:
            odds.append(e)
    return odds

def sum_square(alist):
    ssq = 0
    for e in alist:
        ssq += e*e
    return ssq

exec(input().strip())