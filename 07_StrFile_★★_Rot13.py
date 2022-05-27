upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = 2*upper + 2*upper.lower()

while True:
    t = input()
    if t == 'end': break
    rot = ''
    for c in t:
        k = alphabets.find(c)
        if k >= 0:
            rot += alphabets[k+13]
        else:
            rot += c

    print(rot)