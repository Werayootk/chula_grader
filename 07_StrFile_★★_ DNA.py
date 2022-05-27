dna = input().strip()
dna = dna.upper()
op = input().strip()
invalid = False
for c in dna:
    if c not in 'ACGT':
        invalid = True
        break
if invalid:
    print('Invalid DNA')
elif op == 'R':
    complement = ''
    for c in dna:
        if c == 'A':
            complement += 'T'
        elif c == 'T':
            complement += 'A'
        elif c == 'G':
            complement += 'C'
        else:
            complement += 'G'
    print(complement[::-1])
elif op == 'F':
    a = t = g = c = 0
    for s in dna:
        if s == 'A': a += 1
        elif s == 'T': t += 1
        elif s == 'G': g += 1
        else: c += 1
    print('A='+str(a)+', T='+str(t)+', G='+str(g)+', C='+str(c))
elif op == 'D':
    pair = input().strip()
    c = 0
    for i in range(len(dna)-1):
        if dna[i:i+2] == pair:
            c += 1
    print(c)
else:
    print('Invalid operation')