IDs = []
grades = []
x = input()
while x != 'q':
    sid, g = x.split()
    IDs.append(sid)
    grades.append(g)
    x = input()
#-------------------------------------------
qIDs = input().split()
G = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+','A', 'A']
for qid in qIDs:
    if qid in IDs:
        i = IDs.index(qid)
        if grades[i] in G:
            k = G.index(grades[i])
            grades[i] = G[k+1]
#-------------------------------------------
for i in range(len(IDs)):
    print(IDs[i], grades[i])