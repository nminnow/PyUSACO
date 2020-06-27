'''
ID: audrey.6
LANG: PYTHON3
PROB: milk
'''

with open('milk.in') as fin:
    n, m = map(int, next(fin).rstrip().split())
    pas = []
    for _ in range(m):
        p, a = map(int, next(fin).rstrip().split())
        pas.append((p, a))

v = 0
r = n
pas.sort()
for p, a in pas:
    if a > r:
        v += r * p
        break
    else:
        v += a * p
        r -= a

with open('milk.out', 'w') as fout:
    fout.write(str(v) + '\n')
