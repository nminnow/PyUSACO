'''
ID: audrey.6
LANG: PYTHON3
PROB: milk2
'''

with open('milk2.in') as fin:
    n = int(next(fin).rstrip())
    times = []
    for _ in range(n):
        times.append(list(map(int, next(fin).rstrip().split())))
    if not times:
        times.append([0, 0])

times.sort()
ptimes = [times[0]]
for start, end in times:
    pstart, pend = ptimes[-1]
    if pend < start:
        ptimes.append([start, end])
    else:
        if pend < end:
            ptimes[-1][1] = end

maxidle = 0
pend = ptimes[0][1]
for start, end in ptimes[1:]:
    idle = start - pend
    if maxidle < idle:
        maxidle = idle
    pend = end

with open('milk2.out', 'w') as fout:
    fout.write(str(max(e - s for s, e in ptimes)) + ' ' + str(maxidle) + '\n')
