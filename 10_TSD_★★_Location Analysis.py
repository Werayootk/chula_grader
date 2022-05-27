visited = {}
uids = []
for k in range(int(input())):
    uid, locs = [e.strip() for e in input().split(':')]
    locs = set([e.strip() for e in locs.split(',')])
    visited[uid] = locs
    uids.append(uid)
qid = input().strip()
found = False
for uid in uids:
    if uid != qid and len(visited[qid] & visited[uid]) > 0:
        print(uid)
        found = True
if not found:
    print('Not Found')
