cards = input().split()
cmd = input()
for c in cmd:
    if c == 'C':
        n = len(cards)
        cards = cards[n//2:] + cards[:n//2]
    elif c == 'S':
        s = ['']*n
        s[::2] = cards[:n//2]
        s[1::2] = cards[n//2:]
        cards = s
print(' '.join(cards))

"""
A J Q 10
"""