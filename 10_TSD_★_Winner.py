winners = set()
losers = set()
for k in range(int(input())):
    w, l = input().split()
    winners.add(w)
    losers.add(l)
print(sorted(winners - losers))

