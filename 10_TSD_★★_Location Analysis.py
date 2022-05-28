# visited = {}
# uids = []
# for k in range(int(input())):
#     uid, locs = [e.strip() for e in input().split(':')]
#     locs = set([e.strip() for e in locs.split(',')])
#     visited[uid] = locs
#     uids.append(uid)
# qid = input().strip()
# found = False
# for uid in uids:
#     if uid != qid and len(visited[qid] & visited[uid]) > 0:
#         print(uid)
#         found = True
# if not found:
#     print('Not Found')

traveled = {}
uids = []
for k in range(int(input())):
    kid, city = [e.strip() for e in input().split(':')]
    city = set([e.strip() for e in city.split(',')])
    traveled[kid] = city
    uids.append(kid)
uid = input().strip()
check = False
for kid in uids:
    if kid != uid and len(traveled[qid] & traveled[kid]) > 0: #
        print(kid)
        check = True
if not check:
    print('Not Found')

